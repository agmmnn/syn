from synonym_cli.cli import Synonym


def test_req(capsys):
    with capsys.disabled():
        word = Synonym("lighter")
        fetch = word.fetch_data()
        definitions = word.parse_data(fetch)

        # New structure: definitions is a list of dicts
        assert type(definitions) == list
        assert len(definitions) > 0

        # Check first definition structure
        first_def = definitions[0]
        assert "synonyms" in first_def
        assert type(first_def["synonyms"]) == list
        assert len(first_def["synonyms"]) > 0

        # Check first synonym
        first_syn = first_def["synonyms"][0]
        assert first_syn["term"] == "raft"
        assert first_syn["similarity"] == "100"
