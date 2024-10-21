import pytest
import numpy as np
from array_operations import create_random_array, array_mean, array_std, elementwise_multiply, reshape_array

def test_create_random_array():
    arr = create_random_array(10, 0, 100)
    assert len(arr) == 10
    assert all(0 <= x < 100 for x in arr)

def test_array_mean():
    arr = np.array([1, 2, 3, 4, 5])
    assert array_mean(arr) == 3.0

def test_array_std():
    arr = np.array([1, 2, 3, 4, 5])
    assert pytest.approx(array_std(arr)) == 1.4142135

def test_elementwise_multiply():
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    result = elementwise_multiply(arr1, arr2)
    np.testing.assert_array_equal(result, np.array([4, 10, 18]))

def test_reshape_array():
    arr = np.array([1, 2, 3, 4, 5, 6])
    reshaped = reshape_array(arr, (2, 3))
    np.testing.assert_array_equal(reshaped, np.array([[1, 2, 3], [4, 5, 6]]))

def test_reshape_array_invalid_shape():
    arr = np.array([1, 2, 3, 4, 5])
    with pytest.raises(ValueError):
        reshape_array(arr, (2, 3))