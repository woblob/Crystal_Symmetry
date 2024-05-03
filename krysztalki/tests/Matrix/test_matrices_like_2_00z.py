import numpy as np
import sympy as sp

import Crystal_Symmetry.krysztalki.workDir.Matrix.matrices_new_extended as mne
from Crystal_Symmetry.krysztalki.workDir.equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_2_00z:

    def test_matrix_2_00z(self):
        assert Point([-x, -y, z, 1]).is_got_by(mne._matrix_2_00z)

    def test_matrix_2_1_0qz_00h(self):
        assert Point([-x, 1 - y, 1 + z, 1]).is_got_by(mne._matrix_2_1_0qz_00h)

    def test_matrix_2_1_q0z_00h(self):
        assert Point([1 - x, -y, 1 + z, 1]).is_got_by(mne._matrix_2_1_q0z_00h)

    def test_matrix_2_qqz(self):
        assert Point([1 - x, 1 - y, z, 1]).is_got_by(mne._matrix_2_qqz)

    def test_matrix_2_1_qqz_00h(self):
        assert Point([1 - x, 1 - y, 1 + z, 1]).is_got_by(mne._matrix_2_1_qqz_00h)

    def test_matrix_2_0qz(self):
        assert Point([-x, 1 - y, z, 1]).is_got_by(mne._matrix_2_0qz)
