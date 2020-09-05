import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Mirror_0yz:

    def test_matrix_m_0yz(self):
        expected = Point([ -x, y, z, 1])
        calculated = Point.calculate(mne._matrix_m_0yz)
        assert calculated == expected

    def test_matrix_c_0yz_00h(self):
        expected = Point([ -x, y, 1+z, 1])
        calculated = Point.calculate(mne._matrix_c_0yz_00h)
        assert calculated == expected

    def test_matrix_b_qyz(self):
        expected = Point([ 1-x, 1+y, z, 1])
        calculated = Point.calculate(mne._matrix_b_qyz_0h0)
        assert calculated == expected

    def test_matrix_d_oyz_0qq(self):
        expected = Point([ 0.5-x, 0.5+y, 0.5+z, 1])
        calculated = Point.calculate(mne._matrix_d_oyz_0qq)
        assert calculated == expected

    def test_matrix_d_3oyz_0qq(self):
        expected = Point([ 1.5-x, 0.5+y, 0.5+z, 1])
        calculated = Point.calculate(mne._matrix_d_3oyz_0qq)
        assert calculated == expected

    def test_matrix_d_oyz_03qq(self):
        expected = Point([ 0.5-x, 1.5+y, 0.5+z, 1])
        calculated = Point.calculate(mne._matrix_d_oyz_03qq)
        assert calculated == expected

    def test_matrix_d_oyz_0q3q(self):
        expected = Point([ 0.5-x, 0.5+y, 1.5+z, 1])
        calculated = Point.calculate(mne._matrix_d_oyz_0q3q)
        assert calculated == expected

    def test_matrix_d_oyz_03q3q(self):
        expected = Point([ 0.5-x, 1.5+y, 1.5+z, 1])
        calculated = Point.calculate(mne._matrix_d_oyz_03q3q)
        assert calculated == expected

    def test_matrix_d_3oyz_0q3q(self):
        expected = Point([ 1.5-x, 0.5+y, 1.5+z, 1])
        calculated = Point.calculate(mne._matrix_d_3oyz_0q3q)
        assert calculated == expected

    def test_matrix_d_3oyz_03qq(self):
        expected = Point([ 1.5-x, 1.5+y, 0.5+z, 1])
        calculated = Point.calculate(mne._matrix_d_3oyz_03qq)
        assert calculated == expected

    def test_matrix_d_3oyz_03q3q(self):
        expected = Point([ 1.5-x, 1.5+y, 1.5+z, 1])
        calculated = Point.calculate(mne._matrix_d_3oyz_03q3q)
        assert calculated == expected


class Test_Mirror_x0z:

    def test_matrix_m_x0z(self):
        expected = Point([x, -y, z, 1])
        calculated = Point.calculate(mne._matrix_m_x0z)
        assert calculated == expected

    def test_matrix_c_xqz_00h(self):
        expected = Point([x, 1 - y, 1 + z, 1])
        calculated = Point.calculate(mne._matrix_c_xqz_00h)
        assert calculated == expected

    def test_matrix_a_xqz_h00(self):
        expected = Point([1 + x, 1 - y, z, 1])
        calculated = Point.calculate(mne._matrix_a_xqz_h00)
        assert calculated == expected

    def test_matrix_n_xqz_h0h(self):
        expected = Point([1 + x, 1 - y, 1 + z, 1])
        calculated = Point.calculate(mne._matrix_n_xqz_h0h)
        assert calculated == expected

    def test_matrix_d_xoz_q0q(self):
        expected = Point([0.5 + x, 0.5 - y, 0.5 + z, 1])
        calculated = Point.calculate(mne._matrix_d_xoz_q0q)
        assert calculated == expected

    def test_matrix_d_x3oz_q03q(self):
        expected = Point([0.5 + x, 1.5 - y, 1.5 + z, 1])
        calculated = Point.calculate(mne._matrix_d_x3oz_q03q)
        assert calculated == expected

    def test_matrix_d_xoz_3q03q(self):
        expected = Point([1.5 + x, 0.5 - y, 1.5 + z, 1])
        calculated = Point.calculate(mne._matrix_d_xoz_3q03q)
        assert calculated == expected

    def test_matrix_d_x3oz_3q0q(self):
        expected = Point([1.5 + x, 1.5 - y, 0.5 + z, 1])
        calculated = Point.calculate(mne._matrix_d_x3oz_3q0q)
        assert calculated == expected

    def test_matrix_a_x0z_h00(self):
        expected = Point([1 + x, -y, +z, 1])
        calculated = Point.calculate(mne._matrix_a_x0z_h00)
        assert calculated == expected

    def test_matrix_d_xoz_q03q(self):
        expected = Point([0.5 + x, 0.5 - y, 1.5 + z, 1])
        calculated = Point.calculate(mne._matrix_d_xoz_q03q)
        assert calculated == expected

    def test_matrix_d_x3oz_q0q(self):
        expected = Point([0.5 + x, 1.5 - y, 0.5 + z, 1])
        calculated = Point.calculate(mne._matrix_d_x3oz_q0q)
        assert calculated == expected

    def test_matrix_d_xoz_3q0q(self):
        expected = Point([1.5 + x, 0.5 - y, 0.5 + z, 1])
        calculated = Point.calculate(mne._matrix_d_xoz_3q0q)
        assert calculated == expected

    def test_matrix_d_x3oz_3q03q(self):
        expected = Point([1.5 + x, 1.5 - y, 1.5 + z, 1])
        calculated = Point.calculate(mne._matrix_d_x3oz_3q03q)
        assert calculated == expected


