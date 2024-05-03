import numpy as np
import sympy as sp

import Crystal_Symmetry.krysztalki.workDir.Matrix.matrices_new_extended as mne
from Crystal_Symmetry.krysztalki.workDir.equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_hex_2_2xx0:

    def test_matrix_hex_2_2xx0(self):
        assert Point([x, x - y, -z, 1]).is_got_by(mne._matrix_hex_2_2xx0)

    def test_matrix_hex_2_2xxq(self):
        assert Point([x, x - y, 3 / 3 - z, 1]).is_got_by(mne._matrix_hex_2_2xxq)

    def test_matrix_2_2xxv(self):
        assert Point([x, x - y, 1 / 3 - z, 1]).is_got_by(mne._matrix_hex_2_2xxv)
