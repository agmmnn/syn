import { Action, ActionPanel, List } from "@raycast/api";
import { usePromise } from "@raycast/utils";
import { useState } from "react";
import { fetchThesaurusData, Definition } from "./api/thesaurus";

export default function Command() {
  const [searchText, setSearchText] = useState("");

  const { isLoading, data } = usePromise(fetchThesaurusData, [searchText], {
    execute: !!searchText,
    initialData: [],
  });

  return (
    <List
      isLoading={isLoading}
      onSearchTextChange={setSearchText}
      searchBarPlaceholder="Search for a word (e.g. happy)"
      throttle
      isShowingDetail={data.length > 0}
    >
      {data.map((def, index) => (
        <List.Item
          key={index}
          title={def.definition}
          subtitle={def.pos}
          detail={
            <List.Item.Detail markdown={getMarkdownContent(def, searchText)} />
          }
          actions={
            <ActionPanel>
              <Action.CopyToClipboard title="Copy Definition" content={def.definition} />
              <Action.CopyToClipboard
                title="Copy Synonyms"
                content={def.synonyms.map((s) => s.term).join(", ")}
              />
              <Action.CopyToClipboard
                title="Copy Antonyms"
                content={def.antonyms.map((s) => s.term).join(", ")}
              />
              <Action.OpenInBrowser url={`https://www.thesaurus.com/browse/${searchText}`} />
            </ActionPanel>
          }
        />
      ))}
    </List>
  );
}

function getMarkdownContent(def: Definition, word: string): string {
  const synonyms = def.synonyms.map((s) => {
    return s.similarity === "100" ? `**${s.term}**` : s.term;
  }).join(", ");

  const antonyms = def.antonyms.map((s) => {
      return s.similarity === "-100" ? `**${s.term}**` : s.term;
  }).join(", ");

  return `
# ${word}
*(${def.pos})* ${def.definition}

---

### 🔵 Synonyms
${synonyms || "None"}

### 🟤 Antonyms
${antonyms || "None"}
`;
}
