import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_m3_mxxmx:

    def test_matrix_m3_mxxmx(self):
        expected = Point([ -z, x, y, 1])
        calculated = Point.calculate(mne._matrix_m3_mxxmx)
        assert calculated == expected

    def test_matrix_m3_mhmxxmx_mqmqq(self):
        expected = Point([ -z, x, 1+y, 1])
        calculated = Point.calculate(mne._matrix_m3_mhmxxmx_mqmqq)
        assert calculated == expected

    def test_matrix_m3_m1mxhxmx_mh0h(self):
        expected = Point([ -z, 1+x, 1+y, 1])
        calculated = Point.calculate(mne._matrix_m3_m1mxhxmx_mh0h)
        assert calculated == expected

    def test_matrix_m3_hmxhxmx_00h(self):
        expected = Point([ 1-z, x, 1+y, 1])
        calculated = Point.calculate(mne._matrix_m3_hmxhxmx_00h)
        assert calculated == expected

    def test_matrix_m3_mhmx1xmx_0hh(self):
        expected = Point([ 1-z, 1+x, y, 1])
        calculated = Point.calculate(mne._matrix_m3_mhmx1xmx_0hh)
        assert calculated == expected

    def test_matrix_m3_mxxmx_mqq3q(self):
        expected = Point([ 1-z, 1+x, 1+y, 1])
        calculated = Point.calculate(mne._matrix_m3_mxxmx_mqq3q)
        assert calculated == expected

    def test_matrix_m3_mhmx1xmx_o3o5o(self):
        expected = Point([ 1.5-z, 0.5+x, 0.5+y, 1])
        calculated = Point.calculate(mne._matrix_m3_mhmx1xmx_o3o5o)
        assert calculated == expected

    def test_matrix_m3_m1mx1xmx_m3o3o5o(self):
        expected = Point([ 0.5-z, 1.5+x, 0.5+y, 1])
        calculated = Point.calculate(mne._matrix_m3_m1mx1xmx_m3o3o5o)
        assert calculated == expected

    def test_matrix_m3_m1mxhxmx_m3omo5o(self):
        expected = Point([ 0.5-z, 0.5+x, 1.5+y, 1])
        calculated = Point.calculate(mne._matrix_m3_m1mxhxmx_m3omo5o)
        assert calculated == expected

    def test_matrix_m3_mhmxhxmx_m3o3oo(self):
        expected = Point([ 1.5-z, 1.5+x, 1.5+y, 1])
        calculated = Point.calculate(mne._matrix_m3_mhmxhxmx_m3o3oo)
        assert calculated == expected
