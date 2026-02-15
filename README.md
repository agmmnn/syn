<div align="center">
  <img src="https://github.com/agmmnn/syn/assets/16024979/7d40727c-cc35-4bea-9679-1cad46ae0850" alt="syn">
  <p><strong>Synonyms, antonyms, and related words — everywhere.</strong></p>
  <p>
    <a href="https://github.com/agmmnn/syn"><img alt="GitHub release" src="https://img.shields.io/github/v/release/agmmnn/syn"></a>
    <a href="https://pypi.org/project/synonym-cli/"><img alt="PyPI" src="https://img.shields.io/pypi/v/synonym-cli"></a>
    <a href="https://pepy.tech/project/synonym-cli"><img alt="Downloads" src="https://pepy.tech/badge/synonym-cli"></a>
  </p>
</div>

---

**syn** is a word lookup toolkit powered by [Thesaurus.com](https://www.thesaurus.com/), [Datamuse API](https://www.datamuse.com/api/), and [AlterVista](https://thesaurus.altervista.org/). Available as a CLI tool and a Raycast extension.

## Packages

| Package                           | Description                                        | Path                    |
| --------------------------------- | -------------------------------------------------- | ----------------------- |
| [**CLI**](#cli)                   | Terminal-based synonym lookup with rich output     | [`cli/`](./cli)         |
| [**Raycast**](#raycast-extension) | Native macOS extension with drill-down exploration | [`raycast/`](./raycast) |
| **Web**                           | _Coming soon_                                      | —                       |

## CLI

> `pip install synonym-cli`

```
syn <word>
```

### Thesaurus

Get synonyms and antonyms with color-coded similarity scores and rich terminal output.

`$ syn happy`

### Explore Mode

Returns detailed results using [Datamuse API](https://www.datamuse.com/api/) — similars, rhymes, sounds like, and more.

`$ syn happy -d`

![](https://github.com/agmmnn/syn/assets/16024979/a9ba9df5-bad0-421a-abea-163d11c37f1d)

### Other Languages

Supports 16 languages via [AlterVista API](https://thesaurus.altervista.org/openapi) (requires free API key):

```
syn -l fr belle
syn -l ru фраза
```

![](https://user-images.githubusercontent.com/16024979/209144768-0cde6709-65d9-4142-9eae-bb4bc38e4a13.png)

<details>
<summary>Supported languages</summary>

Czech `cs`, Danish `da`, English `en`, French `fr`, German `de`, Greek `el`, Hungarian `hu`, Italian `it`, Norwegian `no`, Polish `pl`, Portuguese `pt`, Romanian `ro`, Russian `ru`, Slovak `sk`, Spanish `es`

</details>

<details>
<summary>All CLI arguments</summary>

```
syn <word> [options]

  -d, --datamuse    use Datamuse explore mode
  -p, --plain       plain text output (no colors)
  -l, --lang        target language code
  --setkey          set AlterVista API key
  --setlang         set default language
  --show            show settings file
  -v, --version     show version
  -h, --help        show help
```

</details>

## Raycast Extension

Three commands for fast word lookup on macOS:

### Synonyms

Look up synonyms and antonyms from Thesaurus.com. Definitions are shown with color-coded tags by similarity. Press Enter to browse individual words, then drill down recursively.

### Word Explorer

Explore words across 10 categories from Datamuse — similars, rhymes, sounds like, similar spelling, evocative, and more. Filter by category with the dropdown. Enter on any word drills down to explore it.

### Look Up

Select a word anywhere on your Mac, trigger this command (assign a hotkey), and it opens Synonyms with that word. Both Synonyms and Word Explorer also auto-fill from selected/clipboard text as fallback.

## Data Sources

| Source                                          | Used for                                          | Type          |
| ----------------------------------------------- | ------------------------------------------------- | ------------- |
| [Thesaurus.com](https://www.thesaurus.com/)     | Synonyms, antonyms, definitions                   | HTML scraping |
| [Datamuse API](https://www.datamuse.com/api/)   | Similars, rhymes, sounds like, spelling, and more | REST API      |
| [AlterVista](https://thesaurus.altervista.org/) | Multi-language synonyms (CLI only)                | REST API      |

## Contributing

Contributions are welcome. Open an issue or send a pull request.

## License

MIT
