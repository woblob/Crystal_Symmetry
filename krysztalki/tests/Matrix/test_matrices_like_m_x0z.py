import numpy as np
import sympy as sp

import Crystal_Symmetry.krysztalki.workDir.Matrix.matrices_new_extended as mne
from Crystal_Symmetry.krysztalki.workDir.equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Mirror_x0z:

    def test_matrix_m_x0z(self):
        assert Point([x, -y, z, 1]).is_got_by(mne._matrix_m_x0z)

    def test_matrix_c_xqz_00h(self):
        assert Point([x, 1 - y, 1 + z, 1]).is_got_by(mne._matrix_c_xqz_00h)

    def test_matrix_a_xqz_h00(self):
        assert Point([1 + x, 1 - y, z, 1]).is_got_by(mne._matrix_a_xqz_h00)

    def test_matrix_n_xqz_h0h(self):
        assert Point([1 + x, 1 - y, 1 + z, 1]).is_got_by(mne._matrix_n_xqz_h0h)

    def test_matrix_d_xoz_q0q(self):
        assert Point([0.5 + x, 0.5 - y, 0.5 + z, 1]).is_got_by(mne._matrix_d_xoz_q0q)

    def test_matrix_d_x3oz_q03q(self):
        assert Point([0.5 + x, 1.5 - y, 1.5 + z, 1]).is_got_by(mne._matrix_d_x3oz_q03q)

    def test_matrix_d_xoz_3q03q(self):
        assert Point([1.5 + x, 0.5 - y, 1.5 + z, 1]).is_got_by(mne._matrix_d_xoz_3q03q)

    def test_matrix_d_x3oz_3q0q(self):
        assert Point([1.5 + x, 1.5 - y, 0.5 + z, 1]).is_got_by(mne._matrix_d_x3oz_3q0q)

    def test_matrix_a_x0z_h00(self):
        assert Point([1 + x, -y, +z, 1]).is_got_by(mne._matrix_a_x0z_h00)

    def test_matrix_d_xoz_q03q(self):
        assert Point([0.5 + x, 0.5 - y, 1.5 + z, 1]).is_got_by(mne._matrix_d_xoz_q03q)

    def test_matrix_d_x3oz_q0q(self):
        assert Point([0.5 + x, 1.5 - y, 0.5 + z, 1]).is_got_by(mne._matrix_d_x3oz_q0q)

    def test_matrix_d_xoz_3q0q(self):
        assert Point([1.5 + x, 0.5 - y, 0.5 + z, 1]).is_got_by(mne._matrix_d_xoz_3q0q)

    def test_matrix_d_x3oz_3q03q(self):
        assert Point([1.5 + x, 1.5 - y, 1.5 + z, 1]).is_got_by(mne._matrix_d_x3oz_3q03q)
