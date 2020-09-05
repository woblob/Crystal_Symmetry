import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_3_mxmxx:

    def test_matrix_3_mxmxx(self):
        expected = Point([ -z, x, -y, 1])
        calculated = Point.calculate(mne._matrix_3_mxmxx)
        assert calculated == expected

    def test_matrix_3_2_tmxHmxx_HHmH(self):
        expected = Point([ 1-z, x, -y, 1])
        calculated = Point.calculate(mne._matrix_3_2_tmxHmxx_HHmH)
        assert calculated == expected

    def test_matrix_3_mxhmxx(self):
        expected = Point([ -z, 1+x, 1-y, 1])
        calculated = Point.calculate(mne._matrix_3_mxhmxx)
        assert calculated == expected

    def test_matrix_3_hmxhmxx(self):
        expected = Point([ 1-z, x, 1-y, 1])
        calculated = Point.calculate(mne._matrix_3_hmxhmxx)
        assert calculated == expected

    def test_matrix_3_2_Hmxtmxx_ttmt(self):
        expected = Point([ 1-z, 1+x, -y, 1])
        calculated = Point.calculate(mne._matrix_3_2_Hmxtmxx_ttmt)
        assert calculated == expected

    def test_matrix_3_2_tmx2tmxx_HHmH(self):
        expected = Point([ 1-z, 1+x, 1-y, 1])
        calculated = Point.calculate(mne._matrix_3_2_tmx2tmxx_HHmH)
        assert calculated == expected
