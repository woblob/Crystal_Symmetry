import numpy as np
import sympy as sp

import Matrix.matrices_new_extended as mne
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Mirror_xxz:

    def test_matrix_m_xxz(self):
        assert Point([y, x, z, 1]).is_got_by(mne._matrix_m_xxz)

    def test_matrix_n_mqxxz_qq0(self):
        assert Point([y, 1 + x, z, 1]).is_got_by(mne._matrix_n_mqxxz_qq0)

    def test_matrix_c_xxz_00h(self):
        assert Point([y, x, 1 + z, 1]).is_got_by(mne._matrix_c_xxz_00h)

    def test_matrix_n_qxxz_qq0(self):
        assert Point([1 + y, x, z, 1]).is_got_by(mne._matrix_n_qxxz_qq0)

    def test_matrix_n_xxz_hhh(self):
        assert Point([1 + y, 1 + x, 1 + z, 1]).is_got_by(mne._matrix_n_xxz_hhh)

    def test_matrix_d_xxz_qqq(self):
        assert Point([0.5 + y, 0.5 + x, 0.5 + z, 1]).is_got_by(mne._matrix_d_xxz_qqq)

    def test_matrix_d_xxz_3q3q3q(self):
        assert Point([0.5 + y, 0.5 + x, 1.5 + z, 1]).is_got_by(mne._matrix_d_xxz_3q3q3q)
