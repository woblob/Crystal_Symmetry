import Matrix.matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_4_x00:

    def test_matrix_4_x00(self):
        assert Point([x, -z, y, 1]).is_got_by(mne._matrix_4_x00)

    def test_matrix_4_2_x00_h00(self):
        assert Point([1 + x, -z, y, 1]).is_got_by(mne._matrix_4_2_x00_h00)

    def test_matrix_4_xqq(self):
        assert Point([x, 1 - z, y, 1]).is_got_by(mne._matrix_4_xqq)

    def test_matrix_4_xmqq(self):
        assert Point([x, -z, 1 + y, 1]).is_got_by(mne._matrix_4_xmqq)

    def test_matrix_4_2_x0h_h00(self):
        assert Point([1 + x, 1 - z, 1 + y, 1]).is_got_by(mne._matrix_4_2_x0h_h00)

    def test_matrix_4_1_x0q_q00(self):
        assert Point([0.5 + x, 0.5 - z, 0.5 + y, 1]).is_got_by(mne._matrix_4_1_x0q_q00)

    def test_matrix_4_1_xmqh_q00(self):
        assert Point([0.5 + x, 0.5 - z, 1.5 + y, 1]).is_got_by(mne._matrix_4_1_xmqh_q00)

    def test_matrix_4_1_x03q_q00(self):
        assert Point([0.5 + x, 1.5 - z, 1.5 + y, 1]).is_got_by(mne._matrix_4_1_x03q_q00)

    def test_matrix_4_3_xmqh_3q00(self):
        assert Point([1.5 + x, 0.5 - z, 1.5 + y, 1]).is_got_by(
            mne._matrix_4_3_xmqh_3q00
        )

    def test_matrix_4_3_xqh_3q00(self):
        assert Point([1.5 + x, 1.5 - z, 0.5 + y, 1]).is_got_by(mne._matrix_4_3_xqh_3q00)
