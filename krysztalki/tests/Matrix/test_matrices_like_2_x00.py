import numpy as np
import sympy as sp

import Crystal_Symmetry.krysztalki.workDir.Matrix.matrices_new_extended as mne
from Crystal_Symmetry.krysztalki.workDir.equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_2_x00:

    def test_matrix_2_x00(self):
        assert Point([x, -y, -z, 1]).is_got_by(mne._matrix_2_x00)

    def test_matrix_2_xqq(self):
        assert Point([x, 1 - y, 1 - z, 1]).is_got_by(mne._matrix_2_xqq)

    def test_matrix_2_1_x0q_h00(self):
        assert Point([1 + x, -y, 1 - z, 1]).is_got_by(mne._matrix_2_1_x0q_h00)

    def test_matrix_2_1_xq0_h00(self):
        assert Point([1 + x, 1 - y, -z, 1]).is_got_by(mne._matrix_2_1_xq0_h00)

    def test_matrix_2_1_xqq_h00(self):
        assert Point([1 + x, 1 - y, 1 - z, 1]).is_got_by(mne._matrix_2_1_xqq_h00)

    def test_matrix_2_x0q(self):
        assert Point([x, -y, 1 - z, 1]).is_got_by(mne._matrix_2_x0q)