class Test_Mirror_xy0:

    def test_matrix_m_xy0(self):
        expected = Point([x, y, -z, 1])
        calculated = Point.calculate(mne._matrix_m_xy0)
        assert calculated == expected

    def test_matrix_b_xy0_0h0(self):
        expected = Point([x, 1 + y, -z, 1])
        calculated = Point.calculate(mne._matrix_b_xy0_0h0)
        assert calculated == expected

    def test_matrix_b_xyq_0h0(self):
        expected = Point([x, 1 + y, 1 - z, 1])
        calculated = Point.calculate(mne._matrix_b_xyq_0h0)
        assert calculated == expected

    def test_matrix_a_xyq_h00(self):
        expected = Point([1 + x, y, 1 - z, 1])
        calculated = Point.calculate(mne._matrix_a_xyq_h00)
        assert calculated == expected

    def test_matrix_n_xy0_hh0(self):
        expected = Point([1 + x, 1 + y, -z, 1])
        calculated = Point.calculate(mne._matrix_n_xy0_hh0)
        assert calculated == expected

    def test_matrix_n_xyq_hh0(self):
        expected = Point([1 + x, 1 + y, 1 - z, 1])
        calculated = Point.calculate(mne._matrix_n_xyq_hh0)
        assert calculated == expected

    def test_matrix_d_xyo_qq0(self):
        expected = Point([0.5 + x, 0.5 + y, 0.5 - z, 1])
        calculated = Point.calculate(mne._matrix_d_xyo_qq0)
        assert calculated == expected

    def test_matrix_d_xyo_3qq0(self):
        expected = Point([1.5 + x, 0.5 + y, 0.5 - z, 1])
        calculated = Point.calculate(mne._matrix_d_xyo_3qq0)
        assert calculated == expected

    def test_matrix_d_xyo_q3q0(self):
        expected = Point([0.5 + x, 1.5 + y, 0.5 - z, 1])
        calculated = Point.calculate(mne._matrix_d_xyo_q3q0)
        assert calculated == expected

    def test_matrix_d_xy3o_qq0(self):
        expected = Point([0.5 + x, 0.5 + y, 1.5 - z, 1])
        calculated = Point.calculate(mne._matrix_d_xy3o_qq0)
        assert calculated == expected

    def test_matrix_d_xy3o_q3q0(self):
        expected = Point([0.5 + x, 1.5 + y, 1.5 - z, 1])
        calculated = Point.calculate(mne._matrix_d_xy3o_q3q0)
        assert calculated == expected

    def test_matrix_dxy3o_3qq0(self):
        expected = Point([1.5 + x, 0.5 + y, 1.5 - z, 1])
        calculated = Point.calculate(mne._matrix_dxy3o_3qq0)
        assert calculated == expected

    def test_matrix_d_xyo_3q3q0(self):
        expected = Point([1.5 + x, 1.5 + y, 0.5 - z, 1])
        calculated = Point.calculate(mne._matrix_d_xyo_3q3q0)
        assert calculated == expected

    def test_matrix_d_xy3o_3q3q0(self):
        expected = Point([1.5 + x, 1.5 + y, 1.5 - z, 1])
        calculated = Point.calculate(mne._matrix_d_xy3o_3q3q0)
        assert calculated == expected



