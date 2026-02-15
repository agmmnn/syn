import { Action, ActionPanel, Color, List } from "@raycast/api";
import { useCachedPromise } from "@raycast/utils";
import { useState } from "react";
import { fetchThesaurusData, SynonymItem } from "./api/thesaurus";

function similarityColor(similarity: string): Color {
  switch (similarity) {
    case "100":
      return Color.Yellow;
    case "50":
      return Color.Green;
    case "10":
      return Color.Blue;
    case "-10":
      return Color.SecondaryText;
    case "-50":
      return Color.Orange;
    case "-100":
      return Color.Red;
    default:
      return Color.PrimaryText;
  }
}

export default function Command() {
  const [searchText, setSearchText] = useState("");

  const { isLoading, data } = useCachedPromise(fetchThesaurusData, [searchText], {
    execute: searchText.length > 0,
    keepPreviousData: true,
  });

  const definitions = data ?? [];

  return (
    <List
      isLoading={isLoading}
      onSearchTextChange={setSearchText}
      searchBarPlaceholder="Search for a word (e.g. happy)"
      throttle
      isShowingDetail={definitions.length > 0}
    >
      {definitions.map((def, index) => (
        <List.Item
          key={index}
          title={def.definition}
          subtitle={def.pos}
          detail={
            <List.Item.Detail
              metadata={
                <List.Item.Detail.Metadata>
                  <List.Item.Detail.Metadata.Label title="Part of Speech" text={def.pos} />
                  <List.Item.Detail.Metadata.Label title="Definition" text={def.definition} />
                  <List.Item.Detail.Metadata.Separator />
                  <List.Item.Detail.Metadata.TagList title="Synonyms">
                    {def.synonyms.length > 0 ? (
                      def.synonyms.map((s: SynonymItem, i: number) => (
                        <List.Item.Detail.Metadata.TagList.Item
                          key={i}
                          text={s.term}
                          color={similarityColor(s.similarity)}
                        />
                      ))
                    ) : (
                      <List.Item.Detail.Metadata.TagList.Item text="None" color={Color.SecondaryText} />
                    )}
                  </List.Item.Detail.Metadata.TagList>
                  <List.Item.Detail.Metadata.Separator />
                  <List.Item.Detail.Metadata.TagList title="Antonyms">
                    {def.antonyms.length > 0 ? (
                      def.antonyms.map((s: SynonymItem, i: number) => (
                        <List.Item.Detail.Metadata.TagList.Item
                          key={i}
                          text={s.term}
                          color={similarityColor(s.similarity)}
                        />
                      ))
                    ) : (
                      <List.Item.Detail.Metadata.TagList.Item text="None" color={Color.SecondaryText} />
                    )}
                  </List.Item.Detail.Metadata.TagList>
                </List.Item.Detail.Metadata>
              }
            />
          }
          actions={
            <ActionPanel>
              <Action.CopyToClipboard title="Copy Definition" content={def.definition} />
              <Action.CopyToClipboard
                title="Copy Synonyms"
                content={def.synonyms.map((s: SynonymItem) => s.term).join(", ")}
              />
              <Action.CopyToClipboard
                title="Copy Antonyms"
                content={def.antonyms.map((s: SynonymItem) => s.term).join(", ")}
              />
              <Action.OpenInBrowser url={`https://www.thesaurus.com/browse/${searchText}`} />
            </ActionPanel>
          }
        />
      ))}
    </List>
  );
}
