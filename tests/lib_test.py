from toto.lib import whats_my_name

def test_largo():
    res = whats_my_name()
    assert len(res) != 0

def test_whoiam():
    res = whats_my_name()
    assert 'Daniel' in res
