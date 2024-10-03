import numpy as np
import sympy as sp

import Matrix.matrices_new_extended as mne
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_4_00z:

    def test_matrix_4_00z(self):
        assert Point([-y, x, z, 1]).is_got_by(mne._matrix_4_00z)

    def test_matrix_4_qqz(self):
        assert Point([1 - y, x, z, 1]).is_got_by(mne._matrix_4_qqz)

    def test_matrix_4_mqqz(self):
        assert Point([-y, 1 + x, z, 1]).is_got_by(mne._matrix_4_mqqz)

    def test_matrix_4_2_00z_00h(self):
        assert Point([-y, x, 1 + z, 1]).is_got_by(mne._matrix_4_2_00z_00h)

    def test_matrix_4_2_0hz_00h(self):
        assert Point([1 - y, 1 + x, 1 + z, 1]).is_got_by(mne._matrix_4_2_0hz_00h)

    def test_matrix_4_1_0qz_00q(self):
        assert Point([0.5 - y, 0.5 + x, 0.5 + z, 1]).is_got_by(mne._matrix_4_1_0qz_00q)

    def test_matrix_4_1_mqhz_00q(self):
        assert Point([0.5 - y, 1.5 + x, 0.5 + z, 1]).is_got_by(mne._matrix_4_1_mqhz_00q)

    def test_matrix_4_3_mqhz_003q(self):
        assert Point([0.5 - y, 1.5 + x, 1.5 + z, 1]).is_got_by(
            mne._matrix_4_3_mqhz_003q
        )

    def test_matrix_4_3_qhz_003q(self):
        assert Point([1.5 - y, 0.5 + x, 1.5 + z, 1]).is_got_by(mne._matrix_4_3_qhz_003q)

    def test_matrix_4_1_03qz_00q(self):
        assert Point([1.5 - y, 1.5 + x, 0.5 + z, 1]).is_got_by(mne._matrix_4_1_03qz_00q)
