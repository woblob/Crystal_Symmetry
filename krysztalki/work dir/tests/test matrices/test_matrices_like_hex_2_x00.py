import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_hex_2_x00:

    def test_matrix_hex_2_x00(self):
        expected = Point([ x-y, -y, -z, 1])
        calculated = Point.calculate(mne._matrix_hex_2_x00)
        assert calculated == expected

    def test_matrix_hex_2_x0H(self):
        expected = Point([ x-y, -y, 2/3-z, 1])
        calculated = Point.calculate(mne._matrix_hex_2_x0H)
        assert calculated == expected

    def test_matrix_hex_2_x0q(self):
        expected = Point([ x-y, -y, 3/3-z, 1])
        calculated = Point.calculate(mne._matrix_hex_2_x0q)
        assert calculated == expected

    def test_matrix_hex_2_x0t(self):
        expected = Point([ x-y, -y, 4/3-z, 1])
        calculated = Point.calculate(mne._matrix_hex_2_x0t)
        assert calculated == expected
