import numpy as np
import sympy as sp

import Matrix.matrices_new_extended as mne
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_2_0y0:

    def test_matrix_2_0y0(self):
        assert Point([-x, y, -z, 1]).is_got_by(mne._matrix_2_0y0)

    def test_matrix_2_qy0(self):
        assert Point([1 - x, y, -z, 1]).is_got_by(mne._matrix_2_qy0)

    def test_matrix_2_1_0yq_0h0(self):
        assert Point([-x, 1 + y, 1 - z, 1]).is_got_by(mne._matrix_2_1_0yq_0h0)

    def test_matrix_2_qyq(self):
        assert Point([1 - x, y, 1 - z, 1]).is_got_by(mne._matrix_2_qyq)

    def test_matrix_2_1_qy0_0h0(self):
        assert Point([1 - x, 1 + y, -z, 1]).is_got_by(mne._matrix_2_1_qy0_0h0)

    def test_matrix_2_1_qyq_0h0(self):
        assert Point([1 - x, 1 + y, 1 - z, 1]).is_got_by(mne._matrix_2_1_qyq_0h0)

    # def test_matrix_2_0y0_0h0_out(self):
    #   assert Point([-x, 1 + y, -z, 1]).is_got_by(mne._matrix_2_0y0)
    #
    # def test_matrix_2_0y0_00h_out(self):
    #   assert Point([-x, y, 1 - z, 1]).is_got_by(mne._matrix_2_0y0)
