import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_3_xxx:

    def test_matrix_3_xxx(self):
        expected = Point([ z, x, y, 1])
        calculated = Point.calculate(mne._matrix_3_xxx)
        assert calculated == expected

    def test_matrix_3_1_mtmHxx_ttt(self):
        expected = Point([ z, 1+x, 1+y, 1])
        calculated = Point.calculate(mne._matrix_3_1_mtmHxx_ttt)
        assert calculated == expected

    def test_matrix_3_1_HxmHxx_ttt(self):
        expected = Point([ 1+z, x, 1+y, 1])
        calculated = Point.calculate(mne._matrix_3_1_HxmHxx_ttt)
        assert calculated == expected

    def test_matrix_3_1_Hxtxx_ttt(self):
        expected = Point([ 1+z, 1+x, y, 1])
        calculated = Point.calculate(mne._matrix_3_1_Hxtxx_ttt)
        assert calculated == expected

    def test_matrix_3_xxx_hhh(self):
        expected = Point([ 1+z, 1+x, 1+y, 1])
        calculated = Point.calculate(mne._matrix_3_xxx_hhh)
        assert calculated == expected
