import Matrix.matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_m3_mxxmx:

    def test_matrix_m3_mxxmx(self):
        assert Point([-z, x, y, 1]).is_got_by(mne._matrix_m3_mxxmx)

    def test_matrix_m3_mhmxxmx_mqmqq(self):
        assert Point([-z, x, 1 + y, 1]).is_got_by(mne._matrix_m3_mhmxxmx_mqmqq)

    def test_matrix_m3_m1mxhxmx_mh0h(self):
        assert Point([-z, 1 + x, 1 + y, 1]).is_got_by(mne._matrix_m3_m1mxhxmx_mh0h)

    def test_matrix_m3_hmxhxmx_00h(self):
        assert Point([1 - z, x, 1 + y, 1]).is_got_by(mne._matrix_m3_hmxhxmx_00h)

    def test_matrix_m3_mhmx1xmx_0hh(self):
        assert Point([1 - z, 1 + x, y, 1]).is_got_by(mne._matrix_m3_mhmx1xmx_0hh)

    def test_matrix_m3_mxxmx_mqq3q(self):
        assert Point([1 - z, 1 + x, 1 + y, 1]).is_got_by(mne._matrix_m3_mxxmx_mqq3q)

    def test_matrix_m3_mhmx1xmx_o3o5o(self):
        assert Point([1.5 - z, 0.5 + x, 0.5 + y, 1]).is_got_by(
            mne._matrix_m3_mhmx1xmx_o3o5o
        )

    def test_matrix_m3_m1mx1xmx_m3o3o5o(self):
        assert Point([0.5 - z, 1.5 + x, 0.5 + y, 1]).is_got_by(
            mne._matrix_m3_m1mx1xmx_m3o3o5o
        )

    def test_matrix_m3_m1mxhxmx_m3omo5o(self):
        assert Point([0.5 - z, 0.5 + x, 1.5 + y, 1]).is_got_by(
            mne._matrix_m3_m1mxhxmx_m3omo5o
        )

    def test_matrix_m3_mhmxhxmx_m3o3oo(self):
        assert Point([1.5 - z, 1.5 + x, 1.5 + y, 1]).is_got_by(
            mne._matrix_m3_mhmxhxmx_m3o3oo
        )
