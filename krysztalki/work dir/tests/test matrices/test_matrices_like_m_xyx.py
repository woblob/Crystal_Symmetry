import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Mirror_xyx:

    def test_matrix_m_xyx(self):
        expected = Point([ z, y, x, 1])
        calculated = Point.calculate(mne._matrix_m_xyx)
        assert calculated == expected

    def test_matrix_n_mqxyx_q0q(self):
        expected = Point([ z, y, 1+x, 1])
        calculated = Point.calculate(mne._matrix_n_mqxyx_q0q)
        assert calculated == expected

    def test_matrix_b_xyx_0h0(self):
        expected = Point([ z, 1+y, x, 1])
        calculated = Point.calculate(mne._matrix_b_xyx_0h0)
        assert calculated == expected

    def test_matrix_n_qxymx_q0q(self):
        expected = Point([ 1+z, y, x, 1])
        calculated = Point.calculate(mne._matrix_n_qxymx_q0q)
        assert calculated == expected

    def test_matrix_n_xyx_hhh(self):
        expected = Point([ 1+z, 1+y, 1+x, 1])
        calculated = Point.calculate(mne._matrix_n_xyx_hhh)
        assert calculated == expected

    def test_matrix_d_xyx_qqq(self):
        expected = Point([ 0.5+z, 0.5+y, 0.5+x, 1])
        calculated = Point.calculate(mne._matrix_d_xyx_qqq)
        assert calculated == expected

    def test_matrix_d_xyx_3q3q3q(self):
        expected = Point([ 1.5+z, 1.5+y, 1.5+x, 1])
        calculated = Point.calculate(mne._matrix_d_xyx_3q3q3q)
        assert calculated == expected