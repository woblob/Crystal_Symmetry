import numpy as np
import sympy as sp

import Crystal_Symmetry.krysztalki.workDir.Matrix.matrices_new_extended as mne
from Crystal_Symmetry.krysztalki.workDir.equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_hex_2_xmx0_xx0:

    def test_matrix_hex_2_xxH(self):
        assert Point([y, x, 2 / 3 - z, 1]).is_got_by(mne._matrix_hex_2_xxH)

    def test_matrix_hex_2_xmxH(self):
        assert Point([-y, -x, 2 / 3 - z, 1]).is_got_by(mne._matrix_hex_2_xmxH)

    def test_matrix_hex_2_xmxt(self):
        assert Point([-y, -x, 4 / 3 - z, 1]).is_got_by(mne._matrix_hex_2_xmxt)

    def test_matrix_hex_2_xmx5v(self):
        assert Point([-y, -x, 5 / 3 - z, 1]).is_got_by(mne._matrix_hex_2_xmx5v)
