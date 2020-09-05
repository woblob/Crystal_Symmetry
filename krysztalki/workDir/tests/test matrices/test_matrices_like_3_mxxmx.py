import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_3_mxxmx:

    def test_matrix_3_mxxmx(self):
        expected = Point([ z, -x, -y, 1])
        calculated = Point.calculate(mne._matrix_3_mxxmx)
        assert calculated == expected

    def test_matrix_3_2_mHmxtxmx_HmHH(self):
        expected = Point([ z, -x, 1-y, 1])
        calculated = Point.calculate(mne._matrix_3_2_mHmxtxmx_HmHH)
        assert calculated == expected

    def test_matrix_3_mxhxmx(self):
        expected = Point([ z, 1-x, 1-y, 1])
        calculated = Point.calculate(mne._matrix_3_mxhxmx)
        assert calculated == expected

    def test_matrix_3_2_HmxHxmx_tmtt(self):
        expected = Point([ 1+z, -x, 1-y, 1])
        calculated = Point.calculate(mne._matrix_3_2_HmxHxmx_tmtt)
        assert calculated == expected

    def test_matrix_3_hmxxmx(self):
        expected = Point([ 1+z, 1-x, -y, 1])
        calculated = Point.calculate(mne._matrix_3_hmxxmx)
        assert calculated == expected

    def test_matrix_3_2_tmxtxmx_HmHH(self):
        expected = Point([ 1+z, 1-x, 1-y, 1])
        calculated = Point.calculate(mne._matrix_3_2_tmxtxmx_HmHH)
        assert calculated == expected
