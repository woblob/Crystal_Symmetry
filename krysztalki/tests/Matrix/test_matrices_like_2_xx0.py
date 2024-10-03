import numpy as np
import sympy as sp

import Matrix.matrices_new_extended as mne
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_2_xx0:

    def test_matrix_2_xx0(self):
        assert Point([y, x, -z, 1]).is_got_by(mne._matrix_2_xx0)

    def test_matrix_2_xxq(self):
        assert Point([y, x, 1 - z, 1]).is_got_by(mne._matrix_2_xxq)

    def test_matrix_2_1_xqx0_qq0(self):
        assert Point([y, 1 + x, -z, 1]).is_got_by(mne._matrix_2_1_xqx0_qq0)

    def test_matrix_2_1_xmqx0_qq0(self):
        assert Point([1 + y, x, -z, 1]).is_got_by(mne._matrix_2_1_xmqx0_qq0)

    def test_matrix_2_1_xxq_hh0(self):
        assert Point([1 + y, 1 + x, 1 - z, 1]).is_got_by(mne._matrix_2_1_xxq_hh0)

    def test_matrix_2_1_xmqxo_hh0(self):
        assert Point([1.5 + y, 0.5 + x, 0.5 - z, 1]).is_got_by(
            mne._matrix_2_1_xmqxo_hh0
        )

    def test_matrix_2_1_xqx3o_hh0(self):
        assert Point([0.5 + y, 1.5 + x, 1.5 - z, 1]).is_got_by(
            mne._matrix_2_1_xqx3o_hh0
        )

    def test_matrix_2_1_xxo_qq0(self):
        assert Point([0.5 + y, 0.5 + x, 0.5 - z, 1]).is_got_by(mne._matrix_2_1_xxo_qq0)

    def test_matrix_2_1_xmqx3o_hh0(self):
        assert Point([1.5 + y, 0.5 + x, 1.5 - z, 1]).is_got_by(
            mne._matrix_2_1_xmqx3o_hh0
        )

    def test_matrix_2_1_xxo_3q3qo(self):
        assert Point([1.5 + y, 1.5 + x, 0.5 - z, 1]).is_got_by(
            mne._matrix_2_1_xxo_3q3qo
        )
