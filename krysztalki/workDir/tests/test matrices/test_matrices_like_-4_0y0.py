import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_m4_0y0:

    def test_matrix_m4_0y0(self):
        expected = Point([ -z, -y, x, 1])
        calculated = Point.calculate(mne._matrix_m4_0y0)
        assert calculated == expected

    def test_matrix_m4_qyq_q0q(self):
        expected = Point([ 1-z, -y, x, 1])
        calculated = Point.calculate(mne._matrix_m4_qyq_q0q)
        assert calculated == expected

    def test_matrix_m4_0y0_0q0(self):
        expected = Point([ -z, 1-y, x, 1])
        calculated = Point.calculate(mne._matrix_m4_0y0_0q0)
        assert calculated == expected

    def test_matrix_m4_mqyq_mq0q(self):
        expected = Point([ -z, -y, 1+x, 1])
        calculated = Point.calculate(mne._matrix_m4_mqyq_mq0q)
        assert calculated == expected

    def test_matrix_m4_0yh_0qh(self):
        expected = Point([ 1-z, 1-y, 1+x, 1])
        calculated = Point.calculate(mne._matrix_m4_0yh_0qh)
        assert calculated == expected

    def test_matrix_m4_qyh_qoh(self):
        expected = Point([ 1.5-z, 0.5-y, 0.5+x, 1])
        calculated = Point.calculate(mne._matrix_m4_qyh_qoh)
        assert calculated == expected

    def test_matrix_m4_mqyh_mq3oh(self):
        expected = Point([ 0.5-z, 1.5-y, 1.5+x, 1])
        calculated = Point.calculate(mne._matrix_m4_mqyh_mq3oh)
        assert calculated == expected
