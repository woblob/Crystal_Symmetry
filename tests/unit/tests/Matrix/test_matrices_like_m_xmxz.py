import Matrix.matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Mirror_xmxz:

    def test_matrix_m_xmxz(self):
        assert Point([-y, -x, z, 1]).is_got_by(mne._matrix_m_xmxz)

    def test_matrix_c_xmxz_00h(self):
        assert Point([-y, -x, 1 + z, 1]).is_got_by(mne._matrix_c_xmxz_00h)

    def test_matrix_n_qxmxz_mqq0(self):
        assert Point([-y, 1 - x, z, 1]).is_got_by(mne._matrix_n_qxmxz_mqq0)

    def test_matrix_n_qxmxz_qmq0(self):
        assert Point([1 - y, -x, z, 1]).is_got_by(mne._matrix_n_qxmxz_qmq0)

    def test_matrix_c_hxmxz_00h(self):
        assert Point([1 - y, 1 - x, 1 + z, 1]).is_got_by(mne._matrix_c_hxmxz_00h)

    def test_matrix_d_hxmxz_qmqq(self):
        assert Point([1.5 - y, 0.5 - x, 0.5 + z, 1]).is_got_by(mne._matrix_d_hxmxz_qmqq)

    def test_matrix_d_hxmxz_mqq3q(self):
        assert Point([0.5 - y, 1.5 - x, 1.5 + z, 1]).is_got_by(
            mne._matrix_d_hxmxz_mqq3q
        )
