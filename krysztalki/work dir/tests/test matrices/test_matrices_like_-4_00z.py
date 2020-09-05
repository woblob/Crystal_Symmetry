import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_m4_00z:

    def test_matrix_m4_00z(self):
        expected = Point([ y, -x, -z, 1])
        calculated = Point.calculate(mne._matrix_m4_00z)
        assert calculated == expected

    def test_matrix_m4_qmqz_qmq0(self):
        expected = Point([ 1+y, -x, -z, 1])
        calculated = Point.calculate(mne._matrix_m4_qmqz_qmq0)
        assert calculated == expected

    def test_matrix_m4_qqz_qq0(self):
        expected = Point([ y, 1-x, -z, 1])
        calculated = Point.calculate(mne._matrix_m4_qqz_qq0)
        assert calculated == expected

    def test_matrix_m4_00z_00q(self):
        expected = Point([ y, -x, 1-z, 1])
        calculated = Point.calculate(mne._matrix_m4_00z_00q)
        assert calculated == expected

    def test_matrix_m4_h0z_h0q(self):
        expected = Point([ 1+y, 1-x, 1-z, 1])
        calculated = Point.calculate(mne._matrix_m4_h0z_h0q)
        assert calculated == expected

    def test_matrix_m4_hqz_hqo(self):
        expected = Point([ 0.5+y, 1.5-x, 0.5-z, 1])
        calculated = Point.calculate(mne._matrix_m4_hqz_hqo)
        assert calculated == expected

    def test_matrix_m4_hmqz_hmq3o(self):
        expected = Point([ 1.5+y, 0.5-x, 1.5-z, 1])
        calculated = Point.calculate(mne._matrix_m4_hmqz_hmq3o)
        assert calculated == expected
