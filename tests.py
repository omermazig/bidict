import pytest


@pytest.fixture()
def two_way_dict(request) -> dict:
    # Return your object here
    raise NotImplementedError


# Tests for both TwoWayDictNaive and TwoWayDictReverse
def test_add_and_get_keys_for_value(two_way_dict):
    two_way_dict["a"] = 1
    two_way_dict["b"] = 2
    two_way_dict["c"] = 1
    assert set(two_way_dict.get_keys_for_value(1)) == {"a", "c"}
    assert two_way_dict.get_keys_for_value(2) == {"b"}
    assert two_way_dict.get_keys_for_value(3) == set()


def test_update_value(two_way_dict):
    two_way_dict["a"] = 1
    two_way_dict["b"] = 2
    two_way_dict["a"] = 3
    assert two_way_dict.get_keys_for_value(1) == set()
    assert two_way_dict.get_keys_for_value(3) == {"a"}


def test_pop_key(two_way_dict):
    two_way_dict["a"] = 1
    two_way_dict["b"] = 2
    two_way_dict.pop("a")
    assert two_way_dict.get_keys_for_value(1) == set()
    assert two_way_dict.get_keys_for_value(2) == {"b"}


def test_nonstring_value(two_way_dict):
    two_way_dict["a"] = (1,)
    two_way_dict["b"] = 2
    two_way_dict["a"] = (3, 4)
    assert two_way_dict.get_keys_for_value((1,)) == set()
    assert two_way_dict.get_keys_for_value(1) == set()
    assert two_way_dict.get_keys_for_value((3, 4)) == {"a"}
