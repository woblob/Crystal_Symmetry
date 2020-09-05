import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_2_x0x:

    def test_matrix_2_x0x(self):
        expected = Point([ z, -y, x, 1])
        calculated = Point.calculate(mne._matrix_2_x0x)
        assert calculated == expected

    def test_matrix_2_1_mqx0x_q0q(self):
        expected = Point([ z, -y, 1+x, 1])
        calculated = Point.calculate(mne._matrix_2_1_mqx0x_q0q)
        assert calculated == expected

    def test_matrix_2_xqx(self):
        expected = Point([ z, 1-y, x, 1])
        calculated = Point.calculate(mne._matrix_2_xqx)
        assert calculated == expected

    def test_matrix_2_1_qx0x_q0mq(self):
        expected = Point([ 1+z, -y, x, 1])
        calculated = Point.calculate(mne._matrix_2_1_qx0x_q0mq)
        assert calculated == expected

    def test_matrix_2_1_xqx_q0q(self):
        expected = Point([ 1+z, 1-y, 1+x, 1])
        calculated = Point.calculate(mne._matrix_2_1_xqx_q0q)
        assert calculated == expected

    def test_matrix_2_1_qx3ox_h0h(self):
        expected = Point([ 1.5+z, 1.5-y, 0.5+x, 1])
        calculated = Point.calculate(mne._matrix_2_1_qx3ox_h0h)
        assert calculated == expected

    def test_matrix_2_1_mqxox_h0h(self):
        expected = Point([ 0.5+z, 0.5-y, 1.5+x, 1])
        calculated = Point.calculate(mne._matrix_2_1_mqxox_h0h)
        assert calculated == expected

    def test_matrix_2_1_xox_q0q(self):
        expected = Point([ 0.5+z, 0.5-y, 0.5+x, 1])
        calculated = Point.calculate(mne._matrix_2_1_xox_q0q)
        assert calculated == expected

    def test_matrix_2_1_mqx3ox_h0h(self):
        expected = Point([ 0.5+z, 1.5-y, 1.5+x, 1])
        calculated = Point.calculate(mne._matrix_2_1_mqx3ox_h0h)
        assert calculated == expected

    def test_matrix_2_1_xox_3q03q(self):
        expected = Point([ 1.5+z, 0.5-y, 1.5+x, 1])
        calculated = Point.calculate(mne._matrix_2_1_xox_3q03q)
        assert calculated == expected
