import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_2_mx0x:

    def test_matrix_2_mx0x(self):
        expected = Point([ -z, -y, -x, 1])
        calculated = Point.calculate(mne._matrix_2_mx0x)
        assert calculated == expected

    def test_matrix_2_1_qmx0x_mq0q(self):
        expected = Point([ -z, -y, 1-x, 1])
        calculated = Point.calculate(mne._matrix_2_1_qmx0x_mq0q)
        assert calculated == expected
        
    def test_matrix_2_mxqx(self):
        expected = Point([ -z, 1-y, -x, 1])
        calculated = Point.calculate(mne._matrix_2_mxqx)
        assert calculated == expected
        
    def test_matrix_2_1_qmx0x_q0mq(self):
        expected = Point([ 1-z, -y, -x, 1])
        calculated = Point.calculate(mne._matrix_2_1_qmx0x_q0mq)
        assert calculated == expected
        
    def test_matrix_2_hmxqx(self):
        expected = Point([ 1-z, 1-y, 1-x, 1])
        calculated = Point.calculate(mne._matrix_2_hmxqx)
        assert calculated == expected
        
    def test_matrix_2_qmxox(self):
        expected = Point([ 0.5-z, 0.5-y, 0.5-x, 1])
        calculated = Point.calculate(mne._matrix_2_qmxox)
        assert calculated == expected
        
    def test_matrix_2_3qmx3ox(self):
        expected = Point([ 1.5-z, 1.5-y, 1.5-x, 1])
        calculated = Point.calculate(mne._matrix_2_3qmx3ox)
        assert calculated == expected

    def test_matrix_2_1_hmx3ox_mq0q(self):
        expected = Point([ 0.5-z, 1.5-y, 1.5-x, 1])
        calculated = Point.calculate(mne._matrix_2_1_hmx3ox_mq0q)
        assert calculated == expected
        
    def test_matrix_2_3qmx3ox_dwa(self):
        expected = Point([ 1.5-z, 0.5-y, 1.5-x, 1])
        calculated = Point.calculate(mne._matrix_2_3qmxox)
        assert calculated == expected

    def test_matrix_2_1_hmx3ox_q0mq(self):
        expected = Point([ 1.5-z, 1.5-y, 0.5-x, 1])
        calculated = Point.calculate(mne._matrix_2_1_hmx3ox_q0mq)
        assert calculated == expected
