import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_inverse:

    def test_matrix_inv_000(self):
        expected = Point([ -x, -y, -z, 1])
        calculated = Point.calculate(mne._matrix_inv_000)
        assert calculated == expected

    def test_matrix_inv_0qq(self):
        expected = Point([ -x, 1-y, 1-z, 1])
        calculated = Point.calculate(mne._matrix_inv_0qq)
        assert calculated == expected

    def test_matrix_inv_q0q(self):
        expected = Point([ 1-x, -y, 1-z, 1])
        calculated = Point.calculate(mne._matrix_inv_q0q)
        assert calculated == expected

    def test_matrix_inv_qq0(self):
        expected = Point([ 1-x, 1-y, -z, 1])
        calculated = Point.calculate(mne._matrix_inv_qq0)
        assert calculated == expected

    def test_matrix_inv_qqq(self):
        expected = Point([ 1-x, 1-y, 1-z, 1])
        calculated = Point.calculate(mne._matrix_inv_qqq)
        assert calculated == expected

    def test_matrix_inv_ooo(self):
        expected = Point([ 0.5-x, 0.5-y, 0.5-z, 1])
        calculated = Point.calculate(mne._matrix_inv_ooo)
        assert calculated == expected

    def test_matrix_inv_3ooo(self):
        expected = Point([ 1.5-x, 0.5-y, 0.5-z, 1])
        calculated = Point.calculate(mne._matrix_inv_3ooo)
        assert calculated == expected

    def test_matrix_inv_o3oo(self):
        expected = Point([ 0.5-x, 1.5-y, 0.5-z, 1])
        calculated = Point.calculate(mne._matrix_inv_o3oo)
        assert calculated == expected

    def test_matrix_inv_oo3o(self):
        expected = Point([ 0.5-x, 0.5-y, 1.5-z, 1])
        calculated = Point.calculate(mne._matrix_inv_oo3o)
        assert calculated == expected

    def test_matrix_inv_o3o3o(self):
        expected = Point([ 0.5-x, 1.5-y, 1.5-z, 1])
        calculated = Point.calculate(mne._matrix_inv_o3o3o)
        assert calculated == expected

    def test_matrix_inv_3oo3o(self):
        expected = Point([ 1.5-x, 0.5-y, 1.5-z, 1])
        calculated = Point.calculate(mne._matrix_inv_3oo3o)
        assert calculated == expected

    def test_matrix_inv_3o3oo(self):
        expected = Point([ 1.5-x, 1.5-y, 0.5-z, 1])
        calculated = Point.calculate(mne._matrix_inv_3o3oo)
        assert calculated == expected

    def test_matrix_inv_3o3o3o(self):
        expected = Point([ 1.5-x, 1.5-y, 1.5-z, 1])
        calculated = Point.calculate(mne._matrix_inv_3o3o3o)
        assert calculated == expected
