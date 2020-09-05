import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_m3_xxx:

    def test_matrix_m3_xxx(self):
        expected = Point([ -z, -x, -y, 1])
        calculated = Point.calculate(mne._matrix_m3_xxx)
        assert calculated == expected

    def test_matrix_m3_xhxx_0h0(self):
        expected = Point([ -z, 1-x, 1-y, 1])
        calculated = Point.calculate(mne._matrix_m3_xhxx_0h0)
        assert calculated == expected

    def test_matrix_m3_mhxmhxx_00h(self):
        expected = Point([ 1-z, -x, 1-y, 1])
        calculated = Point.calculate(mne._matrix_m3_mhxmhxx_00h)
        assert calculated == expected

    def test_matrix_m3_mhxxx_h00(self):
        expected = Point([ 1-z, 1-x, -y, 1])
        calculated = Point.calculate(mne._matrix_m3_mhxxx_h00)
        assert calculated == expected

    def test_matrix_m3_xxx_qqq(self):
        expected = Point([ 1-z, 1-x, 1-y, 1])
        calculated = Point.calculate(mne._matrix_m3_xxx_qqq)
        assert calculated == expected

    def test_matrix_m3_xmhxx_3omo3o(self):
        expected = Point([ 1.5-z, 0.5-x, 0.5-y, 1])
        calculated = Point.calculate(mne._matrix_m3_xmhxx_3omo3o)
        assert calculated == expected

    def test_matrix_m3_hxhxx_3o3omo(self):
        expected = Point([ 0.5-z, 1.5-x, 0.5-y, 1])
        calculated = Point.calculate(mne._matrix_m3_hxhxx_3o3omo)
        assert calculated == expected

    def test_matrix_m3_mhxxx_mo3o3o(self):
        expected = Point([ 0.5-z, 0.5-x, 1.5-y, 1])
        calculated = Point.calculate(mne._matrix_m3_mhxxx_mo3o3o)
        assert calculated == expected

    def test_matrix_m3_xxx_3o3o3o(self):
        expected = Point([ 1.5-z, 1.5-x, 1.5-y, 1])
        calculated = Point.calculate(mne._matrix_m3_xxx_3o3o3o)
        assert calculated == expected
