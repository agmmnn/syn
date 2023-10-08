import asyncio
from os import name as os_name
from rich import print, box
from rich.table import Table
from json import loads
from aiohttp import ClientSession
from urllib.parse import urlencode


class DataMuse:
    def __init__(self, word, max: int = 15):
        self.word = word
        self.max = max
        if len(self.word.split(":")) > 1:
            self.topics = self.word.split(":")[1]
            self.word = self.word.split(":")[0]
        else:
            self.topics = ""

        if os_name == "nt":
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(self.main())

    async def fetch(self, session, url):
        async with session.get(url) as response:
            if response.status != 200:
                response.raise_for_status()
            return await response.text()

    async def fetch_all(self, session):
        dic = {
            "words": {
                "ml": "🔡[green]similars: ",
                "rel_syn": "🔵[green]synonyms: ",
                "rel_ant": "🟤[green]antonyms: ",
                "rel_trg": "💭[green]evocative: ",
                "sl": "📣[green]sound\[saʊnd]: ",
                "sp": "🧮[green]similar spelling: ",
                "rel_rhy": "👂[green]rhymic: ",
                "rel_jjb": f"[green]___ + [i]{self.word}[/]: ",
                "rel_jja": f"[green][i]{self.word}[/] + ___: ",
            },
            "sug": {"s": f"[green][i]{self.word}[/]...:"},
        }
        tasks = []
        base_url = "https://api.datamuse.com"
        for i in dic:
            for j in dic[i]:
                url_args = urlencode(
                    {j: self.word, "max": self.max, "topics": self.topics}
                )
                url = f"{base_url}/{i}?{url_args}"
                task = asyncio.create_task(self.fetch(session, url))
                tasks.append(task)
        results = await asyncio.gather(*tasks)
        tables = []
        idx = 0
        for i in dic:
            for j in dic[i]:
                word_list = []
                for results[idx] in loads(results[idx]):
                    if results[idx]["word"] != self.word:
                        word_list.append(results[idx]["word"])
                    else:
                        continue
                table = Table(box=box.SIMPLE, expand=True, padding=0)
                table.add_column(dic[i][j])
                row_words = ", ".join(word_list)
                table.add_row("[cyan3]" + row_words)
                if row_words:
                    tables.append(table)
                idx += 1

        topics = self.topics.split(",")
        desc = f'{self.word}{("🪢("+" • ".join(topics)+")") if topics!=[""] else ""}'
        # Iterate through the tables in increments of 3
        for i in range(0, len(tables), 3):
            grid = Table.grid(padding=0, expand=True)
            # Get the current group of 3 tables
            group = tables[i : i + 3]
            # Add the group to a row in the grid
            grid.add_row(*group)
            print(grid)

    async def main(self):
        async with ClientSession() as session:
            await self.fetch_all(session)
