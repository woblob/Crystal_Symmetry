import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_2_0yy:

    def test_matrix_2_0yy(self):
        expected = Point([ -x, z, y, 1])
        calculated = Point.calculate(mne._matrix_2_0yy)
        assert calculated == expected

    def test_matrix_2_qyy(self):
        expected = Point([ 1-x, z, y, 1])
        calculated = Point.calculate(mne._matrix_2_qyy)
        assert calculated == expected

    def test_matrix_2_1_0qyy_0qq(self):
        expected = Point([ -x, 1+z, y, 1])
        calculated = Point.calculate(mne._matrix_2_1_0qyy_0qq)
        assert calculated == expected

    def test_matrix_2_0qyy_0qq(self):
        expected = Point([ -x, z, 1+y, 1])
        calculated = Point.calculate(mne._matrix_2_0qyy_0qq)
        assert calculated == expected

    def test_matrix_2_1_qyy_0hh(self):
        expected = Point([ 1-x, 1+z, 1+y, 1])
        calculated = Point.calculate(mne._matrix_2_1_qyy_0hh)
        assert calculated == expected

    def test_matrix_2_1_3omqyy_0hh(self):
        expected = Point([ 1.5-x, 0.5+z, 1.5+y, 1])
        calculated = Point.calculate(mne._matrix_2_1_3omqyy_0hh)
        assert calculated == expected

    def test_matrix_2_1_oqyy_0hh(self):
        expected = Point([ 0.5-x, 1.5+z, 0.5+y, 1])
        calculated = Point.calculate(mne._matrix_2_1_oqyy_0hh)
        assert calculated == expected

    def test_matrix_2_1_oyy_0qq(self):
        expected = Point([ 0.5-x, 0.5+z, 0.5+y, 1])
        calculated = Point.calculate(mne._matrix_2_1_oyy_0qq)
        assert calculated == expected

    def test_matrix_2_1_oyy_03q3q(self):
        expected = Point([ 0.5-x, 1.5+z, 1.5+y, 1])
        calculated = Point.calculate(mne._matrix_2_1_oyy_03q3q)
        assert calculated == expected

    def test_matrix_2_1_3ohmyy_0mqq(self):
        expected = Point([ 1.5-x, 0.5+z, 1.5+y, 1])
        calculated = Point.calculate(mne._matrix_2_1_3ohmyy_0mqq)
        assert calculated == expected

    def test_matrix_2_1_3oqyy_0hh(self):
        expected = Point([ 1.5-x, 1.5+z, 0.5+y, 1])
        calculated = Point.calculate(mne._matrix_2_1_3oqyy_0hh)
        assert calculated == expected
