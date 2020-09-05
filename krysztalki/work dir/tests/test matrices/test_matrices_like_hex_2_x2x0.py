import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_hex_2_x2x0:

    def test_matrix_hex_2_x2x0(self):
        expected = Point([ -x+y, y, -z, 1])
        calculated = Point.calculate(mne._matrix_hex_2_x2x0)
        assert calculated == expected

    def test_matrix_hex_2_x2xH(self):
        expected = Point([ -x+y, y, 2/3-z, 1])
        calculated = Point.calculate(mne._matrix_hex_2_x2xH)
        assert calculated == expected

    def test_matrix_hex_2_x2xq(self):
        expected = Point([ -x+y, y, 3/3-z, 1])
        calculated = Point.calculate(mne._matrix_hex_2_x2xq)
        assert calculated == expected

    def test_matrix_hex_2_x2xt(self):
        expected = Point([ -x+y, y, 4/3-z, 1])
        calculated = Point.calculate(mne._matrix_hex_2_x2xt)
        assert calculated == expected
