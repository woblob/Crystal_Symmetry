import Matrix.matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_hex_3_00z:

    def test_matrix_hex_3_00z(self):
        assert Point([-y, x - y, z, 1]).is_got_by(mne._matrix_hex_3_00z)

    def test_matrix_hex_3_1_00z_00t(self):
        assert Point([-y, x - y, 2 / 3 + z, 1]).is_got_by(mne._matrix_hex_3_1_00z_00t)

    def test_matrix_hex_3_2_00z_002t(self):
        assert Point([-y, x - y, 4 / 3 + z, 1]).is_got_by(mne._matrix_hex_3_2_00z_002t)
