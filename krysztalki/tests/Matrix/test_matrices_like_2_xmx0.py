import numpy as np
import sympy as sp

import Matrix.matrices_new_extended as mne
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_2_xmx0:

    def test_matrix_2_xmx0(self):
        assert Point([-y, -x, -z, 1]).is_got_by(mne._matrix_2_xmx0)

    def test_matrix_2_xmxq(self):
        assert Point([-y, -x, 1 - z, 1]).is_got_by(mne._matrix_2_xmxq)

    def test_matrix_2_1_xqmx0_mqq0(self):
        assert Point([-y, 1 - x, -z, 1]).is_got_by(mne._matrix_2_1_xqmx0_mqq0)

    def test_matrix_2_1_xqmx0_qmq0(self):
        assert Point([1 - y, -x, -z, 1]).is_got_by(mne._matrix_2_1_xqmx0_qmq0)

    def test_matrix_2_xhmxq(self):
        assert Point([1 - y, 1 - x, 1 - z, 1]).is_got_by(mne._matrix_2_xhmxq)

    def test_matrix_2_xqmxo(self):
        assert Point([0.5 - y, 0.5 - x, 0.5 - z, 1]).is_got_by(mne._matrix_2_xqmxo)

    def test_matrix_2_1_xhmx3o_mqq0(self):
        assert Point([0.5 - y, 1.5 - x, 1.5 - z, 1]).is_got_by(
            mne._matrix_2_1_xhmx3o_mqq0
        )

    def test_matrix_2_1_xhmx3o_qmq0(self):
        assert Point([1.5 - y, 0.5 - x, 1.5 - z, 1]).is_got_by(
            mne._matrix_2_1_xhmx3o_qmq0
        )

    def test_matrix_2_x3qmxo(self):
        assert Point([1.5 - y, 1.5 - x, 0.5 - z, 1]).is_got_by(mne._matrix_2_x3qmxo)

    def test_matrix_2_x3qmx3o(self):
        assert Point([1.5 - y, 1.5 - x, 1.5 - z, 1]).is_got_by(mne._matrix_2_x3qmx3o)
