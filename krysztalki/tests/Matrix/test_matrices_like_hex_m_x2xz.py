import Matrix.matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_hex_m_x2xz:

    def test_matrix_hex_m_x2xz(self):
        assert Point([-x + y, y, z, 1]).is_got_by(mne._matrix_hex_m_x2xz)

    def test_matrix_hex_c_x2xz_00h(self):
        assert Point([-x + y, y, 3 / 3 + z, 1]).is_got_by(mne._matrix_hex_c_x2xz_00h)
