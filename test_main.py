from main import hello


def test_main():
    assert "Hello" == hello()


def test_fail():
    assert "Bye" == hello()
