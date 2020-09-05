import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Mirror_0yz:

    def test_matrix_m_0yz(self):
        expected = Point([ -x, y, z, 1])
        calculated = Point.calculate(mne._matrix_m_0yz)
        assert calculated == expected

    def test_matrix_c_0yz_00h(self):
        expected = Point([ -x, y, 1+z, 1])
        calculated = Point.calculate(mne._matrix_c_0yz_00h)
        assert calculated == expected

    def test_matrix_b_qyz(self):
        expected = Point([ 1-x, 1+y, z, 1])
        calculated = Point.calculate(mne._matrix_b_qyz_0h0)
        assert calculated == expected

    def test_matrix_d_oyz_0qq(self):
        expected = Point([ 0.5-x, 0.5+y, 0.5+z, 1])
        calculated = Point.calculate(mne._matrix_d_oyz_0qq)
        assert calculated == expected

    def test_matrix_d_3oyz_0qq(self):
        expected = Point([ 1.5-x, 0.5+y, 0.5+z, 1])
        calculated = Point.calculate(mne._matrix_d_3oyz_0qq)
        assert calculated == expected

    def test_matrix_d_oyz_03qq(self):
        expected = Point([ 0.5-x, 1.5+y, 0.5+z, 1])
        calculated = Point.calculate(mne._matrix_d_oyz_03qq)
        assert calculated == expected

    def test_matrix_d_oyz_0q3q(self):
        expected = Point([ 0.5-x, 0.5+y, 1.5+z, 1])
        calculated = Point.calculate(mne._matrix_d_oyz_0q3q)
        assert calculated == expected

    def test_matrix_d_oyz_03q3q(self):
        expected = Point([ 0.5-x, 1.5+y, 1.5+z, 1])
        calculated = Point.calculate(mne._matrix_d_oyz_03q3q)
        assert calculated == expected

    def test_matrix_d_3oyz_0q3q(self):
        expected = Point([ 1.5-x, 0.5+y, 1.5+z, 1])
        calculated = Point.calculate(mne._matrix_d_3oyz_0q3q)
        assert calculated == expected

    def test_matrix_d_3oyz_03qq(self):
        expected = Point([ 1.5-x, 1.5+y, 0.5+z, 1])
        calculated = Point.calculate(mne._matrix_d_3oyz_03qq)
        assert calculated == expected

    def test_matrix_d_3oyz_03q3q(self):
        expected = Point([ 1.5-x, 1.5+y, 1.5+z, 1])
        calculated = Point.calculate(mne._matrix_d_3oyz_03q3q)
        assert calculated == expected
