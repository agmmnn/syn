import * as cheerio from "cheerio";
import fetch from "node-fetch";

export interface SynonymItem {
  term: string;
  similarity: string;
}

export interface Definition {
  definition: string;
  pos: string;
  synonyms: SynonymItem[];
  antonyms: SynonymItem[];
}

export async function fetchThesaurusData(word: string): Promise<Definition[]> {
  const url = `https://www.thesaurus.com/browse/${encodeURIComponent(word)}`;

  try {
    const response = await fetch(url);
    if (!response.ok) {
        if (response.status === 404) {
            return [];
        }
        throw new Error(`Failed to fetch data: ${response.statusText}`);
    }
    const html = await response.text();
    const $ = cheerio.load(html);
    const definitions: Definition[] = [];

    const defBlocks = $(".definition-block");

    defBlocks.each((_, block) => {
      const header = $(block).find(".definition-header");
      const posTag = header.find(".part-of-speech-label");
      const pos = posTag.length ? posTag.text().trim() : "N/A";

      const defTag = header.find(".definition");
      const definitionText = defTag.length ? defTag.text().trim() : "N/A";

      const synonyms: SynonymItem[] = [];
      const antonyms: SynonymItem[] = [];

      const panels = $(block).find(".synonym-antonym-panel");

      panels.each((_, panel) => {
        const labelDiv = $(panel).find(".synonym-antonym-panel-label");
        if (!labelDiv.length) return;

        const label = labelDiv.text().trim();
        const isSynonym = label.includes("Synonyms");
        const isAntonym = label.includes("Antonyms");

        if (!isSynonym && !isAntonym) return;

        const wordChips = $(panel).find("a.word-chip");
        wordChips.each((_, chip) => {
          const term = $(chip).text().trim();
          const classes = $(chip).attr("class")?.split(/\s+/) || [];
          let similarity = "0";

          for (const cls of classes) {
            if (cls.startsWith("similarity-")) {
              similarity = cls.replace("similarity-", "");
              break;
            }
          }

          const item: SynonymItem = { term, similarity };

          if (isSynonym) {
            synonyms.push(item);
          } else if (isAntonym) {
            antonyms.push(item);
          }
        });
      });

      definitions.push({
        definition: definitionText,
        pos,
        synonyms,
        antonyms,
      });
    });

    return definitions;
  } catch (error) {
    console.error("Error fetching Thesaurus data:", error);
    return [];
  }
}
