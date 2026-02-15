import { Action, ActionPanel, List } from "@raycast/api";
import { usePromise } from "@raycast/utils";
import { useState } from "react";
import { fetchDatamuseData, DatamuseResult } from "./api/datamuse";

export default function Command() {
  const [searchText, setSearchText] = useState("");

  const { isLoading, data } = usePromise(fetchDatamuseData, [searchText], {
    execute: !!searchText,
    initialData: [],
  });

  return (
    <List
      isLoading={isLoading}
      onSearchTextChange={setSearchText}
      searchBarPlaceholder="Search word (e.g. happy or happy:topic)"
      throttle
    >
      {data.map((categoryGroup: DatamuseResult, index: number) => (
        <List.Section key={index} title={categoryGroup.category}>
          {categoryGroup.items.map((word, wIndex) => (
             <List.Item
               key={wIndex}
               title={word}
               actions={
                 <ActionPanel>
                   <Action.CopyToClipboard title="Copy Word" content={word} />
                   <Action.Paste title="Paste Word" content={word} />
                   <Action.CopyToClipboard
                      title="Copy All in Category"
                      content={categoryGroup.items.join(", ")}
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
