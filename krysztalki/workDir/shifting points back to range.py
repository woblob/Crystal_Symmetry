import numpy as np

arr = np.array([[1, -0.5, 2],
                [0, 1, 2],
                [-2, -1.5, 0.75]])

print(arr)

def get_back_in_range(array):
    mask = np.where(array > 1)
    array[mask] -= 1

    mask = np.where(array < -1)
    array[mask] += 1

    return array

print(func(arr))