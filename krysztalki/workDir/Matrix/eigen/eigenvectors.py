import numpy as np


def get_eigenvectors( mat: np.ndarray[np.dtype[float]] ) -> np.ndarray[np.dtype[float]]:
    _, vectors = np.linalg.eigh(mat)
    return vectors


# resize parameters of the vector to be at most 1
def resize_vectors( vectors: np.ndarray[np.dtype[float], np.dtype[int]] ) -> np.ndarray[np.dtype[float]]:
    local_extremum = np.max(np.abs(vectors), axis=0)
    return vectors / local_extremum


if __name__ == "__main__":
    matrix = np.array(
        [[0, 1, 0, 0],
         [-1, 0, 0, 0],
         [0, 0, -1, 0],
         [0, 0, 0, 1]]
    )
    eigenvectors = get_eigenvectors( matrix )
    resized_vectors = resize_vectors(eigenvectors)
    print(f"eigenvectors\n{eigenvectors}", end="\n\n")
    print(f"resized_vectors\n{resized_vectors}")
