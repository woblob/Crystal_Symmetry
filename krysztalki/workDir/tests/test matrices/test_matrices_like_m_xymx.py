# test_matrices_like_

import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Mirror_xymx:

    def test_matrix_m_xymx(self):
        expected = Point([ -z, y, -x, 1])
        calculated = Point.calculate(mne._matrix_m_xymx)
        assert calculated == expected

    def test_matrix_n_qxymx_mq0q(self):
        expected = Point([ -z, y, 1-x, 1])
        calculated = Point.calculate(mne._matrix_n_qxymx_mq0q)
        assert calculated == expected

    def test_matrix_b_xymx_0h0(self):
        expected = Point([ -z, 1+y, -x, 1])
        calculated = Point.calculate(mne._matrix_b_xymx_0h0)
        assert calculated == expected

    def test_matrix_n_qxymx_q0mq(self):
        expected = Point([ 1-z, y, -x, 1])
        calculated = Point.calculate(mne._matrix_n_qxymx_q0mq)
        assert calculated == expected

    def test_matrix_b_hxymx_0h0(self):
        expected = Point([ 1-z, 1+y, 1-x, 1])
        calculated = Point.calculate(mne._matrix_b_hxymx_0h0)
        assert calculated == expected

    def test_matrix_d_hxymx_mqqq(self):
        expected = Point([ 0.5-z, 0.5+y, 1.5-x, 1])
        calculated = Point.calculate(mne._matrix_d_hxymx_mqqq)
        assert calculated == expected

    def test_matrix_d_hxymx_q3qmq(self):
        expected = Point([ 1.5-z, 1.5+y, 0.5-x, 1])
        calculated = Point.calculate(mne._matrix_d_hxymx_q3qmq)
        assert calculated == expected
