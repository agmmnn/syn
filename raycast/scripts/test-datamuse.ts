import { fetchDatamuseData } from "../src/api/datamuse";

async function main() {
  const word = "happy";
  console.log(`Fetching Datamuse data for "${word}"...`);
  const data = await fetchDatamuseData(word);
  console.log(JSON.stringify(data, null, 2));
}

main();
