import numpy as np

matrix = np.array(
    [
        [[1, 0, 0, 0.5], [0, 1, 0, 0.5], [0, 0, 1, 0], [0, 0, 0, 1]],
        [[0, 1, 0, 0.5], [1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
    ]
)

points = np.array([[1, 1, 1, 1], [0, 0, 0, 1], [1, -1, 0, 1]])

print((matrix @ points.T).transpose(0, 2, 1))
