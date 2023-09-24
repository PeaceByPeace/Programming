from hello import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    for name in ["Ilya", "David", "Sergey"]:
        assert hello(name) == f"hello, {name}"
