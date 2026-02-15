import fetch from "node-fetch";

export interface DatamuseItem {
  word: string;
  score: number;
  tags?: string[];
}

export interface DatamuseResult {
  category: string;
  items: string[];
}

const BASE_URL = "https://api.datamuse.com";

const ENDPOINTS: Record<string, Record<string, string>> = {
  words: {
    ml: "Similars",
    rel_syn: "Synonyms",
    rel_ant: "Antonyms",
    rel_trg: "Evocative",
    sl: "Sounds Like",
    sp: "Similar Spelling",
    rel_rhy: "Rhymes",
    rel_jjb: "Adjectives modifying word",
    rel_jja: "Nouns modified by word",
  },
  sug: {
    s: "Suggestions",
  },
};

export async function fetchDatamuseData(wordInput: string): Promise<DatamuseResult[]> {
  const [word, topic] = wordInput.split(":");
  const max = 15;
  const tasks: Promise<{ category: string; items: string[] }>[] = [];

  for (const endpointType in ENDPOINTS) {
    for (const param in ENDPOINTS[endpointType]) {
      const category = ENDPOINTS[endpointType][param];
      const queryParams = new URLSearchParams();
      queryParams.append(param, word);
      queryParams.append("max", max.toString());
      if (topic) {
        queryParams.append("topics", topic);
      }

      const url = `${BASE_URL}/${endpointType}?${queryParams.toString()}`;

      tasks.push(
        fetch(url)
          .then((res) => {
            if (!res.ok) throw new Error(res.statusText);
            return res.json() as Promise<DatamuseItem[]>;
          })
          .then((data) => {
            const items = data
              .filter((item) => item.word.toLowerCase() !== word.toLowerCase())
              .map((item) => item.word);
            return { category, items };
          })
          .catch((err) => {
            console.error(`Error fetching ${category}:`, err);
            return { category, items: [] };
          }),
      );
    }
  }

  const results = await Promise.all(tasks);
  return results.filter((res) => res.items.length > 0);
}
