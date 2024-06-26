import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_hex_2_2xx0:

    def test_matrix_hex_2_2xx0(self):
        expected = Point([ x, x-y, -z, 1])
        calculated = Point.calculate(mne._matrix_hex_2_2xx0)
        assert calculated == expected

    def test_matrix_hex_2_2xxq(self):
        expected = Point([ x, x-y, 3/3-z, 1])
        calculated = Point.calculate(mne._matrix_hex_2_2xxq)
        assert calculated == expected

    def test_matrix_2_2xxv(self):
        expected = Point([ x, x-y, 1/3-z, 1])
        calculated = Point.calculate(mne._matrix_hex_2_2xxv)
        assert calculated == expected
