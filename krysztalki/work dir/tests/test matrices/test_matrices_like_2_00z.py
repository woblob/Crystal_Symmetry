import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_2_00z:

    def test_matrix_2_00z(self):
        expected = Point([ -x, -y, z, 1])
        calculated = Point.calculate(mne._matrix_2_00z)
        assert calculated == expected

    def test_matrix_2_1_0qz_00h(self):
        expected = Point([ -x, 1-y, 1+z, 1])
        calculated = Point.calculate(mne._matrix_2_1_0qz_00h)
        assert calculated == expected

    def test_matrix_2_1_q0z_00h(self):
        expected = Point([ 1-x, -y, 1+z, 1])
        calculated = Point.calculate(mne._matrix_2_1_q0z_00h)
        assert calculated == expected

    def test_matrix_2_qqz(self):
        expected = Point([ 1-x, 1-y, z, 1])
        calculated = Point.calculate(mne._matrix_2_qqz)
        assert calculated == expected

    def test_matrix_2_1_qqz_00h(self):
        expected = Point([ 1-x, 1-y, 1+z, 1])
        calculated = Point.calculate(mne._matrix_2_1_qqz_00h)
        assert calculated == expected

    def test_matrix_2_0qz(self):
        expected = Point([ -x, 1-y, z, 1])
        calculated = Point.calculate(mne._matrix_2_0qz)
        assert calculated == expected
