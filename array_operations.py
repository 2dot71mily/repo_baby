import numpy as np

def create_random_array(size, low=0, high=100):
    return np.random.randint(low, high, size)

def array_mean(arr):
    return np.mean(arr)

def array_std(arr):
    return np.std(arr)

def elementwise_multiply(arr1, arr2):
    return np.multiply(arr1, arr2)

def reshape_array(arr, shape):
    try:
        return np.reshape(arr, shape)
    except ValueError:
        raise ValueError("Cannot reshape array to the given shape")