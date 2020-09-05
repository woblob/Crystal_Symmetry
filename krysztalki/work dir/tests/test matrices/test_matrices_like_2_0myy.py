import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_2_0myy:

    def test_matrix_2_0myy(self):
        expected = Point([ -x, -z, -y, 1])
        calculated = Point.calculate(mne._matrix_2_0myy)
        assert calculated == expected

    def test_matrix_2_qmyy(self):
        expected = Point([ 1-x, -z, -y, 1])
        calculated = Point.calculate(mne._matrix_2_qmyy)
        assert calculated == expected

    def test_matrix_2_1_0qmyy_0qmq(self):
        expected = Point([ -x, 1-z, -y, 1])
        calculated = Point.calculate(mne._matrix_2_1_0qmyy_0qmq)
        assert calculated == expected

    def test_matrix_2_0qmyy_0mqq(self):
        expected = Point([ -x, -z, 1-y, 1])
        calculated = Point.calculate(mne._matrix_2_0qmyy_0mqq)
        assert calculated == expected

    def test_matrix_2_qhmyy(self):
        expected = Point([ 1-x, 1-z, 1-y, 1])
        calculated = Point.calculate(mne._matrix_2_qhmyy)
        assert calculated == expected

    def test_matrix_2_oqmyy(self):
        expected = Point([ 0.5-x, 0.5-z, 0.5-y, 1])
        calculated = Point.calculate(mne._matrix_2_oqmyy)
        assert calculated == expected

    def test_matrix_2_o3qmyy(self):
        expected = Point([ 0.5-x, 1.5-z, 1.5-y, 1])
        calculated = Point.calculate(mne._matrix_2_o3qmyy)
        assert calculated == expected

    def test_matrix_2_1_3ohmyy_0qmq(self):
        expected = Point([ 1.5-x, 1.5-z, 0.5-y, 1])
        calculated = Point.calculate(mne._matrix_2_1_3ohmyy_0qmq)
        assert calculated == expected

    def test_matrix_2_3o3qmyy(self):
        expected = Point([ 1.5-x, 1.5-z, 1.5-y, 1])
        calculated = Point.calculate(mne._matrix_2_3o3qmyy)
        assert calculated == expected

    def test_matrix_2_0myy_h0h_out(self):
        expected = Point([ 1.5-x, 0.5-z, 1.5-y, 1])
        calculated = Point.calculate(mne._matrix_2_myy)
        assert calculated == expected