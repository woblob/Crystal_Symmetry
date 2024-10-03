import numpy as np
import sympy as sp

import Matrix.matrices_new_extended as mne
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_3_mxxmx:

    def test_matrix_3_mxxmx(self):
        assert Point([z, -x, -y, 1]).is_got_by(mne._matrix_3_mxxmx)

    def test_matrix_3_2_mHmxtxmx_HmHH(self):
        assert Point([z, -x, 1 - y, 1]).is_got_by(mne._matrix_3_2_mHmxtxmx_HmHH)

    def test_matrix_3_mxhxmx(self):
        assert Point([z, 1 - x, 1 - y, 1]).is_got_by(mne._matrix_3_mxhxmx)

    def test_matrix_3_2_HmxHxmx_tmtt(self):
        assert Point([1 + z, -x, 1 - y, 1]).is_got_by(mne._matrix_3_2_HmxHxmx_tmtt)

    def test_matrix_3_hmxxmx(self):
        assert Point([1 + z, 1 - x, -y, 1]).is_got_by(mne._matrix_3_hmxxmx)

    def test_matrix_3_2_tmxtxmx_HmHH(self):
        assert Point([1 + z, 1 - x, 1 - y, 1]).is_got_by(mne._matrix_3_2_tmxtxmx_HmHH)
