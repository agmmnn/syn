import argparse
from importlib_metadata import version, metadata

from .cli import Synonym
from .tur import tur_main
from .altervista import alter_main
from .settings import settings_set, settings_get, settings_show
from .datamuse import DataMuse

# parse arguments
ap = argparse.ArgumentParser()
ap.add_argument(
    "word",
    type=str,
    nargs="*",
    help="<word>",
)
ap.add_argument(
    "-p",
    "--plain",
    action="store_true",
    default=False,
    help="returns plain text output",
)
ap.add_argument(
    "-l",
    "--lang",
    type=str,
    help="<language>",
)
ap.add_argument("--setkey", type=str, help="set apikey for altervista api")
ap.add_argument(
    "--setlang",
    type=str,
    help=f"set default language",
)
ap.add_argument(
    "-d",
    "--datamuse",
    action="store_true",
    default=False,
    help="show datamuse",
)
ap.add_argument(
    "--show",
    action="store_true",
    default=False,
    help="show settings file",
)
ap.add_argument(
    "-v",
    "--version",
    action="version",
    version=f"🌾syn {version('synonym-cli')}",
)
args = ap.parse_args()


def cli():
    if args.setkey:
        settings_set("altervista_apikey", args.setkey)
        print("api key added successfully.")
        exit()
    if args.setlang:
        settings_set("default_lang", args.setlang)
        print("default language is: " + args.setlang)
        exit()
    if args.show:
        settings_show()
        exit()

    lang = args.lang if args.lang else settings_get("default_lang")
    word = " ".join(args.word)
    if word == "":
        print("enter a word...")
        exit()
    if args.datamuse:
        DataMuse(word)
        exit()
    if lang == "en":
        if not args.plain:
            Synonym(word).rich()
        else:
            Synonym(word).plain()
    elif lang == "tr":
        tur_main(word)
    else:
        alter_main(word, lang)


if __name__ == "__main__":
    cli()
