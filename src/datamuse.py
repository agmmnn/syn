import asyncio
from os import name as os_name
from rich import print, box
from rich.table import Table
from json import loads
from aiohttp import ClientSession


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
                "ml": "🔡[green]synonyms/similars: ",
                "sl": "📣[green]sound\[saʊnd]: ",
                "sp": "🧮[green]similar spelling: ",
                "rel_trg": "💭[green]evocative: ",
                "rel_rhy": "👂[green]rhymic: ",
                "rel_jjb": f"[green]___ + [i]{self.word}[/]: ",
                "rel_jja": f"[green][i]{self.word}[/] + ___: ",
            },
            "sug": {"s": f"[green][i]{self.word}[/]...:"},
        }
        tasks = []
        for i in dic:
            for j in dic[i]:
                url = f"https://api.datamuse.com/{i}?{j}={self.word}&max={self.max}&topics={self.topics}"
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
                table = Table(box=box.MINIMAL, expand=True, padding=0)
                table.add_column(dic[i][j])
                table.add_row(", ".join(word_list))
                tables.append(table)
                idx += 1
        topics = self.topics.split(",")
        middle_text = f"""

{self.word}{("🪢("+" • ".join(topics)+")") if topics!=[""] else ""}

        """

        middle = Table(box=None, show_header=False, expand=True, padding=0)
        middle.add_column(justify="center")
        middle.add_row(middle_text)

        grid1 = Table.grid(padding=0, expand=True)
        grid1.add_row(tables[0], tables[3])
        print(grid1)

        grid2 = Table.grid(padding=0, expand=True)
        grid2.add_row(tables[1], tables[2], tables[4])
        grid2.add_row(tables[5], tables[6], tables[7])
        print(grid2)

    async def main(self):
        async with ClientSession() as session:
            await self.fetch_all(session)
