import numpy as np
import sympy as sp

import Crystal_Symmetry.krysztalki.workDir.Matrix.matrices_new_extended as mne
from Crystal_Symmetry.krysztalki.workDir.equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_hex_2_0y0:

    def test_matrix_hex_2_0y0(self):
        assert Point([-x, -x + y, -z, 1]).is_got_by(mne._matrix_hex_2_0y0)
        # assert mne._matrix_hex_2_0y0 @ mne._matrix_hex_2_0y0

    def test_matrix_hex_2_0yq(self):
        assert Point([-x, -x + y, 1 - z, 1]).is_got_by(mne._matrix_hex_2_0yq)

    def test_matrix_hex_2_0yt(self):
        assert Point([-x, -x + y, 4 / 3 - z, 1]).is_got_by(mne._matrix_hex_2_0yt)

    def test_matrix_hex_2_0yH(self):
        assert Point([-x, -x + y, 2 / 3 - z, 1]).is_got_by(mne._matrix_hex_2_0yH)


# TODO: potęgi maciezy = ID
