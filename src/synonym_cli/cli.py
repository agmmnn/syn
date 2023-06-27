from urllib.parse import quote
import requests
from bs4 import BeautifulSoup
import json
from rich.table import Table
from rich.console import Console
from rich import box
from rich import print as rprint

class Synonym:
    def __init__(self, word):
        self.word = quote(word)

    def req(self):
        
        url = f"https://www.thesaurus.com/browse/{self.word}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        script = soup.find('script', {'id': 'preloaded-state'})
        if script is not None:
            script_text = script.string

            start = script_text.find('{')
            end = script_text.rfind('}') + 1
            json_text = script_text[start:end]

            data = json.loads(json_text)
            
            tuna_data = data['tuna']
            results_data = tuna_data['resultsData']
            if results_data is None:
                    rprint(f"[cayn]{self.word} is not a word (according to thesaurus.com)")
                    return []
                
            definition_data = results_data['definitionData']
            definitions = definition_data['definitions']

            colors = {
                "100": "[rgb(252,232,197)]",
                "50": "[rgb(220,221,187)]",
                "10": "[rgb(191,182,155)]",
                "-100": "[grey74]",
                "-50": "[grey58]",
                "-10": "[grey42]",
            }

            definitions_synonyms_antonyms = []
            for definition in definitions:
                def_text = definition.get('definition', 'N/A')
                pos = definition.get('pos', 'N/A')
                synonyms = [colors[syn['similarity']] + syn['term'] + "[/]" for syn in definition.get('synonyms', [])]
                antonyms = [colors[ant['similarity']] + ant['term'] + "[/]" for ant in definition.get('antonyms', [])]
                definitions_synonyms_antonyms.append((f"{pos}. {def_text}", synonyms, antonyms))
            
            return definitions_synonyms_antonyms

    def rich(self):
        definitions_synonyms_antonyms = self.req()
        console = Console()

        for definition, synonyms, antonyms in definitions_synonyms_antonyms:
            def_split = definition.split('.')
            part_of_speech = def_split[0]
            def_text = def_split[1].strip()
            table = Table(box=box.SQUARE)
            table.add_column("[blue]❯ " + def_text + " [gray50](" + part_of_speech + ")")
            table.add_row("🔵[cyan3]Synonyms:[/cyan3] " +
                          "[grey50],[/grey50] ".join(synonyms))
            if antonyms:
                table.add_row("🟤[grey74]Antonyms:[/grey74] " +
                              "[grey74],[/grey74] ".join(antonyms))
            console.print(table)
        console.print(
            f"[grey42][link=https://www.thesaurus.com/browse/{self.word}]thesaurus.com↗[/link]",
            justify="right",
        )
