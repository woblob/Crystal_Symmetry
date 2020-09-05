# test_matrices_like_

import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_hex:

    def test_matrix_hex_m_0yz(self):
        expected = Point([ -x, -x+y, z, 1])
        calculated = Point.calculate(mne._matrix_hex_m_0yz)
        assert calculated == expected

    def test_matrix_hex_m_x0z(self):
        expected = Point([ x-y, -y, z, 1])
        calculated = Point.calculate(mne._matrix_hex_m_x0z)
        assert calculated == expected

    def test_matrix_hex_m_x2xz(self):
        expected = Point([ -x+y, y, z, 1])
        calculated = Point.calculate(mne._matrix_hex_m_x2xz)
        assert calculated == expected

    def test_matrix_hex_m_2xxz(self):
        expected = Point([ x, x-y, z, 1])
        calculated = Point.calculate(mne._matrix_hex_m_2xxz)
        assert calculated == expected

    def test_matrix_hex_2_x00(self):
        expected = Point([ x-y, -y, -z, 1])
        calculated = Point.calculate(mne._matrix_hex_2_x00)
        assert calculated == expected

    def test_matrix_hex_2_0y0(self):
        expected = Point([ -x, -x+y, -z, 1])
        calculated = Point.calculate(mne._matrix_hex_2_0y0)
        assert calculated == expected

    def test_matrix_hex_2_x2x0(self):
        expected = Point([ -x+y, y, -z, 1])
        calculated = Point.calculate(mne._matrix_hex_2_x2x0)
        assert calculated == expected

    def test_matrix_hex_2_2xx0(self):
        expected = Point([ x, x-y, -z, 1])
        calculated = Point.calculate(mne._matrix_hex_2_2xx0)
        assert calculated == expected

    def test_matrix_3_00z(self):
        expected = Point([ -y, x-y, z, 1])
        calculated = Point.calculate(mne._matrix_hex_3_00z)
        assert calculated == expected

    def test_matrix_m3_00z(self):
        expected = Point([ y, -x+y, -z, 1])
        calculated = Point.calculate(mne._matrix_hex_m3_00z)
        assert calculated == expected

    def test_matrix_6_00z(self):
        expected = Point([ x-y, x, z, 1])
        calculated = Point.calculate(mne._matrix_hex_6_00z)
        assert calculated == expected

    def test_matrix_m6_00z(self):
        expected = Point([ -x+y, -x, -z, 1])
        calculated = Point.calculate(mne._matrix_hex_m6_00z)
        assert calculated == expected