class Test_Mirror_xmxz:

    def test_matrix_m_xmxz(self):
        expected = Point([ -y, -x, z, 1])
        calculated = Point.calculate(mne._matrix_m_xmxz)
        assert calculated == expected

    def test_matrix_n_qxmxz_qmq0(self):
        expected = Point([ 1-y, -x, z, 1])
        calculated = Point.calculate(mne._matrix_n_qxmxz_qmq0)
        assert calculated == expected

    def test_matrix_n_qxmxz_mqq0(self):
        expected = Point([ -y, 1-x, z, 1])
        calculated = Point.calculate(mne._matrix_n_qxmxz_mqq0)
        assert calculated == expected

    def test_matrix_c_xmxz_00h(self):
        expected = Point([ -y, -x, 1+z, 1])
        calculated = Point.calculate(mne._matrix_c_xmxz_00h)
        assert calculated == expected

    def test_matrix_c_hxmxz_00h(self):
        expected = Point([ 1-y, 1-x, 1+z, 1])
        calculated = Point.calculate(mne._matrix_c_hxmxz_00h)
        assert calculated == expected

    def test_matrix_d_hxmxz_qmqq(self):
        expected = Point([ 1.5-y, 0.5-x, 0.5+z, 1])
        calculated = Point.calculate(mne._matrix_d_hxmxz_qmqq)
        assert calculated == expected

    def test_matrix_d_hxmxz_mqq3q(self):
        expected = Point([ 0.5-y, 1.5-x, 1.5+z, 1])
        calculated = Point.calculate(mne._matrix_d_hxmxz_mqq3q)
        assert calculated == expected


class Test_Mirror_xymy:

    def test_matrix_m_xymy(self):
        expected = Point([ x, -z, -y, 1])
        calculated = Point.calculate(mne._matrix_m_xymy)
        assert calculated == expected

    def test_matrix_a_xymy_h00(self):
        expected = Point([ 1+x, -z, -y, 1])
        calculated = Point.calculate(mne._matrix_a_xymy_h00)
        assert calculated == expected

    def test_matrix_n_xqymy_0qmq(self):
        expected = Point([x, 1-z, -y, 1])
        calculated = Point.calculate(mne._matrix_n_xqymy_0qmq)
        assert calculated == expected

    def test_matrix_n_xmqyy_0qq(self):
        expected = Point([x, -z, 1-y, 1])
        calculated = Point.calculate(mne._matrix_n_xmqyy_0qq)
        assert calculated == expected

    def test_matrix_a_xhymy_h00(self):
        expected = Point([1+x, 1-z, 1-y, 1])
        calculated = Point.calculate(mne._matrix_a_xhymy_h00)
        assert calculated == expected

    def test_matrix_d_xhymy_3qmqq(self):
        expected = Point([1.5+x, 0.5-z, 1.5-y, 1])
        calculated = Point.calculate(mne._matrix_d_xhymy_3qmqq)
        assert calculated == expected


class Test_Mirror_xymx:

    def test_matrix_m_xymx(self):
        expected = Point([ -z, y, -x, 1])
        calculated = Point.calculate(mne._matrix_m_xymx)
        assert calculated == expected

    def test_matrix_n_qxymx_q0mq(self):
        expected = Point([ 1-z, y, -x, 1])
        calculated = Point.calculate(mne._matrix_n_qxymx_q0mq)
        assert calculated == expected

    def test_matrix_b_xymx_0h0(self):
        expected = Point([ -z, 1+y, -x, 1])
        calculated = Point.calculate(mne._matrix_b_xymx_0h0)
        assert calculated == expected

    def test_matrix_n_qxymx_mq0q(self):
        expected = Point([ -z, y, 1-x, 1])
        calculated = Point.calculate(mne._matrix_n_qxymx_mq0q)
        assert calculated == expected

    def test_matrix_b_hxymx_0h0(self):
        expected = Point([ 1-z, 1+y, 1-x, 1])
        calculated = Point.calculate(mne._matrix_b_hxymx_0h0)
        assert calculated == expected

    def test_matrix_d_hxymx_mqqq(self):
        expected = Point([ 0.5-z, 0.5+y, 1.5-x, 1])
        calculated = Point.calculate(mne._matrix_d_hxymx_mqqq)
        assert calculated == expected

    def test_matrix_d_hxymx_q3qmq(self):
        expected = Point([ 1.5-z, 1.5+y, 0.5-x, 1])
        calculated = Point.calculate(mne._matrix_d_hxymx_q3qmq)
        assert calculated == expected


