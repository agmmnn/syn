from urllib.parse import quote
import requests
from rich import print


def tur_main(word):
    url = "https://radyal-api.vercel.app/api/esanlam?word=" + quote(word)
    r = requests.get(url)
    data = r.json()
    if not "error" in data:
        print("🔵" + ", ".join(data["synonyms"])) if data["synonyms"] else None
        print("🟤" + ", ".join(data["antonyms"])) if data["antonyms"] else None
    else:
        print(data["error"])
