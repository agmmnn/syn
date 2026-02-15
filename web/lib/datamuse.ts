export interface DatamuseItem {
  word: string;
  score: number;
  tags?: string[];
}

export interface CategoryResult {
  category: string;
  items: string[];
}

export const CATEGORIES: Record<string, { endpoint: string; param: string }> = {
  Similars: { endpoint: "words", param: "ml" },
  Synonyms: { endpoint: "words", param: "rel_syn" },
  Antonyms: { endpoint: "words", param: "rel_ant" },
  Evocative: { endpoint: "words", param: "rel_trg" },
  "Sounds Like": { endpoint: "words", param: "sl" },
  "Similar Spelling": { endpoint: "words", param: "sp" },
  Rhymes: { endpoint: "words", param: "rel_rhy" },
  "Adjectives for word": { endpoint: "words", param: "rel_jjb" },
  "Nouns for word": { endpoint: "words", param: "rel_jja" },
  Suggestions: { endpoint: "sug", param: "s" },
};

export const CATEGORY_COLORS: Record<string, string> = {
  Similars: "var(--cat-similars)",
  Synonyms: "var(--cat-synonyms)",
  Antonyms: "var(--cat-antonyms)",
  Evocative: "var(--cat-evocative)",
  "Sounds Like": "var(--cat-sounds)",
  "Similar Spelling": "var(--cat-spelling)",
  Rhymes: "var(--cat-rhymes)",
  "Adjectives for word": "var(--cat-adjectives)",
  "Nouns for word": "var(--cat-nouns)",
  Suggestions: "var(--cat-suggestions)",
};

const BASE_URL = "https://api.datamuse.com";

async function fetchCategory(
  word: string,
  category: string,
  topic?: string,
): Promise<CategoryResult> {
  const { endpoint, param } = CATEGORIES[category];
  const queryParams = new URLSearchParams({ [param]: word, max: "20" });
  if (topic) queryParams.append("topics", topic);

  try {
    const res = await fetch(`${BASE_URL}/${endpoint}?${queryParams}`);
    if (!res.ok) throw new Error(res.statusText);
    const data = (await res.json()) as DatamuseItem[];
    return {
      category,
      items: data
        .filter((item) => item.word.toLowerCase() !== word.toLowerCase())
        .map((item) => item.word),
    };
  } catch {
    return { category, items: [] };
  }
}

export async function fetchAll(
  wordInput: string,
  categoryFilter?: string,
): Promise<CategoryResult[]> {
  const [word, topic] = wordInput.split(":");
  if (!word) return [];

  const categoriesToFetch = categoryFilter
    ? [categoryFilter]
    : Object.keys(CATEGORIES);

  const results = await Promise.all(
    categoriesToFetch.map((cat) => fetchCategory(word, cat, topic)),
  );

  return results.filter((r) => r.items.length > 0);
}
