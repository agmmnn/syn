<div align="center"><img src="https://github.com/agmmnn/syn/assets/16024979/7d40727c-cc35-4bea-9679-1cad46ae0850" alt="syn"><a alt="Github" href="https://github.com/agmmnn/syn"><img alt="GitHub release" src="https://img.shields.io/github/v/release/agmmnn/syn"></a> <a href="https://pypi.org/project/synonym-cli/"><img alt="PyPI" src="https://img.shields.io/pypi/v/synonym-cli"></a> <a href="https://pepy.tech/project/synonym-cli"><img alt="PyPI" src="https://pepy.tech/badge/synonym-cli"></a></div>

# 🌾 syn

Get synonyms and antonyms of words from [Thesaurus.com](https://www.thesaurus.com/), [Datamuse API](https://www.datamuse.com/api/) and [AlterVista](https://thesaurus.altervista.org/) in your terminal, with [rich](https://github.com/Textualize/rich) output.

# Install:

```
pip install synonym-cli
```

## Usage:

```
syn <word>
```

### Explore Mode

Returns more particular results about the given word. Uses [Datamuse API](https://www.datamuse.com/api/).

> for Web UI: https://wordwhisper.vercel.app

`$ syn dominant -d`
![](https://github.com/agmmnn/syn/assets/16024979/a9ba9df5-bad0-421a-abea-163d11c37f1d)

### Other Languages

For other languages you can use `--lang`, `-l` command. To use this feature, you need to get an api key from [here](https://thesaurus.altervista.org/openapi).

`$ syn -l fr belle`
![](https://user-images.githubusercontent.com/16024979/209144768-0cde6709-65d9-4142-9eae-bb4bc38e4a13.png)

`$ syn -l ru фраза`
![](https://user-images.githubusercontent.com/16024979/209144765-abca9b54-5495-4295-98f7-15acdbde7623.png)

> AlterVista's Thesaurus API supports the following languages:

> Czech: `cs`, Danish: `da`, English (US): `en`, French: `fr`, German (Germany): `de`, German (Switzerland): `de`, Greek: `el`, Hungarian: `hu`, Italian: `it`, Norwegian: `no`, Polish: `pl`, Portuguese: `pt`, Romanian: `ro`, Russian: `ru`, Slovak: `sk`, Spanish: `es`.

### Set Default Language

You can set the default language with the `--setlang <lang_code>` argument, so you don't have to give the `-l` argument every time.

```
$ syn --setlang fr
> default language is: fr
$ syn belle
> ...
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

# Contrubuting

Contributions are welcome. If you want to contribute to this list send a pull request or just open a new issue.
