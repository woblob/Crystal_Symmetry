import Matrix.matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Mirror_xymy:

    def test_matrix_m_xymy(self):
        assert Point([x, -z, -y, 1]).is_got_by(mne._matrix_m_xymy)

    def test_matrix_n_xmqyy_0qq(self):
        assert Point([x, -z, 1 - y, 1]).is_got_by(mne._matrix_n_xmqyy_0qq)

    def test_matrix_n_xqymy_0qmq(self):
        assert Point([x, 1 - z, -y, 1]).is_got_by(mne._matrix_n_xqymy_0qmq)

    def test_matrix_a_xymy_h00(self):
        assert Point([1 + x, -z, -y, 1]).is_got_by(mne._matrix_a_xymy_h00)

    def test_matrix_a_xhymy_h00(self):
        assert Point([1 + x, 1 - z, 1 - y, 1]).is_got_by(mne._matrix_a_xhymy_h00)

    def test_matrix_d_xhymy_3qmqq(self):
        assert Point([1.5 + x, 0.5 - z, 1.5 - y, 1]).is_got_by(
            mne._matrix_d_xhymy_3qmqq
        )
