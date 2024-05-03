import numpy as np
import sympy as sp

import Crystal_Symmetry.krysztalki.workDir.Matrix.matrices_new_extended as mne
from Crystal_Symmetry.krysztalki.workDir.equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Mirror_xyy:

    def test_matrix_m_xyy(self):
        assert Point([x, z, y, 1]).is_got_by(mne._matrix_m_xyy)

    def test_matrix_n_xqymy_0mqq(self):
        assert Point([x, z, 1 + y, 1]).is_got_by(mne._matrix_n_xqymy_0mqq)

    def test_matrix_n_xqyy_0qq(self):
        assert Point([x, 1 + z, y, 1]).is_got_by(mne._matrix_n_xqyy_0qq)

    def test_matrix_a_xyy_h00(self):
        assert Point([1 + x, z, y, 1]).is_got_by(mne._matrix_a_xyy_h00)

    def test_matrix_n_xyy_hhh(self):
        assert Point([1 + x, 1 + z, 1 + y, 1]).is_got_by(mne._matrix_n_xyy_hhh)

    def test_matrix_d_xyy_qqq(self):
        assert Point([0.5 + x, 0.5 + z, 0.5 + y, 1]).is_got_by(mne._matrix_d_xyy_qqq)

    def test_matrix_d_xhymy_qqmq(self):
        assert Point([0.5 + x, 1.5 + z, 0.5 + y, 1]).is_got_by(mne._matrix_d_xhymy_qqmq)

    def test_matrix_d_xyy_3q3q3q(self):
        assert Point([1.5 + x, 1.5 + z, 1.5 + y, 1]).is_got_by(mne._matrix_d_xyy_3q3q3q)
