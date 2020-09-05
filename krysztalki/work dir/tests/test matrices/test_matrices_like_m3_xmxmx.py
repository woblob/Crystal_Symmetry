import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_m3_xmxmx:

    def test_matrix_m3_xmxmx(self):
        expected = Point([ z, x, -y, 1])
        calculated = Point.calculate(mne._matrix_m3_xmxmx)
        assert calculated == expected

    def test_matrix_m3_mhxhmxmx_mqqmq(self):
        expected = Point([ z, 1+x, -y, 1])
        calculated = Point.calculate(mne._matrix_m3_mhxhmxmx_mqqmq)
        assert calculated == expected

    def test_matrix_m3_xhmxmx_0h0(self):
        expected = Point([ z, 1+x, 1-y, 1])
        calculated = Point.calculate(mne._matrix_m3_xhmxmx_0h0)
        assert calculated == expected

    def test_matrix_m3_hxhmxmx_hh0(self):
        expected = Point([ 1+z, x, 1-y, 1])
        calculated = Point.calculate(mne._matrix_m3_hxhmxmx_hh0)
        assert calculated == expected

    def test_matrix_m3_mhx1mxmx_0hmh(self):
        expected = Point([ 1+z, 1+x, -y, 1])
        calculated = Point.calculate(mne._matrix_m3_mhx1mxmx_0hmh)
        assert calculated == expected

    def test_matrix_m3_xmxmx_q3qmq(self):
        expected = Point([ 1+z, 1+x, 1-y, 1])
        calculated = Point.calculate(mne._matrix_m3_xmxmx_q3qmq)
        assert calculated == expected

    def test_matrix_m3_x1mxmx_3o5om3o(self):
        expected = Point([ 1.5+z, 0.5+x, 0.5-y, 1])
        calculated = Point.calculate(mne._matrix_m3_x1mxmx_3o5om3o)
        assert calculated == expected

    def test_matrix_m3_mhx1mxmx_mo5om3o(self):
        expected = Point([ 0.5+z, 1.5+x, 0.5-y, 1])
        calculated = Point.calculate(mne._matrix_m3_mhx1mxmx_mo5om3o)
        assert calculated == expected

    def test_matrix_m3_hxhmxmx_3o5oo(self):
        expected = Point([ 0.5+z, 0.5+x, 1.5-y, 1])
        calculated = Point.calculate(mne._matrix_m3_hxhmxmx_3o5oo)
        assert calculated == expected

    def test_matrix_m3_xhmxmx_3oom3o(self):
        expected = Point([ 1.5+z, 1.5+x, 1.5-y, 1])
        calculated = Point.calculate(mne._matrix_m3_xhmxmx_3oom3o)
        assert calculated == expected
