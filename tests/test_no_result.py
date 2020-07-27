from resultful import NoResult


def test_special_methods() -> None:
    assert bool(NoResult) is False
    assert repr(NoResult) == "resultful.NoResult"
