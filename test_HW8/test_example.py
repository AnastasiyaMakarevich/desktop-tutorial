import pytest
import random


def test_len():
    assert len([1, 2, 3]) == 3
    assert len("Nastya") == 6
    assert len("") == 0

def test_sum():
    assert sum([1, 2, 3, 4]) == 10
    assert sum([]) == 0
    assert sum([-2, 2, 0]) == 0

def test_sorted():
    assert sorted([3, 1, 2]) == [1, 2, 3]
    assert sorted([]) == []
    assert sorted(["b", "a", "c"]) == ["a", "b", "c"]

@pytest.fixture
def random_list():
    return [random.randint(1, 100) * 2 for _ in range(10)]

def test_even(random_list):
    for num in random_list:
        assert num % 2 == 0

@pytest.fixture
def odd_random_list():
    return [random.randint(1, 100) * 2 + 1 for _ in range(10)]

def test_odd(odd_random_list):
    for num in odd_random_list:
        assert num % 2 != 0

@pytest.mark.basic
def test_len():
    assert len([1, 2, 3]) == 3
    assert len("Nastya") == 6
    assert len("") == 0

@pytest.mark.basic
def test_sum():
    assert sum([1, 2, 3, 4]) == 10
    assert sum([]) == 0
    assert sum([-2, 2, 0]) == 0

@pytest.mark.basic
def test_sorted():
    assert sorted([3, 1, 2]) == [1, 2, 3]
    assert sorted([]) == []
    assert sorted(["b", "a", "c"]) == ["a", "b", "c"]

@pytest.mark.random
def test_even(random_list):
    for num in random_list:
        assert num % 2 == 0

@pytest.mark.random
def test_odd1(odd_random_list):
    for num in odd_random_list:
        assert num % 2 != 0
