import requests
from urllib.parse import quote
from rich import print, box
from rich.table import Table
from urllib.parse import urlencode
from .settings import settings_get

api_base = "https://thesaurus.altervista.org/thesaurus/v1"
lang_dict = {
    "cs": "cs_CZ",
    "da": "da_DK",
    "de": "de_DE",
    "el": "el_GR",
    "en": "en_US",
    "es": "es_ES",
    "fr": "fr_FR",
    "hu": "hu_HU",
    "it": "it_IT",
    "no": "no_NO",
    "pl": "pl_PL",
    "pt": "pt_PT",
    "ro": "ro_RO",
    "ru": "ru_RU",
    "sk": "sk_SK",
}


def alter_main(word, lang):
    if lang not in lang_dict:
        print("incorrect language code: " + lang)
        exit()
    lang_code = lang_dict[lang]
    apikey = settings_get("altervista_apikey")
    if apikey == "":
        print("you need altervista apikey to use this feature.")
        print(
            "• if you don't have apikey yet, get a free key from: [cyan link=https://thesaurus.altervista.org/mykey]https://thesaurus.altervista.org/mykey[/]"
        )
        print("• if you have an apikey, use: [cyan]--setkey <apikey>[/]")
        exit()

    url_args = urlencode(
        {"word": word, "language": lang_code, "key": apikey, "output": "json"}
    )
    url = f"{api_base}?{url_args}"
    js_data = requests.get(url).json()

    if "error" in js_data:
        # https://thesaurus.altervista.org/thesaurus/v1?word=root&language=en_US&output=json&key=xxxxxx
        # {"error":"xxxxxx dfg is invalid"}
        # {"error":"unsupported value for parameter language x"}
        # {"error":"no result found"}
        print(js_data["error"])
        exit()

    list_result = []
    for i in js_data["response"]:
        syns = [
            i["list"]["category"],
            i["list"]["synonyms"]
            .replace(" (similar term)", "")
            .replace(" (related term)", "")
            .replace(" (generic term)", "")
            .replace(" (fig.)", "")
            .replace(" (antonym)", "(antonym)")
            .split("|"),
        ]
        list_result.append(syns)

    table = Table(
        # row_styles=("medium_spring_green", "cyan"),
        show_header=False,
        box=box.ROUNDED,
        padding=0,
    )
    if len(list_result) == 1:
        table.add_row(list_result[0][0], ", ".join(list_result[0][1]))
        print(table)
        return

    item = []
    for x, i in enumerate(list_result):
        if not x % 2:
            item = [i[0], ", ".join(i[1])]
        else:
            table.add_row(item[0], item[1], i[0], ", ".join(i[1]))

    if len(list_result) % 2:
        table.add_row(item[0], item[1], "", "")

    print(table)
