import numpy as np
import sympy as sp

import Crystal_Symmetry.krysztalki.workDir.Matrix.matrices_new_extended as mne
from Crystal_Symmetry.krysztalki.workDir.equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_hex_2_x2x0:

    def test_matrix_hex_2_x2x0(self):
        assert Point([-x + y, y, -z, 1]).is_got_by(mne._matrix_hex_2_x2x0)

    def test_matrix_hex_2_x2xH(self):
        assert Point([-x + y, y, 2 / 3 - z, 1]).is_got_by(mne._matrix_hex_2_x2xH)

    def test_matrix_hex_2_x2xq(self):
        assert Point([-x + y, y, 3 / 3 - z, 1]).is_got_by(mne._matrix_hex_2_x2xq)

    def test_matrix_hex_2_x2xt(self):
        assert Point([-x + y, y, 4 / 3 - z, 1]).is_got_by(mne._matrix_hex_2_x2xt)
