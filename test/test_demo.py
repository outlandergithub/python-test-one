import pytest

@pytest.fixture()
def before_after():
    print("Fixture before running test")
    yield
    print("Fixture after running test")

def test_one(before_after: None):
    assert 1 == 1

def test_two(before_after: None):
    assert "one" == "one"

def test_fail(before_after: None):
    assert not "one" == "one"