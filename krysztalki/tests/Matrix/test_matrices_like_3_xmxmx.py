import numpy as np
import sympy as sp

import Crystal_Symmetry.krysztalki.workDir.Matrix.matrices_new_extended as mne
from Crystal_Symmetry.krysztalki.workDir.equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_3_xmxmx:

    def test_matrix_3_xmxmx(self):
        assert Point([-z, -x, y, 1]).is_got_by(mne._matrix_3_xmxmx)

    def test_matrix_3_2_txmHmxmx_mttt(self):
        assert Point([-z, 1 - x, 1 + y, 1]).is_got_by(mne._matrix_3_2_txmHmxmx_mttt)

    def test_matrix_3_hxmhmxmx(self):
        assert Point([1 - z, -x, 1 + y, 1]).is_got_by(mne._matrix_3_hxmhmxmx)

    def test_matrix_3_hxmxmx(self):
        assert Point([1 - z, 1 - x, y, 1]).is_got_by(mne._matrix_3_hxmxmx)

    def test_matrix_3_2_2txmtmxmx_mHHH(self):
        assert Point([1 - z, 1 - x, 1 + y, 1]).is_got_by(mne._matrix_3_2_2txmtmxmx_mHHH)

    def test_matrix_3_2_HxHmxmx_mHHH(self):
        assert Point([-z, 1 - x, y, 1]).is_got_by(mne._matrix_3_2_HxHmxmx_mHHH)
