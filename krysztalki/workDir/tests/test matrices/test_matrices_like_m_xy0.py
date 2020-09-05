import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Mirror_xy0:

    def test_matrix_m_xy0(self):
        expected = Point([ x, y, -z, 1])
        calculated = Point.calculate(mne._matrix_m_xy0)
        assert calculated == expected

    def test_matrix_b_xyq_0h0(self):
        expected = Point([ x, 1+y, 1-z, 1])
        calculated = Point.calculate(mne._matrix_b_xyq_0h0)
        assert calculated == expected

    def test_matrix_a_xyq_h00(self):
        expected = Point([ 1+x, y, 1-z, 1])
        calculated = Point.calculate(mne._matrix_a_xyq_h00)
        assert calculated == expected

    def test_matrix_n_xy0_hh0(self):
        expected = Point([ 1+x, 1+y, -z, 1])
        calculated = Point.calculate(mne._matrix_n_xy0_hh0)
        assert calculated == expected

    def test_matrix_n_xyq_hh0(self):
        expected = Point([ 1+x, 1+y, 1-z, 1])
        calculated = Point.calculate(mne._matrix_n_xyq_hh0)
        assert calculated == expected

    def test_matrix_d_xyo_qq0(self):
        expected = Point([ 0.5+x, 0.5+y, 0.5-z, 1])
        calculated = Point.calculate(mne._matrix_d_xyo_qq0)
        assert calculated == expected

    def test_matrix_d_xy3o_q3q0(self):
        expected = Point([ 0.5+x, 1.5+y, 1.5-z, 1])
        calculated = Point.calculate(mne._matrix_d_xy3o_q3q0)
        assert calculated == expected

    def test_matrix_dxy3o_3qq0(self):
        expected = Point([ 1.5+x, 0.5+y, 1.5-z, 1])
        calculated = Point.calculate(mne._matrix_dxy3o_3qq0)
        assert calculated == expected

    def test_matrix_d_xyo_3q3q0(self):
        expected = Point([ 1.5+x, 1.5+y, 0.5-z, 1])
        calculated = Point.calculate(mne._matrix_d_xyo_3q3q0)
        assert calculated == expected

    def test_matrix_b_xy0_0h0(self):
        expected = Point([ x, 1+y, -z, 1])
        calculated = Point.calculate(mne._matrix_b_xy0_0h0)
        assert calculated == expected

    def test_matrix_d_xy3o_qq0(self):
        expected = Point([ 0.5+x, 0.5+y, 1.5-z, 1])
        calculated = Point.calculate(mne._matrix_d_xy3o_qq0)
        assert calculated == expected

    def test_matrix_d_xyo_q3q0(self):
        expected = Point([ 0.5+x, 1.5+y, 0.5-z, 1])
        calculated = Point.calculate(mne._matrix_d_xyo_q3q0)
        assert calculated == expected

    
    def test_matrix_d_xyo_3qq0(self):
        expected = Point([ 1.5+x, 0.5+y, 0.5-z, 1])
        calculated = Point.calculate(mne._matrix_d_xyo_3qq0)
        assert calculated == expected

    def test_matrix_d_xy3o_3q3q0(self):
        expected = Point([ 1.5+x, 1.5+y, 1.5-z, 1])
        calculated = Point.calculate(mne._matrix_d_xy3o_3q3q0)
        assert calculated == expected