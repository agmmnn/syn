import { fetchThesaurusData } from "../src/api/thesaurus";

async function main() {
  const word = "happy";
  console.log(`Fetching data for "${word}"...`);
  const data = await fetchThesaurusData(word);
  console.log(JSON.stringify(data, null, 2));
}

main();
