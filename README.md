<div align="center">
  <img src="https://github.com/agmmnn/syn/assets/16024979/7d40727c-cc35-4bea-9679-1cad46ae0850" alt="syn" width="400">

  <p>
    <a href="https://synnn.fly.dev"><img alt="Web App" src="https://img.shields.io/badge/web-synnn.fly.dev-c9a96e?style=flat-square"></a>
    <a href="https://pypi.org/project/synonym-cli/"><img alt="PyPI" src="https://img.shields.io/pypi/v/synonym-cli?style=flat-square&color=c9a96e"></a>
    <a href="https://pepy.tech/project/synonym-cli"><img alt="Downloads" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpepy.tech%2Fapi%2Fv2%2Fprojects%2Fsynonym-cli&query=%24.total_downloads&style=flat-square&label=downloads&color=c9a96e"></a>
    <a href="https://github.com/agmmnn/syn/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/badge/license-MIT-c9a96e?style=flat-square"></a>
  </p>

  <p><strong>The word toolkit for your terminal, desktop (Raycast), and browser.</strong></p>
  <p>Synonyms, antonyms, rhymes, and related words — powered by <a href="https://www.thesaurus.com/">Thesaurus.com</a>, <a href="https://www.datamuse.com/api/">Datamuse</a>, and <a href="https://thesaurus.altervista.org/">AlterVista</a>.</p>
</div>

<br>

<table>
<tr>
<td width="33%" align="center"><strong>Terminal</strong><br><code>pip install synonym-cli</code></td>
<td width="33%" align="center"><strong>Raycast</strong><br><a href="./raycast">Install Extension</a></td>
<td width="33%" align="center"><strong>Web</strong><br><a href="https://synnn.fly.dev">synnn.fly.dev</a></td>
</tr>
</table>

<br>

## Web

> **[synnn.fly.dev](https://synnn.fly.dev)** — explore words across 10 categories from Datamuse. Click any word to drill down. Shareable URLs.

## Terminal

```bash
pip install synonym-cli
```

```bash
syn <word>          # synonyms & antonyms from Thesaurus.com
syn <word> -d       # explore mode via Datamuse API
syn -l fr <word>    # 16 languages via AlterVista
```

### Explore Mode

`$ syn dominant -d`

![](https://github.com/agmmnn/syn/assets/16024979/a9ba9df5-bad0-421a-abea-163d11c37f1d)

### Multi-Language

```bash
syn -l fr belle
syn -l ru фраза
```

![](https://user-images.githubusercontent.com/16024979/209144768-0cde6709-65d9-4142-9eae-bb4bc38e4a13.png)

Supports Czech, Danish, English, French, German, Greek, Hungarian, Italian, Norwegian, Polish, Portuguese, Romanian, Russian, Slovak, and Spanish via [AlterVista](https://thesaurus.altervista.org/openapi) (free API key required).

<details>
<summary>All CLI options</summary>

```
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

## Raycast

Native macOS extension with three commands:

| Command           | Description                                                                                                                        |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Synonyms**      | Synonyms & antonyms from Thesaurus.com with color-coded similarity tags. Enter to browse words, drill down recursively.            |
| **Word Explorer** | 10 Datamuse categories — similars, rhymes, sounds like, spelling, evocative, and more. Filter by category. Drill down on any word. |
| **Look Up**       | Select text anywhere, trigger with a hotkey — instantly opens Synonyms for that word.                                              |

Both commands accept an inline argument and auto-fill from selected text or clipboard.

## Contributing

Contributions are welcome. [Open an issue](https://github.com/agmmnn/syn/issues) or send a pull request.

## License

[MIT](LICENSE)
