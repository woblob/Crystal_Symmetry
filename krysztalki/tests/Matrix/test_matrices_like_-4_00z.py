import numpy as np
import sympy as sp

import Crystal_Symmetry.krysztalki.workDir.Matrix.matrices_new_extended as mne
from Crystal_Symmetry.krysztalki.workDir.equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_m4_00z:

    def test_matrix_m4_00z(self):
        assert Point([y, -x, -z, 1]).is_got_by(mne._matrix_m4_00z)

    def test_matrix_m4_qmqz_qmq0(self):
        assert Point([1 + y, -x, -z, 1]).is_got_by(mne._matrix_m4_qmqz_qmq0)

    def test_matrix_m4_qqz_qq0(self):
        assert Point([y, 1 - x, -z, 1]).is_got_by(mne._matrix_m4_qqz_qq0)

    def test_matrix_m4_00z_00q(self):
        assert Point([y, -x, 1 - z, 1]).is_got_by(mne._matrix_m4_00z_00q)

    def test_matrix_m4_h0z_h0q(self):
        assert Point([1 + y, 1 - x, 1 - z, 1]).is_got_by(mne._matrix_m4_h0z_h0q)

    def test_matrix_m4_hqz_hqo(self):
        assert Point([0.5 + y, 1.5 - x, 0.5 - z, 1]).is_got_by(mne._matrix_m4_hqz_hqo)

    def test_matrix_m4_hmqz_hmq3o(self):
        assert Point([1.5 + y, 0.5 - x, 1.5 - z, 1]).is_got_by(
            mne._matrix_m4_hmqz_hmq3o
        )
