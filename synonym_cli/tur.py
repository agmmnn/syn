from urllib.parse import quote
import requests
from rich import print


def tur_main(word):
    q_es = "🔵"
    q_zit = "🟤"
    url = "https://radyal-api.vercel.app/api/esanlam?word=" + quote(word)
    r = requests.get(url)
    data = r.json()
    print(data["synonyms"]) if data["synonyms"] else None
    print(data["antonyms"]) if data["antonyms"] else None
