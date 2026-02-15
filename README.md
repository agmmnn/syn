<div align="center">
  <img src="https://github.com/agmmnn/syn/assets/16024979/7d40727c-cc35-4bea-9679-1cad46ae0850" alt="syn" width="400">

  <p>
    <a href="https://synnn.vercel.app"><img alt="Web App" src="https://img.shields.io/badge/web-synnn.vercel.app-c9a96e?style=flat-square"></a>
    <a href="https://pypi.org/project/synonym-cli/"><img alt="PyPI" src="https://img.shields.io/pypi/v/synonym-cli?style=flat-square&color=c9a96e"></a>
    <a href="https://pepy.tech/project/synonym-cli"><img alt="Downloads" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpepy.tech%2Fapi%2Fv2%2Fprojects%2Fsynonym-cli&query=%24.total_downloads&style=flat-square&label=downloads&color=c9a96e"></a>
    <a href="https://github.com/agmmnn/syn/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/badge/license-MIT-c9a96e?style=flat-square"></a>
  </p>

  <h3>The word toolkit for your terminal, desktop, and browser.</h3>
  <p>Synonyms, antonyms, rhymes, and related words — powered by <a href="https://www.thesaurus.com/">Thesaurus.com</a>, <a href="https://www.datamuse.com/api/">Datamuse</a>, and <a href="https://thesaurus.altervista.org/">AlterVista</a>.</p>
</div>

<br>

<div align="center">

|              **Terminal**              |            **Raycast**             |                     **Web**                      |
| :------------------------------------: | :--------------------------------: | :----------------------------------------------: |
| [`pip install synonym-cli`](#terminal) | [**Install Extension**](./raycast) | [**synnn.vercel.app**](https://synnn.vercel.app) |

</div>

<br>

## Terminal

Feature-rich CLI to explore words directly from your command line.

### Installation

```bash
pip install synonym-cli
```

### Usage

**Quick Lookup** (Synonyms & Antonyms via Thesaurus.com)

```bash
syn happy
```

**Explore Mode** (Related words, rhymes, and more via Datamuse)

```bash
syn dominant -d
```

<img src="https://github.com/agmmnn/syn/assets/16024979/a9ba9df5-bad0-421a-abea-163d11c37f1d" alt="Explore Mode Example" width="600">

**Multi-Language** (16 languages via AlterVista)

```bash
syn -l fr belle   # French
syn -l ru фраза   # Russian
```

<img src="https://user-images.githubusercontent.com/16024979/209144768-0cde6709-65d9-4142-9eae-bb4bc38e4a13.png" alt="Multi-Language Example" width="600">

<details>
<summary><strong>See all CLI options</strong></summary>

```text
syn <word> [options]

  -d, --datamuse    explore mode (Datamuse API)
  -p, --plain       plain text output
  -l, --lang        target language code
  --setkey          set AlterVista API key
  --setlang         set default language
  --show            show settings
  -v, --version     show version
```

</details>

## Raycast Extension

Native macOS extension to find the right word without leaving your context.

| Command           | Description                                                                  |
| :---------------- | :--------------------------------------------------------------------------- |
| **Synonyms**      | Synonyms & antonyms from Thesaurus.com with color-coded similarity tags.     |
| **Word Explorer** | 10 Datamuse categories — similars, rhymes, sounds like, evocative, and more. |
| **Look Up**       | Select text anywhere, trigger via hotkey for instant results.                |

👉 [**View Extension Details**](./raycast)

## Web

**[synnn.vercel.app](https://synnn.vercel.app)** — A clean web interface to explore words.

- Explore 10 categories from Datamuse.
- Drill down by clicking any word.
- Shareable URLs for specific words.

## Contributing

Contributions are welcome! Please [open an issue](https://github.com/agmmnn/syn/issues) or submit a pull request.

## License

[MIT](LICENSE)
