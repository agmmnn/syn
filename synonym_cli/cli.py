from urllib.parse import quote
from json import loads
from gazpacho import Soup
import http.client
from rich.table import Table
from rich.console import Console
from rich import box
from rich import print as rprint


class Synonym:
    def __init__(self, word, arg_plain=False):
        self.word = quote(word)
        self.arg_plain = arg_plain
        self.main()

    def req(self):
        conn = http.client.HTTPSConnection("www.thesaurus.com")
        url = "/browse/" + self.word
        conn.request("GET", url)
        html = conn.getresponse().read().decode("utf-8")
        soup = Soup(html)
        js = ""
        for i in soup.find("script", mode="all"):
            if "window.INITIAL_STATE" in i.text:
                js = i.text[23:-1].replace(":undefined", ':"undefined"')

        try:
            jsondata = loads(js)
        except Exception as e:
            print(e)
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
            didym = soup.find("span", attrs={"class": "css-1umtscx e1rvdh510"})
            if didym is not None:
                rprint("[cyan]" + didym.text + " " + didym.find("a").text)
                rprint(
                    "\n[cyan]More suggestions:\n"
                    + ", ".join(
                        [
                            i.text
                            for i in soup.find(
                                "div", attrs={"class": "css-5kov97 e1wla5061"}
                            ).find("a", mode="all")
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
            print("⬤synonyms: " + ", ".join(syn_lst))
            if dic[i]["antonyms"] == []:
                print()
            else:
                ant_lst = []
                for j in dic[i]["antonyms"]:
                    ant_lst.append(j[0])
                print("⬤antonyms: " + ", ".join(ant_lst))
                print()

    def rich(self, dic):
        for i in dic:
            colors = {
                "100": ["[rgb(252,232,197)]", "[/rgb(252,232,197)]"],
                "50": ["[rgb(220,221,187)]", "[/rgb(220,221,187)]"],
                "10": ["[rgb(191,182,155)]", "[/rgb(191,182,155)]"],
                "-100": ["[grey74]", "[/grey74]"],
                "-50": ["[grey58]", "[/grey58]"],
                "-10": ["[grey42]", "[grey42]"],
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
                    "🟤[grey74]antonyms: [/grey74]"
                    + "[grey74],[/grey74] ".join(
                        [
                            colors[tups[1]][0] + "".join(tups[0]) + colors[tups[1]][1]
                            for tups in dic[i]["antonyms"]
                        ]
                    )
                )
            rprint(table)
        Console().print(
            f"[grey42][link=https://www.thesaurus.com/browse/{self.word}]thesaurus.com↗[/link]",
            justify="right",
        )

    def main(self):
        self.plain(self.req()) if self.arg_plain else self.rich(self.req())
