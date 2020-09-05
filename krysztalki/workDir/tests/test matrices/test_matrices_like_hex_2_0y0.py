import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_hex_2_0y0:

    def test_matrix_hex_2_0y0(self):
        expected = Point([ -x, -x+y, -z, 1])
        calculated = Point.calculate(mne._matrix_hex_2_0y0)
        assert calculated == expected
        # assert mne._matrix_hex_2_0y0 @ mne._matrix_hex_2_0y0

    def test_matrix_hex_2_0yq(self):
        expected = Point([ -x, -x+y, 1-z, 1])
        calculated = Point.calculate(mne._matrix_hex_2_0yq)
        assert calculated == expected

    def test_matrix_hex_2_0yt(self):
        expected = Point([ -x, -x+y, 4/3-z, 1])
        calculated = Point.calculate(mne._matrix_hex_2_0yt)
        assert calculated == expected

    def test_matrix_hex_2_0yH(self):
        expected = Point([ -x, -x+y, 2/3-z, 1])
        calculated = Point.calculate(mne._matrix_hex_2_0yH)
        assert calculated == expected

# TODO: potęgi maciezy = ID

