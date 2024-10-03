import Matrix.matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_2_x0x:

    def test_matrix_2_x0x(self):
        assert Point([z, -y, x, 1]).is_got_by(mne._matrix_2_x0x)

    def test_matrix_2_1_mqx0x_q0q(self):
        assert Point([z, -y, 1 + x, 1]).is_got_by(mne._matrix_2_1_mqx0x_q0q)

    def test_matrix_2_xqx(self):
        assert Point([z, 1 - y, x, 1]).is_got_by(mne._matrix_2_xqx)

    def test_matrix_2_1_qx0x_q0mq(self):
        assert Point([1 + z, -y, x, 1]).is_got_by(mne._matrix_2_1_qx0x_q0mq)

    def test_matrix_2_1_xqx_q0q(self):
        assert Point([1 + z, 1 - y, 1 + x, 1]).is_got_by(mne._matrix_2_1_xqx_q0q)

    def test_matrix_2_1_qx3ox_h0h(self):
        assert Point([1.5 + z, 1.5 - y, 0.5 + x, 1]).is_got_by(
            mne._matrix_2_1_qx3ox_h0h
        )

    def test_matrix_2_1_mqxox_h0h(self):
        assert Point([0.5 + z, 0.5 - y, 1.5 + x, 1]).is_got_by(
            mne._matrix_2_1_mqxox_h0h
        )

    def test_matrix_2_1_xox_q0q(self):
        assert Point([0.5 + z, 0.5 - y, 0.5 + x, 1]).is_got_by(mne._matrix_2_1_xox_q0q)

    def test_matrix_2_1_mqx3ox_h0h(self):
        assert Point([0.5 + z, 1.5 - y, 1.5 + x, 1]).is_got_by(
            mne._matrix_2_1_mqx3ox_h0h
        )

    def test_matrix_2_1_xox_3q03q(self):
        assert Point([1.5 + z, 0.5 - y, 1.5 + x, 1]).is_got_by(
            mne._matrix_2_1_xox_3q03q
        )
