import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_hex_m_0yz:

    def test_matrix_hex_m_0yz(self):
        expected = Point([ -x, -x+y, z, 1])
        calculated = Point.calculate(mne._matrix_hex_m_0yz)
        assert calculated == expected

    def test_matrix_hex_c_0yz_00h(self):
        expected = Point([ -x, -x+y, 3/3+z, 1])
        calculated = Point.calculate(mne._matrix_hex_c_0yz_00h)
        assert calculated == expected
