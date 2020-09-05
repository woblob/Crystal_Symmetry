import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_hex_m_x0z:

    def test_matrix_hex_m_x0z(self):
        expected = Point([ x-y, -y, z, 1])
        calculated = Point.calculate(mne._matrix_hex_m_x0z)
        assert calculated == expected

    def test_matrix_hex_c_x0z_00h(self):
        expected = Point([ x-y, -y, 3/3+z, 1])
        calculated = Point.calculate(mne._matrix_hex_c_x0z_00h)
        assert calculated == expected

