import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Mirror_xyy:

    def test_matrix_m_xyy(self):
        expected = Point([ x, z, y, 1])
        calculated = Point.calculate(mne._matrix_m_xyy)
        assert calculated == expected

    def test_matrix_n_xqymy_0mqq(self):
        expected = Point([x, z, 1+y, 1])
        calculated = Point.calculate(mne._matrix_n_xqymy_0mqq)
        assert calculated == expected

    def test_matrix_n_xqyy_0qq(self):
        expected = Point([x, 1+z, y, 1])
        calculated = Point.calculate(mne._matrix_n_xqyy_0qq)
        assert calculated == expected

    def test_matrix_a_xyy_h00(self):
        expected = Point([1+x, z, y, 1])
        calculated = Point.calculate(mne._matrix_a_xyy_h00)
        assert calculated == expected

    def test_matrix_n_xyy_hhh(self):
        expected = Point([1+x, 1+z, 1+y, 1])
        calculated = Point.calculate(mne._matrix_n_xyy_hhh)
        assert calculated == expected

    def test_matrix_d_xyy_qqq(self):
        expected = Point([0.5+x, 0.5+z, 0.5+y, 1])
        calculated = Point.calculate(mne._matrix_d_xyy_qqq)
        assert calculated == expected

    def test_matrix_d_xhymy_qqmq(self):
        expected = Point([ 0.5+x, 1.5+z, 0.5+y, 1])
        calculated = Point.calculate(mne._matrix_d_xhymy_qqmq)
        assert calculated == expected

    def test_matrix_d_xyy_3q3q3q(self):
        expected = Point([ 1.5+x, 1.5+z, 1.5+y, 1])
        calculated = Point.calculate(mne._matrix_d_xyy_3q3q3q)
        assert calculated == expected


