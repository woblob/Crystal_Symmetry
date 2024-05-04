import numpy as np
import sympy as sp

import Crystal_Symmetry.krysztalki.workDir.Matrix.matrices_new_extended as mne
from Crystal_Symmetry.krysztalki.workDir.equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_hex_m6_00z:

    def test_matrix_hex_m6_00z(self):
        assert Point([-x + y, -x, -z, 1]).is_got_by(mne._matrix_hex_m6_00z)
