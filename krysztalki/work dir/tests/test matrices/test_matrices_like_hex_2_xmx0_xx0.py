import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_hex_2_xmx0_xx0:

    def test_matrix_hex_2_xxH(self):
        expected = Point([ y, x, 2/3-z, 1])
        calculated = Point.calculate(mne._matrix_hex_2_xxH)
        assert calculated == expected

    def test_matrix_hex_2_xmxH(self):
        expected = Point([ -y, -x, 2/3-z, 1])
        calculated = Point.calculate(mne._matrix_hex_2_xmxH)
        assert calculated == expected

    def test_matrix_hex_2_xmxt(self):
        expected = Point([ -y, -x, 4/3-z, 1])
        calculated = Point.calculate(mne._matrix_hex_2_xmxt)
        assert calculated == expected

    def test_matrix_hex_2_xmx5v(self):
        expected = Point([ -y, -x, 5/3-z, 1])
        calculated = Point.calculate(mne._matrix_hex_2_xmx5v)
        assert calculated == expected
