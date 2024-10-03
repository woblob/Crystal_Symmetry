import numpy as np
import sympy as sp

import Matrix.matrices_new_extended as mne
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_3_xxx:

    def test_matrix_3_xxx(self):
        assert Point([z, x, y, 1]).is_got_by(mne._matrix_3_xxx)

    def test_matrix_3_1_mtmHxx_ttt(self):
        assert Point([z, 1 + x, 1 + y, 1]).is_got_by(mne._matrix_3_1_mtmHxx_ttt)

    def test_matrix_3_1_HxmHxx_ttt(self):
        assert Point([1 + z, x, 1 + y, 1]).is_got_by(mne._matrix_3_1_HxmHxx_ttt)

    def test_matrix_3_1_Hxtxx_ttt(self):
        assert Point([1 + z, 1 + x, y, 1]).is_got_by(mne._matrix_3_1_Hxtxx_ttt)

    def test_matrix_3_xxx_hhh(self):
        assert Point([1 + z, 1 + x, 1 + y, 1]).is_got_by(mne._matrix_3_xxx_hhh)
