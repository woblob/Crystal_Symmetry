import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_2_xmx0:

    def test_matrix_2_xmx0(self):
        expected = Point([ -y, -x, -z, 1])
        calculated = Point.calculate(mne._matrix_2_xmx0)
        assert calculated == expected

    def test_matrix_2_xmxq(self):
        expected = Point([ -y, -x, 1-z, 1])
        calculated = Point.calculate(mne._matrix_2_xmxq)
        assert calculated == expected

    def test_matrix_2_1_xqmx0_mqq0(self):
        expected = Point([ -y, 1-x, -z, 1])
        calculated = Point.calculate(mne._matrix_2_1_xqmx0_mqq0)
        assert calculated == expected

    def test_matrix_2_1_xqmx0_qmq0(self):
        expected = Point([ 1-y, -x, -z, 1])
        calculated = Point.calculate(mne._matrix_2_1_xqmx0_qmq0)
        assert calculated == expected

    def test_matrix_2_xhmxq(self):
        expected = Point([ 1-y, 1-x, 1-z, 1])
        calculated = Point.calculate(mne._matrix_2_xhmxq)
        assert calculated == expected

    def test_matrix_2_xqmxo(self):
        expected = Point([ 0.5-y, 0.5-x, 0.5-z, 1])
        calculated = Point.calculate(mne._matrix_2_xqmxo)
        assert calculated == expected

    def test_matrix_2_1_xhmx3o_mqq0(self):
        expected = Point([ 0.5-y, 1.5-x, 1.5-z, 1])
        calculated = Point.calculate(mne._matrix_2_1_xhmx3o_mqq0)
        assert calculated == expected

    def test_matrix_2_1_xhmx3o_qmq0(self):
        expected = Point([ 1.5-y, 0.5-x, 1.5-z, 1])
        calculated = Point.calculate(mne._matrix_2_1_xhmx3o_qmq0)
        assert calculated == expected

    def test_matrix_2_x3qmxo(self):
        expected = Point([ 1.5-y, 1.5-x, 0.5-z, 1])
        calculated = Point.calculate(mne._matrix_2_x3qmxo)
        assert calculated == expected

    def test_matrix_2_x3qmx3o(self):
        expected = Point([ 1.5-y, 1.5-x, 1.5-z, 1])
        calculated = Point.calculate(mne._matrix_2_x3qmx3o)
        assert calculated == expected

