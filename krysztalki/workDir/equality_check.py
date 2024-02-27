from __future__ import annotations

import numpy as np
import sympy as sp


class Point:
    base_point = None

    def __init__(self, arr: list[np.ndarray[(1, 4), np.dtype[float]]]):
        self.array = np.array(arr)

    @classmethod
    def calculate(cls, matrix: np.ndarray[(4, 4), np.dtype[float]]):
        calculated_point = (matrix @ cls.base_point.T).T
        return cls(calculated_point)

    def __eq__(self, other: Point):
        equality = sp.simplify(other.array - self.array)
        return not np.any(equality)

    def __repr__(self):
        point_str = ", ".join(str(el) for el in self.array)
        return point_str
