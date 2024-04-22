import pytest
import random
from bubble_sort import bubble_sort


def test_small_list():
    sorted_list = [1, 5, 8]
    unsorted_list = [5, 8, 1]
    bubble_sort(unsorted_list)

    assert sorted_list == unsorted_list

def test_over_100_elements():
    unsorted_list = []
    for i in range(0, 150):
        unsorted_list.append(random.randint(0, 500))
    bubble_sort(unsorted_list)
    
    for y in range(0, len(unsorted_list) -1 ):
        if unsorted_list[y] > unsorted_list[y + 1]:
            assert False
    assert True

def test_empty_list():
    sorted_list = []
    bubble_sort(sorted_list)

    assert sorted_list == []


def test_non_list_parameters():
    with pytest.raises(TypeError):
        bubble_sort(None)
    with pytest.raises(TypeError):
        bubble_sort(True)
    with pytest.raises(TypeError):
        bubble_sort(245)