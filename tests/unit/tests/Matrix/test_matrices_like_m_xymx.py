# test_matrices_like_

import numpy as np
import sympy as sp

import Matrix.matrices_new_extended as mne
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Mirror_xymx:

    def test_matrix_m_xymx(self):
        assert Point([-z, y, -x, 1]).is_got_by(mne._matrix_m_xymx)

    def test_matrix_n_qxymx_mq0q(self):
        assert Point([-z, y, 1 - x, 1]).is_got_by(mne._matrix_n_qxymx_mq0q)

    def test_matrix_b_xymx_0h0(self):
        assert Point([-z, 1 + y, -x, 1]).is_got_by(mne._matrix_b_xymx_0h0)

    def test_matrix_n_qxymx_q0mq(self):
        assert Point([1 - z, y, -x, 1]).is_got_by(mne._matrix_n_qxymx_q0mq)

    def test_matrix_b_hxymx_0h0(self):
        assert Point([1 - z, 1 + y, 1 - x, 1]).is_got_by(mne._matrix_b_hxymx_0h0)

    def test_matrix_d_hxymx_mqqq(self):
        assert Point([0.5 - z, 0.5 + y, 1.5 - x, 1]).is_got_by(mne._matrix_d_hxymx_mqqq)

    def test_matrix_d_hxymx_q3qmq(self):
        assert Point([1.5 - z, 1.5 + y, 0.5 - x, 1]).is_got_by(
            mne._matrix_d_hxymx_q3qmq
        )
