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
        definitions = []

        # Find all definition blocks
        def_blocks = soup.find_all("div", {"class": "definition-block"})

        for block in def_blocks:
            # Extract POS and Definition
            header = block.find("div", {"class": "definition-header"})
            pos_tag = header.find("div", {"class": "part-of-speech-label"})
            pos = pos_tag.get_text(strip=True) if pos_tag else "N/A"

            def_tag = header.find("div", {"class": "definition"})
            definition = def_tag.get_text(strip=True) if def_tag else "N/A"

            synonyms = []
            antonyms = []

            panels = block.find_all("section", {"class": "synonym-antonym-panel"})
            for panel in panels:
                label_div = panel.find("div", {"class": "synonym-antonym-panel-label"})
                if not label_div:
                    continue

                label = label_div.get_text(strip=True)
                is_synonym = "Synonyms" in label
                is_antonym = "Antonyms" in label

                if not (is_synonym or is_antonym):
                    continue

                # Find all word chips
                word_chips = panel.find_all("a", {"class": "word-chip"})
                for chip in word_chips:
                    term = chip.get_text(strip=True)

                    # Extract similarity from class
                    classes = chip.get("class", [])
                    similarity = "0"
                    for cls in classes:
                        if cls.startswith("similarity-"):
                            similarity = cls.replace("similarity-", "")
                            break

                    item = {"term": term, "similarity": similarity}

                    if is_synonym:
                        synonyms.append(item)
                    elif is_antonym:
                        antonyms.append(item)

            definitions.append(
                {
                    "definition": definition,
                    "pos": pos,
                    "synonyms": synonyms,
                    "antonyms": antonyms,
                }
            )

        self.data = definitions
        return definitions

    def extract_info(self):
        if self.data:
            return self.format_definitions(self.data)

        rprint(
            f"\n[cayn]Oops, it looks like thesaurus.com doesn't recognize '{self.word}' as a valid word."
        )
        return []

    def format_definitions(self, definitions):
        colors = {
            "100": "[rgb(252,232,197)]",
            "50": "[rgb(220,221,187)]",
            "10": "[rgb(191,182,155)]",
            "-100": "[grey74]",
            "-50": "[grey58]",
            "-10": "[grey42]",
            "0": "[grey42]",  # Default fallback
        }

        definitions_synonyms_antonyms = []
        for definition in definitions:
            def_text = definition.get("definition", "N/A")
            pos = definition.get("pos", "N/A")
            synonyms = [
                colors.get(syn["similarity"], "[grey42]") + syn["term"] + "[/]"
                for syn in definition.get("synonyms", [])
            ]
            antonyms = [
                colors.get(ant["similarity"], "[grey74]") + ant["term"] + "[/]"
                for ant in definition.get("antonyms", [])
            ]
            definitions_synonyms_antonyms.append(
                (f"{pos}. {def_text}", synonyms, antonyms)
            )
        return definitions_synonyms_antonyms

    def plain(self):
        response_text = self.fetch_data()
        if response_text:
            self.parse_data(response_text)
            if not self.data:
                print(
                    f"Oops, it looks like thesaurus.com doesn't recognize '{self.word}' as a valid word."
                )
                return

            for definition_data in self.data:
                def_text = definition_data.get("definition", "N/A")
                pos = definition_data.get("pos", "N/A")
                print(f"{pos}. {def_text}")

                synonyms = [s["term"] for s in definition_data.get("synonyms", [])]
                if synonyms:
                    print(f"synonyms: {', '.join(synonyms)}")

                antonyms = [a["term"] for a in definition_data.get("antonyms", [])]
                if antonyms:
                    print(f"antonyms: {', '.join(antonyms)}")
                print()

    def rich(self):
        response_text = self.fetch_data()
        if response_text:
            self.parse_data(response_text)
            definitions_synonyms_antonyms = self.extract_info()
            if definitions_synonyms_antonyms:
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
