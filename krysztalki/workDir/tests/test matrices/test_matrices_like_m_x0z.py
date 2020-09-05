import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])

class Test_Mirror_x0z:
    
    def test_matrix_m_x0z(self):
        expected = Point([ x, -y, z, 1])
        calculated = Point.calculate(mne._matrix_m_x0z)
        assert calculated == expected

    def test_matrix_c_xqz_00h(self):
        expected = Point([ x, 1-y, 1+z, 1])
        calculated = Point.calculate(mne._matrix_c_xqz_00h)
        assert calculated == expected

    def test_matrix_a_xqz_h00(self):
        expected = Point([ 1+x, 1-y, z, 1])
        calculated = Point.calculate(mne._matrix_a_xqz_h00)
        assert calculated == expected

    def test_matrix_n_xqz_h0h(self):
        expected = Point([ 1+x, 1-y, 1+z, 1])
        calculated = Point.calculate(mne._matrix_n_xqz_h0h)
        assert calculated == expected

    def test_matrix_d_xoz_q0q(self):
        expected = Point([ 0.5+x, 0.5-y, 0.5+z, 1])
        calculated = Point.calculate(mne._matrix_d_xoz_q0q)
        assert calculated == expected

    def test_matrix_d_x3oz_q03q(self):
        expected = Point([ 0.5+x, 1.5-y, 1.5+z, 1])
        calculated = Point.calculate(mne._matrix_d_x3oz_q03q)
        assert calculated == expected

    def test_matrix_d_xoz_3q03q(self):
        expected = Point([ 1.5+x, 0.5-y, 1.5+z, 1])
        calculated = Point.calculate(mne._matrix_d_xoz_3q03q)
        assert calculated == expected

    def test_matrix_d_x3oz_3q0q(self):
        expected = Point([ 1.5+x, 1.5-y, 0.5+z, 1])
        calculated = Point.calculate(mne._matrix_d_x3oz_3q0q)
        assert calculated == expected

    def test_matrix_a_x0z_h00(self):
        expected = Point([ 1+x, -y, +z, 1])
        calculated = Point.calculate(mne._matrix_a_x0z_h00)
        assert calculated == expected

    def test_matrix_d_xoz_q03q(self):
        expected = Point([ 0.5+x, 0.5-y, 1.5+z, 1])
        calculated = Point.calculate(mne._matrix_d_xoz_q03q)
        assert calculated == expected

    def test_matrix_d_x3oz_q0q(self):
        expected = Point([ 0.5+x, 1.5-y, 0.5+z, 1])
        calculated = Point.calculate(mne._matrix_d_x3oz_q0q)
        assert calculated == expected

    def test_matrix_d_xoz_3q0q(self):
        expected = Point([ 1.5+x, 0.5-y, 0.5+z, 1])
        calculated = Point.calculate(mne._matrix_d_xoz_3q0q)
        assert calculated == expected

    def test_matrix_d_x3oz_3q03q(self):
        expected = Point([ 1.5+x, 1.5-y, 1.5+z, 1])
        calculated = Point.calculate(mne._matrix_d_x3oz_3q03q)
        assert calculated == expected
