import Matrix.matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_inverse:

    def test_matrix_inv_000(self):
        assert Point([-x, -y, -z, 1]).is_got_by(mne._matrix_inv_000)

    def test_matrix_inv_0qq(self):
        assert Point([-x, 1 - y, 1 - z, 1]).is_got_by(mne._matrix_inv_0qq)

    def test_matrix_inv_q0q(self):
        assert Point([1 - x, -y, 1 - z, 1]).is_got_by(mne._matrix_inv_q0q)

    def test_matrix_inv_qq0(self):
        assert Point([1 - x, 1 - y, -z, 1]).is_got_by(mne._matrix_inv_qq0)

    def test_matrix_inv_qqq(self):
        assert Point([1 - x, 1 - y, 1 - z, 1]).is_got_by(mne._matrix_inv_qqq)

    def test_matrix_inv_ooo(self):
        assert Point([0.5 - x, 0.5 - y, 0.5 - z, 1]).is_got_by(mne._matrix_inv_ooo)

    def test_matrix_inv_3ooo(self):
        assert Point([1.5 - x, 0.5 - y, 0.5 - z, 1]).is_got_by(mne._matrix_inv_3ooo)

    def test_matrix_inv_o3oo(self):
        assert Point([0.5 - x, 1.5 - y, 0.5 - z, 1]).is_got_by(mne._matrix_inv_o3oo)

    def test_matrix_inv_oo3o(self):
        assert Point([0.5 - x, 0.5 - y, 1.5 - z, 1]).is_got_by(mne._matrix_inv_oo3o)

    def test_matrix_inv_o3o3o(self):
        assert Point([0.5 - x, 1.5 - y, 1.5 - z, 1]).is_got_by(mne._matrix_inv_o3o3o)

    def test_matrix_inv_3oo3o(self):
        assert Point([1.5 - x, 0.5 - y, 1.5 - z, 1]).is_got_by(mne._matrix_inv_3oo3o)

    def test_matrix_inv_3o3oo(self):
        assert Point([1.5 - x, 1.5 - y, 0.5 - z, 1]).is_got_by(mne._matrix_inv_3o3oo)

    def test_matrix_inv_3o3o3o(self):
        assert Point([1.5 - x, 1.5 - y, 1.5 - z, 1]).is_got_by(mne._matrix_inv_3o3o3o)
