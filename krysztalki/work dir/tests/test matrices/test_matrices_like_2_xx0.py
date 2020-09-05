import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_2_xx0:

    def test_matrix_2_xx0(self):
        expected = Point([ y, x, -z, 1])
        calculated = Point.calculate(mne._matrix_2_xx0)
        assert calculated == expected

    def test_matrix_2_xxq(self):
        expected = Point([ y, x, 1-z, 1])
        calculated = Point.calculate(mne._matrix_2_xxq)
        assert calculated == expected

    def test_matrix_2_1_xqx0_qq0(self):
        expected = Point([ y, 1+x, -z, 1])
        calculated = Point.calculate(mne._matrix_2_1_xqx0_qq0)
        assert calculated == expected

    def test_matrix_2_1_xmqx0_qq0(self):
        expected = Point([ 1+y, x, -z, 1])
        calculated = Point.calculate(mne._matrix_2_1_xmqx0_qq0)
        assert calculated == expected

    def test_matrix_2_1_xxq_hh0(self):
        expected = Point([ 1+y, 1+x, 1-z, 1])
        calculated = Point.calculate(mne._matrix_2_1_xxq_hh0)
        assert calculated == expected

    def test_matrix_2_1_xmqxo_hh0(self):
        expected = Point([ 1.5+y, 0.5+x, 0.5-z, 1])
        calculated = Point.calculate(mne._matrix_2_1_xmqxo_hh0)
        assert calculated == expected

    def test_matrix_2_1_xqx3o_hh0(self):
        expected = Point([ 0.5+y, 1.5+x, 1.5-z, 1])
        calculated = Point.calculate(mne._matrix_2_1_xqx3o_hh0)
        assert calculated == expected

    def test_matrix_2_1_xxo_qq0(self):
        expected = Point([ 0.5+y, 0.5+x, 0.5-z, 1])
        calculated = Point.calculate(mne._matrix_2_1_xxo_qq0)
        assert calculated == expected

    def test_matrix_2_1_xmqx3o_hh0(self):
        expected = Point([ 1.5+y, 0.5+x, 1.5-z, 1])
        calculated = Point.calculate(mne._matrix_2_1_xmqx3o_hh0)
        assert calculated == expected

    def test_matrix_2_1_xxo_3q3qo(self):
        expected = Point([ 1.5+y, 1.5+x, 0.5-z, 1])
        calculated = Point.calculate(mne._matrix_2_1_xxo_3q3qo)
        assert calculated == expected
