# test_matrices_like_

import numpy as np
import sympy as sp

import Crystal_Symmetry.krysztalki.workDir.Matrix.matrices_new_extended as mne
from Crystal_Symmetry.krysztalki.workDir.equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_hex:

    def test_matrix_hex_m_0yz(self):
        assert Point([-x, -x + y, z, 1]).is_got_by(mne._matrix_hex_m_0yz)

    def test_matrix_hex_m_x0z(self):
        assert Point([x - y, -y, z, 1]).is_got_by(mne._matrix_hex_m_x0z)

    def test_matrix_hex_m_x2xz(self):
        assert Point([-x + y, y, z, 1]).is_got_by(mne._matrix_hex_m_x2xz)

    def test_matrix_hex_m_2xxz(self):
        assert Point([x, x - y, z, 1]).is_got_by(mne._matrix_hex_m_2xxz)

    def test_matrix_hex_2_x00(self):
        assert Point([x - y, -y, -z, 1]).is_got_by(mne._matrix_hex_2_x00)

    def test_matrix_hex_2_0y0(self):
        assert Point([-x, -x + y, -z, 1]).is_got_by(mne._matrix_hex_2_0y0)

    def test_matrix_hex_2_x2x0(self):
        assert Point([-x + y, y, -z, 1]).is_got_by(mne._matrix_hex_2_x2x0)

    def test_matrix_hex_2_2xx0(self):
        assert Point([x, x - y, -z, 1]).is_got_by(mne._matrix_hex_2_2xx0)

    def test_matrix_3_00z(self):
        assert Point([-y, x - y, z, 1]).is_got_by(mne._matrix_hex_3_00z)

    def test_matrix_m3_00z(self):
        assert Point([y, -x + y, -z, 1]).is_got_by(mne._matrix_hex_m3_00z)

    def test_matrix_6_00z(self):
        assert Point([x - y, x, z, 1]).is_got_by(mne._matrix_hex_6_00z)

    def test_matrix_m6_00z(self):
        assert Point([-x + y, -x, -z, 1]).is_got_by(mne._matrix_hex_m6_00z)
