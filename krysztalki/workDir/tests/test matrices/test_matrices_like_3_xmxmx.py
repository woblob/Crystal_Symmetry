import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_3_xmxmx:

    def test_matrix_3_xmxmx(self):
        expected = Point([ -z, -x, y, 1])
        calculated = Point.calculate(mne._matrix_3_xmxmx)
        assert calculated == expected

    def test_matrix_3_2_txmHmxmx_mttt(self):
        expected = Point([ -z, 1-x, 1+y, 1])
        calculated = Point.calculate(mne._matrix_3_2_txmHmxmx_mttt)
        assert calculated == expected

    def test_matrix_3_hxmhmxmx(self):
        expected = Point([ 1-z, -x, 1+y, 1])
        calculated = Point.calculate(mne._matrix_3_hxmhmxmx)
        assert calculated == expected

    def test_matrix_3_hxmxmx(self):
        expected = Point([ 1-z, 1-x, y, 1])
        calculated = Point.calculate(mne._matrix_3_hxmxmx)
        assert calculated == expected

    def test_matrix_3_2_2txmtmxmx_mHHH(self):
        expected = Point([ 1-z, 1-x, 1+y, 1])
        calculated = Point.calculate(mne._matrix_3_2_2txmtmxmx_mHHH)
        assert calculated == expected

    def test_matrix_3_2_HxHmxmx_mHHH(self):
        expected = Point([ -z, 1-x, y, 1])
        calculated = Point.calculate(mne._matrix_3_2_HxHmxmx_mHHH)
        assert calculated == expected
