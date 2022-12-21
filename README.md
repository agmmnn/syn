![screenshot](https://user-images.githubusercontent.com/16024979/162848437-8da9d5d4-a234-44d3-94d8-048f92b015a6.png)

<div align="center">
<a alt="Github" href="https://github.com/agmmnn/synonym-cli"><img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/agmmnn/synonym-cli"></a>
<a href="https://pypi.org/project/synonym-cli/"><img alt="PyPI" src="https://img.shields.io/pypi/v/synonym-cli"></a>
</div>

# synonym-cli

<div align="center">

Synonyms and antonyms of words from [Thesaurus.com](https://www.thesaurus.com/) and other sources are now in your terminal, with [rich](https://github.com/Textualize/rich) output.

</div>

# Install:

```
pip install synonym-cli
```

## Usage:

```
syn <word>
```

```
$ syn nominate
┌──────────────────────────────────────────────────────────────────────────────────┐
│ ❯ designate, select (verb)                                                       │
├──────────────────────────────────────────────────────────────────────────────────┤
│ 🔵synonyms: appoint, assign, choose, decide, draft, elect, elevate, name,        │
│ present, propose, recommend, submit, suggest, tap, call, commission, denominate, │
│ empower, intend, make, mean, offer, proffer, purpose, slate, slot, specify,      │
│ tender, term, cognominate, put down for, put up, tab                             │
│                                                                                  │
│ 🟤antonyms: condemn, dissuade, ignore, refuse, reject, deny, discourage, stop,   │
│ take back, pass over                                                             │
└──────────────────────────────────────────────────────────────────────────────────┘

```

## Different Languages `--lang`, `-l`

Multi-language support with Thesaurus AlterVista. API key is required, if you don't have any apikey yet, get a free key from, [thesaurus.altervista.org/openapi](https://thesaurus.altervista.org/openapi).

```
$ syn -l es expresión
╭─┬──────────────────────────────────┬─┬──────────────────────────────────╮
│-│elocución, dicción, estilo        │-│exteriorización, manifestación,   │
│ │                                  │ │revelación, comunicación          │
│-│gesto, rostro, cara, semblante,   │-│locución, frase, dicho, giro      │
│ │aire, aspecto                     │ │                                  │
╰─┴──────────────────────────────────┴─┴──────────────────────────────────╯

$ syn -l ru фраза
╭─────────┬────────────────────────────────────────┬────────────────┬─────╮
│(синоним)│речь, слово, предложение, спич, тост,   │(сходный термин)│слово│
│         │здравица, аллокуция, диатриба, рацея,   │                │     │
│         │тирада, филиппика, изложение, слог,     │                │     │
│         │стиль, перо                             │                │     │
╰─────────┴────────────────────────────────────────┴────────────────┴─────╯
```

> AlterVista's Thesaurus API supports the following languages:

> Czech: `cs`, Danish: `da`, English (US): `en`, French: `fr`, German (Germany): `de`, German (Switzerland): `de`, Greek: `el`, Hungarian: `hu`, Italian: `it`, Norwegian: `no`, Polish: `pl`, Portuguese: `pt`, Romanian: `ro`, Russian: `ru`, Slovak: `sk`, Spanish: `es`.

### Set Default Language

You can set the default language with the `--setlang <lang_code>` argument, so you don't have to give the `-l` argument every time.

```
$ syn --setlang fr
$ syn belle
╭──────────────┬──────────────────────────────────────────────────────────╮
│(Adjectif Nom)│adorable, admirable, brillante, charmante, céleste,       │
│              │délicate, divine, délicieuse, éblouissante, élégante,     │
│              │éclatante, exquise, féerique, harmonieuse, agréable,      │
│              │ajustée, accordée, équilibrée, eurythmique, mélodieuse,   │
│              │musicale, ordonnée, proportionnée, symétrique             │
╰──────────────┴──────────────────────────────────────────────────────────╯
```

## Arguments

```
  -h, --help      show this help message and exit
  -p, --plain     returns plain text output
  -l, --lang      <language>
  --setkey        set apikey for altervista api
  --setlang       set default language (currently default is 'en')
  --show          show settings file
  -v, --version   show program's version number and exit
```
