import numpy as np
import sympy as sp

import Crystal_Symmetry.krysztalki.workDir.Matrix.matrices_new_extended as mne
from Crystal_Symmetry.krysztalki.workDir.equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_3_mxmxx:

    def test_matrix_3_mxmxx(self):
        assert Point([-z, x, -y, 1]).is_got_by(mne._matrix_3_mxmxx)

    def test_matrix_3_2_tmxHmxx_HHmH(self):
        assert Point([1 - z, x, -y, 1]).is_got_by(mne._matrix_3_2_tmxHmxx_HHmH)

    def test_matrix_3_mxhmxx(self):
        assert Point([-z, 1 + x, 1 - y, 1]).is_got_by(mne._matrix_3_mxhmxx)

    def test_matrix_3_hmxhmxx(self):
        assert Point([1 - z, x, 1 - y, 1]).is_got_by(mne._matrix_3_hmxhmxx)

    def test_matrix_3_2_Hmxtmxx_ttmt(self):
        assert Point([1 - z, 1 + x, -y, 1]).is_got_by(mne._matrix_3_2_Hmxtmxx_ttmt)

    def test_matrix_3_2_tmx2tmxx_HHmH(self):
        assert Point([1 - z, 1 + x, 1 - y, 1]).is_got_by(mne._matrix_3_2_tmx2tmxx_HHmH)
