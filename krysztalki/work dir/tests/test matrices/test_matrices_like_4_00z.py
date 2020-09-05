import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_4_00z:

    def test_matrix_4_00z(self):
        expected = Point([ -y, x, z, 1])
        calculated = Point.calculate(mne._matrix_4_00z)
        assert calculated == expected

    def test_matrix_4_qqz(self):
        expected = Point([ 1-y, x, z, 1])
        calculated = Point.calculate(mne._matrix_4_qqz)
        assert calculated == expected

    def test_matrix_4_mqqz(self):
        expected = Point([ -y, 1+x, z, 1])
        calculated = Point.calculate(mne._matrix_4_mqqz)
        assert calculated == expected

    def test_matrix_4_2_00z_00h(self):
        expected = Point([ -y, x, 1+z, 1])
        calculated = Point.calculate(mne._matrix_4_2_00z_00h)
        assert calculated == expected

    def test_matrix_4_2_0hz_00h(self):
        expected = Point([ 1-y, 1+x, 1+z, 1])
        calculated = Point.calculate(mne._matrix_4_2_0hz_00h)
        assert calculated == expected

    def test_matrix_4_1_0qz_00q(self):
        expected = Point([ 0.5-y, 0.5+x, 0.5+z, 1])
        calculated = Point.calculate(mne._matrix_4_1_0qz_00q)
        assert calculated == expected

    def test_matrix_4_1_mqhz_00q(self):
        expected = Point([ 0.5-y, 1.5+x, 0.5+z, 1])
        calculated = Point.calculate(mne._matrix_4_1_mqhz_00q)
        assert calculated == expected

    def test_matrix_4_3_mqhz_003q(self):
        expected = Point([ 0.5-y, 1.5+x, 1.5+z, 1])
        calculated = Point.calculate(mne._matrix_4_3_mqhz_003q)
        assert calculated == expected

    def test_matrix_4_3_qhz_003q(self):
        expected = Point([ 1.5-y, 0.5+x, 1.5+z, 1])
        calculated = Point.calculate(mne._matrix_4_3_qhz_003q)
        assert calculated == expected

    def test_matrix_4_1_03qz_00q(self):
        expected = Point([ 1.5-y, 1.5+x, 0.5+z, 1])
        calculated = Point.calculate(mne._matrix_4_1_03qz_00q)
        assert calculated == expected
