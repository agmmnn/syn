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
        self.data = None

    def fetch_data(self):
        try:
            url = f"https://www.thesaurus.com/browse/{self.word}"
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error during requests to {url} : {str(e)}")
            return None
        return response.text

    def parse_data(self, response_text):
        soup = BeautifulSoup(response_text, "html.parser")
        script = soup.find("script", {"id": "preloaded-state"})
        if script is not None:
            script_text = script.string
            start = script_text.find("{")
            end = script_text.rfind("}") + 1
            json_text = script_text[start:end]
            data = json.loads(json_text)
            self.data = data
            return data

    def extract_info(self):
        if self.data:
            results_data = self.data["tuna"]["resultsData"]
            if results_data is None:
                rprint(
                    f"\n[cayn]Oops, it looks like thesaurus.com doesn't recognize '{self.word}' as a valid word."
                )
                return []

            definition_data = results_data["definitionData"]
            definitions = definition_data["definitions"]
            return self.format_definitions(definitions)
        return []

    def format_definitions(self, definitions):
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
            def_text = definition.get("definition", "N/A")
            pos = definition.get("pos", "N/A")
            synonyms = [
                colors[syn["similarity"]] + syn["term"] + "[/]"
                for syn in definition.get("synonyms", [])
            ]
            antonyms = [
                colors[ant["similarity"]] + ant["term"] + "[/]"
                for ant in definition.get("antonyms", [])
            ]
            definitions_synonyms_antonyms.append(
                (f"{pos}. {def_text}", synonyms, antonyms)
            )
        return definitions_synonyms_antonyms

    def rich(self):
        response_text = self.fetch_data()
        if response_text:
            self.parse_data(response_text)
            definitions_synonyms_antonyms = self.extract_info()
            self.display_definitions(definitions_synonyms_antonyms)

    def display_definitions(self, definitions_synonyms_antonyms):
        console = Console()
        for definition, synonyms, antonyms in definitions_synonyms_antonyms:
            def_split = definition.split(".")
            part_of_speech = def_split[0]
            def_text = def_split[1].strip()
            table = Table(box=box.SQUARE, leading=1)
            table.add_column(
                "[blue]❯ " + def_text + " [gray50](" + part_of_speech + ")"
            )
            table.add_row(
                "🔵[cyan3]synonyms:[/cyan3] " + "[grey50],[/grey50] ".join(synonyms)
            )
            if antonyms:
                table.add_row(
                    "🟤[grey74]antonyms:[/grey74] "
                    + "[grey74],[/grey74] ".join(antonyms)
                )
            console.print(table)
        console.print(
            f"[grey42][link=https://www.thesaurus.com/browse/{self.word}]thesaurus.com↗[/link]",
            justify="right",
        )
