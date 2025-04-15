import Matrix.matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Mirror_0yz:

    def test_matrix_m_0yz(self):
        assert Point([-x, y, z, 1]).is_got_by(mne._matrix_m_0yz)

    def test_matrix_c_0yz_00h(self):
        assert Point([-x, y, 1 + z, 1]).is_got_by(mne._matrix_c_0yz_00h)

    def test_matrix_b_qyz(self):
        assert Point([1 - x, 1 + y, z, 1]).is_got_by(mne._matrix_b_qyz_0h0)

    def test_matrix_d_oyz_0qq(self):
        assert Point([0.5 - x, 0.5 + y, 0.5 + z, 1]).is_got_by(mne._matrix_d_oyz_0qq)

    def test_matrix_d_3oyz_0qq(self):
        assert Point([1.5 - x, 0.5 + y, 0.5 + z, 1]).is_got_by(mne._matrix_d_3oyz_0qq)

    def test_matrix_d_oyz_03qq(self):
        assert Point([0.5 - x, 1.5 + y, 0.5 + z, 1]).is_got_by(mne._matrix_d_oyz_03qq)

    def test_matrix_d_oyz_0q3q(self):
        assert Point([0.5 - x, 0.5 + y, 1.5 + z, 1]).is_got_by(mne._matrix_d_oyz_0q3q)

    def test_matrix_d_oyz_03q3q(self):
        assert Point([0.5 - x, 1.5 + y, 1.5 + z, 1]).is_got_by(mne._matrix_d_oyz_03q3q)

    def test_matrix_d_3oyz_0q3q(self):
        assert Point([1.5 - x, 0.5 + y, 1.5 + z, 1]).is_got_by(mne._matrix_d_3oyz_0q3q)

    def test_matrix_d_3oyz_03qq(self):
        assert Point([1.5 - x, 1.5 + y, 0.5 + z, 1]).is_got_by(mne._matrix_d_3oyz_03qq)

    def test_matrix_d_3oyz_03q3q(self):
        assert Point([1.5 - x, 1.5 + y, 1.5 + z, 1]).is_got_by(mne._matrix_d_3oyz_03q3q)
