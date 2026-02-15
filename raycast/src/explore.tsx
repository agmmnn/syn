import { Action, ActionPanel, List } from "@raycast/api";
import { useCachedPromise } from "@raycast/utils";
import { useState } from "react";
import { fetchDatamuseData, CATEGORIES, DatamuseResult } from "./api/datamuse";

const ALL = "All";

export default function Command() {
  const [searchText, setSearchText] = useState("");
  const [category, setCategory] = useState(ALL);

  const filter = category === ALL ? undefined : category;

  const { isLoading, data } = useCachedPromise(
    (word: string, cat: string | undefined) => fetchDatamuseData(word, cat),
    [searchText, filter],
    {
      execute: searchText.length > 0,
      keepPreviousData: true,
    },
  );

  const results = data ?? [];

  return (
    <List
      isLoading={isLoading}
      onSearchTextChange={setSearchText}
      searchBarPlaceholder="Explore a word (e.g. ocean or ocean:nature)"
      throttle
      searchBarAccessory={
        <List.Dropdown tooltip="Category" storeValue onChange={setCategory}>
          <List.Dropdown.Item title="All" value={ALL} />
          <List.Dropdown.Section title="Categories">
            {Object.keys(CATEGORIES).map((cat) => (
              <List.Dropdown.Item key={cat} title={cat} value={cat} />
            ))}
          </List.Dropdown.Section>
        </List.Dropdown>
      }
    >
      {results.map((group: DatamuseResult, index: number) => (
        <List.Section key={index} title={group.category} subtitle={`${group.items.length} words`}>
          {group.items.map((word, wIndex) => (
            <List.Item
              key={wIndex}
              title={word}
              actions={
                <ActionPanel>
                  <Action.CopyToClipboard title="Copy Word" content={word} />
                  <Action.Paste title="Paste Word" content={word} />
                  <Action.CopyToClipboard
                    title="Copy All in Category"
                    content={group.items.join(", ")}
                  />
                </ActionPanel>
              }
            />
          ))}
        </List.Section>
      ))}
    </List>
  );
}
