import numpy as np
import sympy as sp

import Crystal_Symmetry.krysztalki.workDir.Matrix.matrices_new_extended as mne
from Crystal_Symmetry.krysztalki.workDir.equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_2_0yy:

    def test_matrix_2_0yy(self):
        assert Point([-x, z, y, 1]).is_got_by(mne._matrix_2_0yy)

    def test_matrix_2_qyy(self):
        assert Point([1 - x, z, y, 1]).is_got_by(mne._matrix_2_qyy)

    def test_matrix_2_1_0qyy_0qq(self):
        assert Point([-x, 1 + z, y, 1]).is_got_by(mne._matrix_2_1_0qyy_0qq)

    def test_matrix_2_0qyy_0qq(self):
        assert Point([-x, z, 1 + y, 1]).is_got_by(mne._matrix_2_0qyy_0qq)

    def test_matrix_2_1_qyy_0hh(self):
        assert Point([1 - x, 1 + z, 1 + y, 1]).is_got_by(mne._matrix_2_1_qyy_0hh)

    def test_matrix_2_1_3omqyy_0hh(self):
        assert Point([1.5 - x, 0.5 + z, 1.5 + y, 1]).is_got_by(
            mne._matrix_2_1_3omqyy_0hh
        )

    def test_matrix_2_1_oqyy_0hh(self):
        assert Point([0.5 - x, 1.5 + z, 0.5 + y, 1]).is_got_by(mne._matrix_2_1_oqyy_0hh)

    def test_matrix_2_1_oyy_0qq(self):
        assert Point([0.5 - x, 0.5 + z, 0.5 + y, 1]).is_got_by(mne._matrix_2_1_oyy_0qq)

    def test_matrix_2_1_oyy_03q3q(self):
        assert Point([0.5 - x, 1.5 + z, 1.5 + y, 1]).is_got_by(
            mne._matrix_2_1_oyy_03q3q
        )

    def test_matrix_2_1_3ohmyy_0mqq(self):
        assert Point([1.5 - x, 0.5 + z, 1.5 + y, 1]).is_got_by(
            mne._matrix_2_1_3ohmyy_0mqq
        )

    def test_matrix_2_1_3oqyy_0hh(self):
        assert Point([1.5 - x, 1.5 + z, 0.5 + y, 1]).is_got_by(
            mne._matrix_2_1_3oqyy_0hh
        )
