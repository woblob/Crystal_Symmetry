import Matrix.matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_m3_xxx:

    def test_matrix_m3_xxx(self):
        assert Point([-z, -x, -y, 1]).is_got_by(mne._matrix_m3_xxx)

    def test_matrix_m3_xhxx_0h0(self):
        assert Point([-z, 1 - x, 1 - y, 1]).is_got_by(mne._matrix_m3_xhxx_0h0)

    def test_matrix_m3_mhxmhxx_00h(self):
        assert Point([1 - z, -x, 1 - y, 1]).is_got_by(mne._matrix_m3_mhxmhxx_00h)

    def test_matrix_m3_mhxxx_h00(self):
        assert Point([1 - z, 1 - x, -y, 1]).is_got_by(mne._matrix_m3_mhxxx_h00)

    def test_matrix_m3_xxx_qqq(self):
        assert Point([1 - z, 1 - x, 1 - y, 1]).is_got_by(mne._matrix_m3_xxx_qqq)

    def test_matrix_m3_xmhxx_3omo3o(self):
        assert Point([1.5 - z, 0.5 - x, 0.5 - y, 1]).is_got_by(
            mne._matrix_m3_xmhxx_3omo3o
        )

    def test_matrix_m3_hxhxx_3o3omo(self):
        assert Point([0.5 - z, 1.5 - x, 0.5 - y, 1]).is_got_by(
            mne._matrix_m3_hxhxx_3o3omo
        )

    def test_matrix_m3_mhxxx_mo3o3o(self):
        assert Point([0.5 - z, 0.5 - x, 1.5 - y, 1]).is_got_by(
            mne._matrix_m3_mhxxx_mo3o3o
        )

    def test_matrix_m3_xxx_3o3o3o(self):
        assert Point([1.5 - z, 1.5 - x, 1.5 - y, 1]).is_got_by(
            mne._matrix_m3_xxx_3o3o3o
        )
