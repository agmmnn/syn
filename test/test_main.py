from synonym_cli.cli import Synonym


def test_req(capsys):
    with capsys.disabled():
        word = Synonym("lighter")
        fetch = word.fetch_data()
        data = word.parse_data(fetch)
        results_data = data["tuna"]["resultsData"]
        definition_data = results_data["definitionData"]
        definitions = definition_data["definitions"]

        assert type(definitions) == list
        assert definitions[0]["synonyms"][0]["targetSlug"] == "raft"
        assert definitions[0]["synonyms"][0]["similarity"] == "100"
