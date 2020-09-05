import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Mirror_xxz:

    def test_matrix_m_xxz(self):
        expected = Point([ y, x, z, 1])
        calculated = Point.calculate(mne._matrix_m_xxz)
        assert calculated == expected

    def test_matrix_n_mqxxz_qq0(self):
        expected = Point([ y, 1+x, z, 1])
        calculated = Point.calculate(mne._matrix_n_mqxxz_qq0)
        assert calculated == expected

    def test_matrix_c_xxz_00h(self):
        expected = Point([ y, x, 1+z, 1])
        calculated = Point.calculate(mne._matrix_c_xxz_00h)
        assert calculated == expected

    def test_matrix_n_qxxz_qq0(self):
        expected = Point([ 1+y, x, z, 1])
        calculated = Point.calculate(mne._matrix_n_qxxz_qq0)
        assert calculated == expected

    def test_matrix_n_xxz_hhh(self):
        expected = Point([ 1+y, 1+x, 1+z, 1])
        calculated = Point.calculate(mne._matrix_n_xxz_hhh)
        assert calculated == expected

    def test_matrix_d_xxz_qqq(self):
        expected = Point([ 0.5+y, 0.5+x, 0.5+z, 1])
        calculated = Point.calculate(mne._matrix_d_xxz_qqq)
        assert calculated == expected

    def test_matrix_d_xxz_3q3q3q(self):
        expected = Point([ 0.5+y, 0.5+x, 1.5+z, 1])
        calculated = Point.calculate(mne._matrix_d_xxz_3q3q3q)
        assert calculated == expected