class Test_Mirror_xyx:

    def test_matrix_m_xyx(self):
        expected = Point([ z, y, x, 1])
        calculated = Point.calculate(mne._matrix_m_xyx)
        assert calculated == expected

    def test_matrix_n_qxymx_q0q(self):
        expected = Point([ 1+z, y, x, 1])
        calculated = Point.calculate(mne._matrix_n_qxymx_q0q)
        assert calculated == expected

    def test_matrix_b_xyx_0h0(self):
        expected = Point([ z, 1+y, x, 1])
        calculated = Point.calculate(mne._matrix_b_xyx_0h0)
        assert calculated == expected

    def test_matrix_n_mqxyx_q0q(self):
        expected = Point([ z, y, 1+x, 1])
        calculated = Point.calculate(mne._matrix_n_mqxyx_q0q)
        assert calculated == expected

    def test_matrix_n_xyx_hhh(self):
        expected = Point([ 1+z, 1+y, 1+x, 1])
        calculated = Point.calculate(mne._matrix_n_xyx_hhh)
        assert calculated == expected

    def test_matrix_d_xyx_qqq(self):
        expected = Point([ 0.5+z, 0.5+y, 0.5+x, 1])
        calculated = Point.calculate(mne._matrix_d_xyx_qqq)
        assert calculated == expected

    def test_matrix_d_xyx_3q3q3q(self):
        expected = Point([ 1.5+z, 1.5+y, 1.5+x, 1])
        calculated = Point.calculate(mne._matrix_d_xyx_3q3q3q)
        assert calculated == expected


class Test_Mirror_xxz:

    def test_matrix_m_xxz(self):
        expected = Point([ y, x, z, 1])
        calculated = Point.calculate(mne._matrix_m_xxz)
        assert calculated == expected

    def test_matrix_n_qxxz_qq0(self):
        expected = Point([ 1+y, x, z, 1])
        calculated = Point.calculate(mne._matrix_n_qxxz_qq0)
        assert calculated == expected

    def test_matrix_n_mqxxz_qq0(self):
        expected = Point([ y, 1+x, z, 1])
        calculated = Point.calculate(mne._matrix_n_mqxxz_qq0)
        assert calculated == expected

    def test_matrix_c_xxz_00h(self):
        expected = Point([ y, x, 1+z, 1])
        calculated = Point.calculate(mne._matrix_c_xxz_00h)
        assert calculated == expected

    def test_matrix_n_xxz_hhh(self):
        expected = Point([ 1+y, 1+x, 1+z, 1])
        calculated = Point.calculate(mne._matrix_n_xxz_hhh)
        assert calculated == expected

    def test_matrix_d_xxz_qqq(self):
        expected = Point([ 0.5+y, 0.5+x, 0.5+z, 1])
        calculated = Point.calculate(mne._matrix_d_xxz_qqq)
        assert calculated == expected

    def test_matrix_d_xxz_3q3q3q(self):
        expected = Point([ 0.5+y, 0.5+x, 1.5+z, 1])
        calculated = Point.calculate(mne._matrix_d_xxz_3q3q3q)
        assert calculated == expected


class Test_Mirror_xyy:

    def test_matrix_m_xyy(self):
        expected = Point([ x, z, y, 1])
        calculated = Point.calculate(mne._matrix_m_xyy)
        assert calculated == expected

    def test_matrix_a_xyy_h00(self):
        expected = Point([1+x, z, y, 1])
        calculated = Point.calculate(mne._matrix_a_xyy_h00)
        assert calculated == expected

    def test_matrix_n_xqyy_0qq(self):
        expected = Point([x, 1+z, y, 1])
        calculated = Point.calculate(mne._matrix_n_xqyy_0qq)
        assert calculated == expected

    def test_matrix_n_xqymy_0mqq(self):
        expected = Point([x, z, 1+y, 1])
        calculated = Point.calculate(mne._matrix_n_xqymy_0mqq)
        assert calculated == expected

    def test_matrix_n_xyy_hhh(self):
        expected = Point([1+x, 1+z, 1+y, 1])
        calculated = Point.calculate(mne._matrix_n_xyy_hhh)
        assert calculated == expected

    def test_matrix_d_xyy_qqq(self):
        expected = Point([0.5+x, 0.5+z, 0.5+y, 1])
        calculated = Point.calculate(mne._matrix_d_xyy_qqq)
        assert calculated == expected

    def test_matrix_d_xhymy_qqmq(self):
        expected = Point([ 0.5+x, 1.5+z, 0.5+y, 1])
        calculated = Point.calculate(mne._matrix_d_xhymy_qqmq)
        assert calculated == expected

    def test_matrix_d_xyy_3q3q3q(self):
        expected = Point([ 1.5+x, 1.5+z, 1.5+y, 1])
        calculated = Point.calculate(mne._matrix_d_xyy_3q3q3q)
        assert calculated == expected
