import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_m3_mxmxx:

    def test_matrix_m3_mxmxx(self):
        expected = Point([ z, -x, y, 1])
        calculated = Point.calculate(mne._matrix_m3_mxmxx)
        assert calculated == expected

    def test_matrix_m3_mxmhmxx_qmqmq(self):
        expected = Point([ 1+z, -x, y, 1])
        calculated = Point.calculate(mne._matrix_m3_mxmhmxx_qmqmq)
        assert calculated == expected

    def test_matrix_m3_1mxhmxx_h0h(self):
        expected = Point([ z, 1-x, 1+y, 1])
        calculated = Point.calculate(mne._matrix_m3_1mxhmxx_h0h)
        assert calculated == expected

    def test_matrix_m3_hmxmhmxx_hmh0(self):
        expected = Point([ 1+z, -x, 1+y, 1])
        calculated = Point.calculate(mne._matrix_m3_hmxmhmxx_hmh0)
        assert calculated == expected

    def test_matrix_m3_hmxmxx_h00(self):
        expected = Point([ 1+z, 1-x, y, 1])
        calculated = Point.calculate(mne._matrix_m3_hmxmxx_h00)
        assert calculated == expected

    def test_matrix_m3_mxmxx_3qmqq(self):
        expected = Point([ 1+z, 1-x, 1+y, 1])
        calculated = Point.calculate(mne._matrix_m3_mxmxx_3qmqq)
        assert calculated == expected

    def test_matrix_m3_hmxmhmxx_5om3omo(self):
        expected = Point([ 1.5+z, 0.5-x, 0.5+y, 1])
        calculated = Point.calculate(mne._matrix_m3_hmxmhmxx_5om3omo)
        assert calculated == expected

    def test_matrix_m3_1mxhmxx_5oo3o(self):
        expected = Point([ 0.5+z, 1.5-x, 0.5+y, 1])
        calculated = Point.calculate(mne._matrix_m3_1mxhmxx_5oo3o)
        assert calculated == expected

    def test_matrix_m3_1mxmxx_5om3o3o(self):
        expected = Point([ 0.5+z, 0.5-x, 1.5+y, 1])
        calculated = Point.calculate(mne._matrix_m3_1mxmxx_5om3o3o)
        assert calculated == expected

    def test_matrix_m3_hmxmxx_om3o3o(self):
        expected = Point([ 1.5+z, 1.5-x, 1.5+y, 1])
        calculated = Point.calculate(mne._matrix_m3_hmxmxx_om3o3o)
        assert calculated == expected
