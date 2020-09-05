import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_2_x00:

    def test_matrix_2_x00(self):
        expected = Point([ x, -y, -z, 1])
        calculated = Point.calculate(mne._matrix_2_x00)
        assert calculated == expected

    def test_matrix_2_xqq(self):
        expected = Point([ x, 1-y, 1-z, 1])
        calculated = Point.calculate(mne._matrix_2_xqq)
        assert calculated == expected

    def test_matrix_2_1_x0q_h00(self):
        expected = Point([ 1+x, -y, 1-z, 1])
        calculated = Point.calculate(mne._matrix_2_1_x0q_h00)
        assert calculated == expected

    def test_matrix_2_1_xq0_h00(self):
        expected = Point([ 1+x, 1-y, -z, 1])
        calculated = Point.calculate(mne._matrix_2_1_xq0_h00)
        assert calculated == expected

    def test_matrix_2_1_xqq_h00(self):
        expected = Point([ 1+x, 1-y, 1-z, 1])
        calculated = Point.calculate(mne._matrix_2_1_xqq_h00)
        assert calculated == expected

    def test_matrix_2_x0q(self):
        expected = Point([ x, -y, 1-z, 1])
        calculated = Point.calculate(mne._matrix_2_x0q)
        assert calculated == expected
