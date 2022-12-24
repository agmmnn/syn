from synonym_cli.cli import Synonym


def test_req(capsys):
    with capsys.disabled():
        assert type(Synonym("lighter").req()) == dict
        assert Synonym("lighter").req()["large work boat"]["synonyms"][0][0] == "raft"
        assert Synonym("lighter").req()["large work boat"]["synonyms"][0][1] == "100"
