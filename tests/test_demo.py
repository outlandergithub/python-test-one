import pytest

@pytest.mark.smoke
def test_one(before_after: None):
    assert 1 == 1

@pytest.mark.regression
def test_two(before_after: None):
    assert "one" == "one"

@pytest.mark.xfail
def test_failed(before_after: None):
    assert not "one" == "one"

@pytest.mark.skip(reason="Skipped on purpose for making more examples")
def test_skipped(before_after: None):
    assert not "one" == "one"

def test_None():
    sentinel = object()
    guard = None
    print(sentinel)
    print(guard)
    assert sentinel is not None

