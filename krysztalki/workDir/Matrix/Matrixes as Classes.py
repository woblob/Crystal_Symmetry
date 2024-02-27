import numpy as np


def generateSymetryBaseQUAD():
    return {
        "c": {"000": np.array([[-1, 0, 0], [0, -1, 0], [0, 0, -1]])},
        "m": {
            "100": np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]]),
            "010": np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]]),
            "001": np.array([[1, 0, 0], [0, 1, 0], [0, 0, -1]]),
            "110": np.array([[0, -1, 0], [-1, 0, 0], [0, 0, 1]]),
            "011": np.array([[1, 0, 0], [0, 0, -1], [0, -1, 0]]),
            "101": np.array([[0, 0, -1], [0, 1, 0], [-1, 0, 0]]),
            "-101": np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]]),
            "-110": np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]]),
            "0-11": np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]]),
        },
    }


class Matrix:
    def __init__(self, arrs, trans, dirr):
        self.matrix = arrs
        self.trans = trans
        self.direction = dirr

    def __mul__(self, other):
        return self.matrix @ other.coor

    def __rmul__(self, other):
        return Matrix.__mul__(self, other)
