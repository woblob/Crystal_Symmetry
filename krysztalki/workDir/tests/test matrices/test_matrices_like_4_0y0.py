import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_4_0y0:

    def test_matrix_4_0y0(self):
        expected = Point([ z, y, -x, 1])
        calculated = Point.calculate(mne._matrix_4_0y0)
        assert calculated == expected

    def test_matrix_4_qymq(self):
        expected = Point([ 1+z, y, -x, 1])
        calculated = Point.calculate(mne._matrix_4_qymq)
        assert calculated == expected

    def test_matrix_4_2_0y0_0h0(self):
        expected = Point([ z, 1+y, -x, 1])
        calculated = Point.calculate(mne._matrix_4_2_0y0_0h0)
        assert calculated == expected

    def test_matrix_4_qyq(self):
        expected = Point([ z, y, 1-x, 1])
        calculated = Point.calculate(mne._matrix_4_qyq)
        assert calculated == expected

    def test_matrix_4_1_3qy0_0q0(self):
        expected = Point([ 1+z, y, 1-x, 1])
        calculated = Point.calculate(mne._matrix_4_1_3qy0_0q0)
        assert calculated == expected

    def test_matrix_4_qy0_0h0(self):
        expected = Point([ 1+z, 1+y, 1-x, 1])
        calculated = Point.calculate(mne._matrix_4_qy0_0h0)
        assert calculated == expected

    def test_matrix_4_1_qy0_0q0(self):
        expected = Point([ 0.5+z, 0.5+y, 0.5-x, 1])
        calculated = Point.calculate(mne._matrix_4_1_qy0_0q0)
        assert calculated == expected

    def test_matrix_4_1_hymq_0q0(self):
        expected = Point([ 1.5+z, 0.5+y, 0.5-x, 1])
        calculated = Point.calculate(mne._matrix_4_1_hymq_0q0)
        assert calculated == expected

    def test_matrix_4_3_hyq_03q0(self):
        expected = Point([ 0.5+z, 1.5+y, 1.5-x, 1])
        calculated = Point.calculate(mne._matrix_4_3_hyq_03q0)
        assert calculated == expected

    def test_matrix_4_3_hymq_03q0(self):
        expected = Point([ 1.5+z, 1.5+y, 0.5-x, 1])
        calculated = Point.calculate(mne._matrix_4_3_hymq_03q0)
        assert calculated == expected
