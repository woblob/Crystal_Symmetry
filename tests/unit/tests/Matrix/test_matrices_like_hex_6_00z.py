import Matrix.matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_hex_6_00z:

    def test_matrix_hex_6_00z(self):
        assert Point([x - y, x, z, 1]).is_got_by(mne._matrix_hex_6_00z)

    def test_matrix_hex_6_1_00z_00H(self):
        assert Point([x - y, x, 1 / 3 + z, 1]).is_got_by(mne._matrix_hex_6_1_00z_00H)

    def test_matrix_hex_6_2_00z_00t(self):
        assert Point([x - y, x, 2 / 3 + z, 1]).is_got_by(mne._matrix_hex_6_2_00z_00t)

    def test_matrix_hex_6_3_00z_00h(self):
        assert Point([x - y, x, 3 / 3 + z, 1]).is_got_by(mne._matrix_hex_6_3_00z_00h)

    def test_matrix_hex_6_4_00z_002t(self):
        assert Point([x - y, x, 4 / 3 + z, 1]).is_got_by(mne._matrix_hex_6_4_00z_002t)

    def test_matrix_hex_6_5_00z_005H(self):
        assert Point([x - y, x, 5 / 3 + z, 1]).is_got_by(mne._matrix_hex_6_5_00z_005H)
