import numpy as np
import sympy as sp

import Crystal_Symmetry.krysztalki.workDir.Matrix.matrices_new_extended as mne
from Crystal_Symmetry.krysztalki.workDir.equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Mirror_xyx:

    def test_matrix_m_xyx(self):
        assert Point([z, y, x, 1]).is_got_by(mne._matrix_m_xyx)

    def test_matrix_n_mqxyx_q0q(self):
        assert Point([z, y, 1 + x, 1]).is_got_by(mne._matrix_n_mqxyx_q0q)

    def test_matrix_b_xyx_0h0(self):
        assert Point([z, 1 + y, x, 1]).is_got_by(mne._matrix_b_xyx_0h0)

    def test_matrix_n_qxymx_q0q(self):
        assert Point([1 + z, y, x, 1]).is_got_by(mne._matrix_n_qxymx_q0q)

    def test_matrix_n_xyx_hhh(self):
        assert Point([1 + z, 1 + y, 1 + x, 1]).is_got_by(mne._matrix_n_xyx_hhh)

    def test_matrix_d_xyx_qqq(self):
        assert Point([0.5 + z, 0.5 + y, 0.5 + x, 1]).is_got_by(mne._matrix_d_xyx_qqq)

    def test_matrix_d_xyx_3q3q3q(self):
        assert Point([1.5 + z, 1.5 + y, 1.5 + x, 1]).is_got_by(mne._matrix_d_xyx_3q3q3q)
