import numpy as np
import sympy as sp

import Matrix.matrices_new_extended as mne
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_2_mx0x:

    def test_matrix_2_mx0x(self):
        assert Point([-z, -y, -x, 1]).is_got_by(mne._matrix_2_mx0x)

    def test_matrix_2_1_qmx0x_mq0q(self):
        assert Point([-z, -y, 1 - x, 1]).is_got_by(mne._matrix_2_1_qmx0x_mq0q)

    def test_matrix_2_mxqx(self):
        assert Point([-z, 1 - y, -x, 1]).is_got_by(mne._matrix_2_mxqx)

    def test_matrix_2_1_qmx0x_q0mq(self):
        assert Point([1 - z, -y, -x, 1]).is_got_by(mne._matrix_2_1_qmx0x_q0mq)

    def test_matrix_2_hmxqx(self):
        assert Point([1 - z, 1 - y, 1 - x, 1]).is_got_by(mne._matrix_2_hmxqx)

    def test_matrix_2_qmxox(self):
        assert Point([0.5 - z, 0.5 - y, 0.5 - x, 1]).is_got_by(mne._matrix_2_qmxox)

    def test_matrix_2_3qmx3ox(self):
        assert Point([1.5 - z, 1.5 - y, 1.5 - x, 1]).is_got_by(mne._matrix_2_3qmx3ox)

    def test_matrix_2_1_hmx3ox_mq0q(self):
        assert Point([0.5 - z, 1.5 - y, 1.5 - x, 1]).is_got_by(
            mne._matrix_2_1_hmx3ox_mq0q
        )

    def test_matrix_2_3qmx3ox_dwa(self):
        assert Point([1.5 - z, 0.5 - y, 1.5 - x, 1]).is_got_by(mne._matrix_2_3qmxox)

    def test_matrix_2_1_hmx3ox_q0mq(self):
        assert Point([1.5 - z, 1.5 - y, 0.5 - x, 1]).is_got_by(
            mne._matrix_2_1_hmx3ox_q0mq
        )
