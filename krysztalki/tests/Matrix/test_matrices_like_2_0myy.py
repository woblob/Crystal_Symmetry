import numpy as np
import sympy as sp

import Crystal_Symmetry.krysztalki.workDir.Matrix.matrices_new_extended as mne
from Crystal_Symmetry.krysztalki.workDir.equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_2_0myy:

    def test_matrix_2_0myy(self):
        assert Point([-x, -z, -y, 1]).is_got_by(mne._matrix_2_0myy)

    def test_matrix_2_qmyy(self):
        assert Point([1 - x, -z, -y, 1]).is_got_by(mne._matrix_2_qmyy)

    def test_matrix_2_1_0qmyy_0qmq(self):
        assert Point([-x, 1 - z, -y, 1]).is_got_by(mne._matrix_2_1_0qmyy_0qmq)

    def test_matrix_2_0qmyy_0mqq(self):
        assert Point([-x, -z, 1 - y, 1]).is_got_by(mne._matrix_2_0qmyy_0mqq)

    def test_matrix_2_qhmyy(self):
        assert Point([1 - x, 1 - z, 1 - y, 1]).is_got_by(mne._matrix_2_qhmyy)

    def test_matrix_2_oqmyy(self):
        assert Point([0.5 - x, 0.5 - z, 0.5 - y, 1]).is_got_by(mne._matrix_2_oqmyy)

    def test_matrix_2_o3qmyy(self):
        assert Point([0.5 - x, 1.5 - z, 1.5 - y, 1]).is_got_by(mne._matrix_2_o3qmyy)

    def test_matrix_2_1_3ohmyy_0qmq(self):
        assert Point([1.5 - x, 1.5 - z, 0.5 - y, 1]).is_got_by(
            mne._matrix_2_1_3ohmyy_0qmq
        )

    def test_matrix_2_3o3qmyy(self):
        assert Point([1.5 - x, 1.5 - z, 1.5 - y, 1]).is_got_by(mne._matrix_2_3o3qmyy)

    # def test_matrix_2_0myy_h0h_out(self):
    #     assert Point([1.5 - x, 0.5 - z, 1.5 - y, 1]).is_got_by(mne._matrix_2_myy)
