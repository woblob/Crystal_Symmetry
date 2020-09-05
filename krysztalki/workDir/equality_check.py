import numpy as np
import sympy as sp


class Point:
    base_point = None

    def __init__(self, arr):
        self.array = np.array(arr)

    @classmethod
    def calculate(cls, matrix):
        calculated_point = (matrix @ cls.base_point.T).T
        return cls(calculated_point)

    def __eq__(self, other):
        equality = sp.simplify(other.array - self.array)
        return not np.any(equality)

    def __repr__(self):
        point_str = ", ".join(str(el) for el in self.array)
        return point_str
