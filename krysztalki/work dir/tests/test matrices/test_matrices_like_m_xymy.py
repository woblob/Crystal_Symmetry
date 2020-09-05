import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Mirror_xymy:

    def test_matrix_m_xymy(self):
        expected = Point([ x, -z, -y, 1])
        calculated = Point.calculate(mne._matrix_m_xymy)
        assert calculated == expected

    def test_matrix_n_xmqyy_0qq(self):
        expected = Point([x, -z, 1-y, 1])
        calculated = Point.calculate(mne._matrix_n_xmqyy_0qq)
        assert calculated == expected

    def test_matrix_n_xqymy_0qmq(self):
        expected = Point([x, 1-z, -y, 1])
        calculated = Point.calculate(mne._matrix_n_xqymy_0qmq)
        assert calculated == expected

    def test_matrix_a_xymy_h00(self):
        expected = Point([ 1+x, -z, -y, 1])
        calculated = Point.calculate(mne._matrix_a_xymy_h00)
        assert calculated == expected

    def test_matrix_a_xhymy_h00(self):
        expected = Point([1+x, 1-z, 1-y, 1])
        calculated = Point.calculate(mne._matrix_a_xhymy_h00)
        assert calculated == expected

    def test_matrix_d_xhymy_3qmqq(self):
        expected = Point([1.5+x, 0.5-z, 1.5-y, 1])
        calculated = Point.calculate(mne._matrix_d_xhymy_3qmqq)
        assert calculated == expected
