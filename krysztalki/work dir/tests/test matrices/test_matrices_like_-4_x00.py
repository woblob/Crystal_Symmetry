import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_m4_x00:

    def test_matrix_m4_x00(self):
        expected = Point([ -x, z, -y, 1])
        calculated = Point.calculate(mne._matrix_m4_x00)
        assert calculated == expected

    def test_matrix_m4_x00_q00(self):
        expected = Point([ 1-x, z, -y, 1])
        calculated = Point.calculate(mne._matrix_m4_x00_q00)
        assert calculated == expected
        #  _translation_h00  #133=134

    def test_matrix_m4_1qmq_0qmq(self):
        expected = Point([ -x, 1+z, -y, 1])
        calculated = Point.calculate(mne._matrix_m4_xqmq_0qmq)
        assert calculated == expected
        #  _translation_0h0  #85=86

    def test_matrix_m4_xqq_0qq(self):
        expected = Point([ -x, z, 1-y, 1])
        calculated = Point.calculate(mne._matrix_m4_xqq_0qq)
        assert calculated == expected
        #  _translation_00h  # 37=38

    def test_matrix_m4_xh0_qh0(self):
        expected = Point([ 1-x, 1+z, 1-y, 1])
        calculated = Point.calculate(mne._matrix_m4_xh0_qh0)
        assert calculated == expected
        #  _translation_hhh  #181=182

    def test_matrix_m4_xhq_ohq(self):
        expected = Point([ 0.5-x, 0.5+z, 1.5-y, 1])
        calculated = Point.calculate(mne._matrix_m4_xhq_ohq)
        assert calculated == expected
        #  _translation_qqq  _translation_00h  #37=38

    def test_matrix_m4_xhmq_3ohmq(self):
        expected = Point([ 1.5-x, 1.5+z, 0.5-y, 1])
        calculated = Point.calculate(mne._matrix_m4_xhmq_3ohmq)
        assert calculated == expected
        #  _translation_qqq  _translation_hh0  #85
