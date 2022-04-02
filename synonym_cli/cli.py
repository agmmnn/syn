import requests
from urllib.parse import quote
from bs4 import BeautifulSoup
import json
from rich.table import Table
from rich import box
from rich import print as rprint


class Synonym:
    def __init__(self, word, arg_plain=False):
        self.word = quote(word)
        self.arg_plain = arg_plain
        self.main()

    def req(self):
        url = "https://www.thesaurus.com/browse/" + self.word
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "lxml")
        js = ""
        for i in soup.find_all("script"):
            if "window.INITIAL_STATE" in str(i):
                js = str(i)[31:-10].replace(":undefined", ':"undefined"')

        try:
            jsondata = json.loads(js)
        except ValueError:
            print("try again...")
            exit()

        try:
            self.term = jsondata["searchData"]["searchTerm"]
            tabs = jsondata["searchData"]["tunaApiData"]["posTabs"]
            dic = {}
            for i in tabs:
                synlis = [(i["term"], i["similarity"]) for i in i["synonyms"]]
                antlis = [(i["term"], i["similarity"]) for i in i["antonyms"]]
                dic[i["definition"]] = {
                    "pos": i["pos"],
                    "synonyms": synlis,
                    "antonyms": antlis,
                }
            return dic
        except Exception:
            didym = soup.find("span", class_="css-1umtscx e1rvdh510")
            if didym is not None:
                rprint("[cyan]" + didym.text)
                rprint(
                    "\n[cyan]More suggestions:\n"
                    + ", ".join(
                        [
                            i.text
                            for i in soup.find(
                                "div", class_="css-5kov97 e1wla5061"
                            ).find_all("a")
                        ]
                    )
                    + "."
                )
            else:
                rprint("[cyan]not found")
            exit()

    def plain(self, dic):
        for i in dic:
            print("❯" + i + " (" + dic[i]["pos"] + ")")
            syn_lst = []
            for j in dic[i]["synonyms"]:
                syn_lst.append(j[0])
            print("⬤synonyms: " + ",".join(syn_lst))
            if dic[i]["antonyms"] != []:
                ant_lst = []
                for j in dic[i]["antonyms"]:
                    ant_lst.append(j[0])
                print("⬤antonyms: " + ",".join(ant_lst))
                print()

    def rich(self, dic):
        # rprint("\t" + self.term + " | Thesaurus")
        for i in dic:
            colors = {
                "100": ["[rgb(252,232,197)]", "[/rgb(252,232,197)]"],
                "50": ["[rgb(220,221,187)]", "[/rgb(220,221,187)]"],
                "10": ["[rgb(191,182,155)]", "[/rgb(191,182,155)]"],
                "-100": ["", ""],
                "-50": ["", ""],
                "-10": ["", ""],
            }
            # SQUARE, ROUNDED, SIMPLE_HEAD, MINIMAL_HEAVY_HEAD
            table = Table(box=box.SQUARE)
            # ! TODO: must be sorted by tuple[1]
            table.add_column(
                "[cyan]❯ " + i + "[/cyan]" + "[grey50]" + " (" + dic[i]["pos"] + ")"
            )
            table.add_row(
                "🔵[cyan3]synonyms:[/cyan3] "
                + "[grey50],[/grey50] ".join(
                    [
                        colors[tups[1]][0] + "".join(tups[0]) + colors[tups[1]][1]
                        for tups in dic[i]["synonyms"]
                    ]
                )
            )
            if dic[i]["antonyms"] != []:
                table.add_row()
                table.add_row(
                    "🟤[cyan3]antonyms: "
                    + "[grey50],[/grey50] ".join(
                        [
                            colors[tups[1]][0] + "".join(tups[0]) + colors[tups[1]][1]
                            for tups in dic[i]["antonyms"]
                        ]
                    )
                )
            rprint(table)

    def main(self):
        self.plain(self.req()) if self.arg_plain else self.rich(self.req())
