import pytest
from list_operations import find_max, remove_duplicates, sum_even_numbers

def test_find_max():
    assert find_max([1, 5, 3, 9, 2]) == 9
    assert find_max([-1, -5, -3]) == -1
    assert find_max([0]) == 0

def test_find_max_empty_list():
    with pytest.raises(ValueError):
        find_max([])

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
    assert remove_duplicates([1, 1, 1, 1]) == [1]
    assert remove_duplicates([]) == []

def test_sum_even_numbers():
    assert sum_even_numbers([1, 2, 3, 4, 5, 6]) == 12
    assert sum_even_numbers([1, 3, 5, 7]) == 0
    assert sum_even_numbers([]) == 0