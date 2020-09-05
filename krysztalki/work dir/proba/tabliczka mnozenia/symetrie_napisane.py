import numpy as np
import podstawa as pod
# import symetrie_napisane_hex as HEX
#  Fm-3c
_matrix_4_xmqq = pod.matrices_dict["4_x00"] + pod._translation_00h #13=14
_matrix_2_0qmyy_0mqq = pod.matrices_dict["2_0myy"] + pod._translation_00h #15
_matrix_2_0qyy_0qq = pod.matrices_dict["2_0yy"] + pod._translation_00h #16
_matrix_4_qyq = pod.matrices_dict["4_0y0"] + pod._translation_00h  #17=18
_matrix_2_1_qmx0x_mq0q = pod.matrices_dict["2_mx0x"] + pod._translation_00h  #19
_matrix_2_1_mqx0x_q0q = pod.matrices_dict["2_x0x"] + pod._translation_00h  #20
_matrix_4_2_00z_00h = pod.matrices_dict["4_00z"] + pod._translation_00h  #21=22
_matrix_2_xmxq = pod.matrices_dict["2_xmx0"] + pod._translation_00h  #23
_matrix_2_xxq = pod.matrices_dict["2_xx0"] + pod._translation_00h  #24
_matrix_m4_xqq_0qq = pod.matrices_dict["-4_x00"] + pod._translation_00h  # 37=38
_matrix_n_xmqyy_0qq = pod.matrices_dict["m_xymy"] + pod._translation_00h  #39
_matrix_n_xqymy_0mqq = pod.matrices_dict["m_xyy"] + pod._translation_00h  #40
_matrix_m4_mqyq_mq0q = pod.matrices_dict["-4_0y0"] + pod._translation_00h  #41=42
_matrix_n_mqxyx_q0q = pod.matrices_dict["m_xyx"] + pod._translation_00h  #43
_matrix_n_qxymx_mq0q = pod.matrices_dict["m_xymx"] + pod._translation_00h  #44
_matrix_m4_00z_00q = pod.matrices_dict["-4_00z"] + pod._translation_00h  #45=46
_matrix_c_xxz_00h = pod.matrices_dict["m_xxz"] + pod._translation_00h  #47
_matrix_c_xmxz_00h = pod.matrices_dict["m_xmxz"] + pod._translation_00h  #48

# tA [0,h,h]

_matrix_2_xqq = pod.matrices_dict["2_x00"] + pod._translation_0hh  #50
_matrix_2_1_0yq_0h0 = pod.matrices_dict["2_0y0"] + pod._translation_0hh  #51
_matrix_2_1_0qz_00h = pod.matrices_dict["2_00z"] + pod._translation_0hh  #52
_matrix_3_1_mtmHxx_ttt = pod.matrices_dict["3_xxx"] + pod._translation_0hh  #53=57
_matrix_3_2_txmHmxmx_mttt = pod.matrices_dict["3_xmxmx"] + pod._translation_0hh  #54=58
_matrix_3_mxhxmx = pod.matrices_dict["3_mxxmx"] + pod._translation_0hh  #55=59

_matrix_4_xqq = pod.matrices_dict["4_x00"] + pod._translation_0h0  #61=62
_matrix_2_1_0qmyy_0qmq = pod.matrices_dict["2_0myy"] + pod._translation_0h0  #63
_matrix_2_1_0qyy_0qq = pod.matrices_dict["2_0yy"] + pod._translation_0h0  #64
_matrix_4_2_0y0_0h0 = pod.matrices_dict["4_0y0"] + pod._translation_0h0  #65=66
_matrix_2_mxqx = pod.matrices_dict["2_mx0x"] + pod._translation_0h0  #67
_matrix_2_xqx = pod.matrices_dict["2_x0x"] + pod._translation_0h0  #68
_matrix_4_mqqz = pod.matrices_dict["4_00z"] + pod._translation_0h0  #69=70
_matrix_2_1_xqmx0_mqq0 = pod.matrices_dict["2_xmx0"] + pod._translation_0h0  #71
_matrix_2_1_xqx0_qq0 = pod.matrices_dict["2_xx0"] + pod._translation_0h0  #72

_matrix_inv_0qq = pod.matrices_dict["inv_000"] + pod._translation_0hh  #73
_matrix_n_0yz_0hh = pod.matrices_dict["m_0yz"] + pod._translation_0hh  #74
_matrix_c_xqz_00h = pod.matrices_dict["m_x0z"] + pod._translation_0hh  #75
_matrix_b_xyq_0h0 = pod.matrices_dict["m_xy0"] + pod._translation_0hh  #76
_matrix_m3_xhxx_0h0 = pod.matrices_dict["m3_xxx"] + pod._translation_0hh  #77=81
_matrix_m3_xhmxmx_0h0 = pod.matrices_dict["m3_xmxmx"] + pod._translation_0hh  #78=82
_matrix_m3_m1mxhxmx_mh0h = pod.matrices_dict["m3_mxxmx"] + pod._translation_0hh  #79=83
_matrix_m3_1mxhmxx_h0h = pod.matrices_dict["m3_mxmxx"] + pod._translation_0hh  #80=84

_matrix_m4_xqmq_0qmq = pod.matrices_dict["-4_x00"] + pod._translation_0h0  #85=86
_matrix_n_xqyy_0qq = pod.matrices_dict["m_xyy"] + pod._translation_0h0  #87
_matrix_n_xqymy_0qmq = pod.matrices_dict["m_xymy"] + pod._translation_0h0  #88
_matrix_m4_0y0_0q0 = pod.matrices_dict["-4_0y0"] + pod._translation_0h0  #89=90
_matrix_b_xyx_0h0 = pod.matrices_dict["m_xyx"] + pod._translation_0h0  #91
_matrix_b_xymx_0h0 = pod.matrices_dict["m_xymx"] + pod._translation_0h0  #92
_matrix_n_mqxxz_qq0 = pod.matrices_dict["m_xxz"] + pod._translation_0h0  #95
_matrix_n_qxmxz_mqq0 = pod.matrices_dict["m_xmxz"] + pod._translation_0h0  #96


# tB [h,0,h]  #97
_matrix_2_1_x0q_h00 = pod.matrices_dict["2_x00"] + pod._translation_h0h  #98
_matrix_2_qyq = pod.matrices_dict["2_0y0"] + pod._translation_h0h  #99
_matrix_2_1_q0z_00h = pod.matrices_dict["2_00z"] + pod._translation_h0h  #100
_matrix_3_1_HxmHxx_ttt = pod.matrices_dict["3_xxx"] + pod._translation_h0h  #101=105
_matrix_3_hxmhmxmx = pod.matrices_dict["3_xmxmx"] + pod._translation_h0h  #102=106
_matrix_3_2_HmxHxmx_tmtt = pod.matrices_dict["3_mxxmx"] + pod._translation_h0h  #103=107
_matrix_3_hmxhmxx = pod.matrices_dict["3_mxmxx"] + pod._translation_h0h  #104=108

_matrix_4_2_x00_h00 = pod.matrices_dict["4_x00"] + pod._translation_h00  #109=110
_matrix_2_qmyy = pod.matrices_dict["2_0myy"] + pod._translation_h00  #111
_matrix_2_qyy = pod.matrices_dict["2_0yy"] + pod._translation_h00  #112
_matrix_4_qymq = pod.matrices_dict["4_0y0"] + pod._translation_h00  #113=114
_matrix_2_1_qmx0x_q0mq = pod.matrices_dict["2_mx0x"] + pod._translation_h00  #115
_matrix_2_1_qx0x_q0mq = pod.matrices_dict["2_x0x"] + pod._translation_h00  #116
_matrix_4_qqz = pod.matrices_dict["4_00z"] + pod._translation_h00  #117=118
_matrix_2_1_xqmx0_qmq0 = pod.matrices_dict["2_xmx0"] + pod._translation_h00  #119
_matrix_2_1_xmqx0_qq0 = pod.matrices_dict["2_xx0"] + pod._translation_h00  #120

_matrix_inv_q0q = pod.matrices_dict["inv_000"] + pod._translation_h0h  #121
_matrix_n_qyz_00h = pod.matrices_dict["m_0yz"] + pod._translation_h0h  #122
_matrix_n_x0z_h0h = pod.matrices_dict["m_x0z"] + pod._translation_h0h  #123
_matrix_a_xyq_h00 = pod.matrices_dict["m_xy0"] + pod._translation_h0h  #124
_matrix_m3_mhxmhxx_00h = pod.matrices_dict["m3_xxx"] + pod._translation_h0h  #125=129
_matrix_m3_hxhmxmx_hh0 = pod.matrices_dict["m3_xmxmx"] + pod._translation_h0h  #126=130
_matrix_m3_hmxhxmx_00h = pod.matrices_dict["m3_mxxmx"] + pod._translation_h0h  #127=131
_matrix_m3_hmxmhmxx_hmh0 = pod.matrices_dict["m3_mxmxx"] + pod._translation_h0h #128=132

_matrix_m4_x00_q00 = pod.matrices_dict["-4_x00"] + pod._translation_h00  #133=134
_matrix_a_xyy_h00 = pod.matrices_dict["m_xyy"] + pod._translation_h00  #135
_matrix_a_xymy_h00 = pod.matrices_dict["m_xymy"] + pod._translation_h00  #136
_matrix_m4_qyq_q0q = pod.matrices_dict["-4_0y0"] + pod._translation_h00  #137=138
_matrix_n_qxymx_q0q = pod.matrices_dict["m_xyx"] + pod._translation_h00  #139
_matrix_n_qxymx_q0mq = pod.matrices_dict["m_xymx"] + pod._translation_h00  #140
_matrix_m4_qmqz_qmq0 = pod.matrices_dict["-4_00z"] + pod._translation_h00  #141=142
_matrix_n_qxxz_qq0 = pod.matrices_dict["m_xxz"] + pod._translation_h00  #143
_matrix_n_qxmxz_qmq0 = pod.matrices_dict["m_xmxz"] + pod._translation_h00 #144


# tC [h,h,0]  #145
_matrix_2_1_xq0_h00 = pod.matrices_dict["2_x00"] + pod._translation_hh0  #146
_matrix_2_1_qy0_0h0 = pod.matrices_dict["2_0y0"] + pod._translation_hh0  #147
_matrix_2_qqz = pod.matrices_dict["2_00z"] + pod._translation_hh0  #148

_matrix_3_1_Hxtxx_ttt = pod.matrices_dict["3_xxx"] + pod._translation_hh0  #149=153
_matrix_3_hxmxmx = pod.matrices_dict["3_xmxmx"] + pod._translation_hh0  #150=154
_matrix_3_hmxxmx = pod.matrices_dict["3_mxxmx"] + pod._translation_hh0  #151=155
_matrix_3_2_Hmxtmxx_ttmt = pod.matrices_dict["3_mxmxx"] + pod._translation_hh0  #152=156

_matrix_4_2_x0h_h00 = pod.matrices_dict["4_x00"] + pod._translation_hhh  #157=158
_matrix_2_qhmyy = pod.matrices_dict["2_0myy"] + pod._translation_hhh  #159
_matrix_2_1_qyy_0hh = pod.matrices_dict["2_0yy"] + pod._translation_hhh  #160 dupa
_matrix_4_qy0_0h0 = pod.matrices_dict["4_0y0"] + pod._translation_hhh  #161=162
_matrix_2_hmxqx = pod.matrices_dict["2_mx0x"] + pod._translation_hhh  #163
_matrix_2_1_xqx_q0q = pod.matrices_dict["2_x0x"] + pod._translation_hhh  #164
_matrix_4_2_0hz_00h = pod.matrices_dict["4_00z"] + pod._translation_hhh  #165=166
_matrix_2_xhmxq = pod.matrices_dict["2_xmx0"] + pod._translation_hhh  #167
_matrix_2_1_xxq_hh0 = pod.matrices_dict["2_xx0"] + pod._translation_hhh  #168

_matrix_inv_qq0 = pod.matrices_dict["inv_000"] + pod._translation_hh0  #169
_matrix_b_qyz_0h0 = pod.matrices_dict["m_0yz"] + pod._translation_hh0  #170
_matrix_a_xqz_h00 = pod.matrices_dict["m_x0z"] + pod._translation_hh0  #171
_matrix_n_xy0_hh0 = pod.matrices_dict["m_xy0"] + pod._translation_hh0  #172
_matrix_m3_mhxxx_h00 = pod.matrices_dict["m3_xxx"] + pod._translation_hh0  #173=177
_matrix_m3_mhx1mxmx_0hmh = pod.matrices_dict["m3_xmxmx"] + pod._translation_hh0 #174=178
_matrix_m3_mhmx1xmx_0hh = pod.matrices_dict["m3_mxxmx"] + pod._translation_hh0  #175=179
_matrix_m3_hmxmxx_h00 = pod.matrices_dict["m3_mxmxx"] + pod._translation_hh0 #176=180

_matrix_m4_xh0_qh0 = pod.matrices_dict["-4_x00"] + pod._translation_hhh  #181=182
_matrix_n_xyy_hhh = pod.matrices_dict["m_xyy"] + pod._translation_hhh  #183
_matrix_a_xhymy_h00 = pod.matrices_dict["m_xymy"] + pod._translation_hhh  #184
_matrix_m4_0yh_0qh = pod.matrices_dict["-4_0y0"] + pod._translation_hhh  #185=186
_matrix_n_xyx_hhh = pod.matrices_dict["m_xyx"] + pod._translation_hhh  #187
_matrix_b_hxymx_0h0 = pod.matrices_dict["m_xymx"] + pod._translation_hhh  #188
_matrix_m4_h0z_h0q = pod.matrices_dict["-4_00z"] + pod._translation_hhh  #189=190
_matrix_n_xxz_hhh = pod.matrices_dict["m_xxz"] + pod._translation_hhh  #191
_matrix_c_hxmxz_00h = pod.matrices_dict["m_xmxz"] + pod._translation_hhh #192


# Im-3m

# tI [h,h,h]

_matrix_2_1_xqq_h00 = pod.matrices_dict["2_x00"] + pod._translation_hhh  #50
_matrix_2_1_qyq_0h0 = pod.matrices_dict["2_0y0"] + pod._translation_hhh  #51
_matrix_2_1_qqz_00h = pod.matrices_dict["2_00z"] + pod._translation_hhh  #52
_matrix_3_xxx_hhh = pod.matrices_dict["3_xxx"] + pod._translation_hhh  #53=57
_matrix_3_2_2txmtmxmx_mHHH = pod.matrices_dict["3_xmxmx"] + pod._translation_hhh  #54=58
_matrix_3_2_tmxtxmx_HmHH = pod.matrices_dict["3_mxxmx"] + pod._translation_hhh  #55=59
_matrix_3_2_tmx2tmxx_HHmH = pod.matrices_dict["3_mxmxx"] + pod._translation_hhh  #56=60
_matrix_inv_qqq = pod.matrices_dict["inv_000"] + pod._translation_hhh  #73
_matrix_n_qyz_0hh = pod.matrices_dict["m_0yz"] + pod._translation_hhh  #74
_matrix_n_xqz_h0h = pod.matrices_dict["m_x0z"] + pod._translation_hhh  #75
_matrix_n_xyq_hh0 = pod.matrices_dict["m_xy0"] + pod._translation_hhh  #76
_matrix_m3_xxx_qqq = pod.matrices_dict["m3_xxx"] + pod._translation_hhh  #77=81
_matrix_m3_xmxmx_q3qmq = pod.matrices_dict["m3_xmxmx"] + pod._translation_hhh  #78=82
_matrix_m3_mxxmx_mqq3q = pod.matrices_dict["m3_mxxmx"] + pod._translation_hhh  #79=83
_matrix_m3_mxmxx_3qmqq = pod.matrices_dict["m3_mxmxx"] + pod._translation_hhh  #80=84


# Fddd

_matrix_d_oyz_0qq = pod.matrices_dict["m_0yz"] + pod._translation_qqq
_matrix_d_xoz_q0q = pod.matrices_dict["m_x0z"] + pod._translation_qqq
_matrix_d_xyo_qq0 = pod.matrices_dict["m_xy0"] + pod._translation_qqq
_matrix_inv_ooo   = pod.matrices_dict["inv_000"] + pod._translation_qqq

_matrix_d_oyz_03q3q = pod.matrices_dict["m_0yz"] + pod._translation_qqq + pod._translation_0hh
_matrix_d_x3oz_q03q = pod.matrices_dict["m_x0z"] + pod._translation_qqq + pod._translation_0hh
_matrix_d_xy3o_q3q0 = pod.matrices_dict["m_xy0"] + pod._translation_qqq + pod._translation_0hh
_matrix_inv_o3o3o   = pod.matrices_dict["inv_000"] + pod._translation_qqq + pod._translation_0hh

_matrix_d_3oyz_0q3q = pod.matrices_dict["m_0yz"] + pod._translation_qqq + pod._translation_h0h
_matrix_d_xoz_3q03q = pod.matrices_dict["m_x0z"] + pod._translation_qqq + pod._translation_h0h
_matrix_dxy3o_3qq0  = pod.matrices_dict["m_xy0"] + pod._translation_qqq + pod._translation_h0h
_matrix_inv_3oo3o   = pod.matrices_dict["inv_000"] + pod._translation_qqq + pod._translation_h0h

_matrix_d_3oyz_03qq = pod.matrices_dict["m_0yz"] + pod._translation_qqq + pod._translation_hh0
_matrix_d_x3oz_3q0q = pod.matrices_dict["m_x0z"] + pod._translation_qqq + pod._translation_hh0
_matrix_d_xyo_3q3q0 = pod.matrices_dict["m_xy0"] + pod._translation_qqq + pod._translation_hh0
_matrix_inv_3o3oo   = pod.matrices_dict["inv_000"] + pod._translation_qqq + pod._translation_hh0


#Ia-3d

_matrix_2_x0q = pod.matrices_dict["2_x00"] + pod._translation_00h  #2
_matrix_2_qy0 = pod.matrices_dict["2_0y0"] + pod._translation_h00  #3
_matrix_2_0qz = pod.matrices_dict["2_00z"] + pod._translation_0h0  #4

_matrix_3_2_HxHmxmx_mHHH = pod.matrices_dict["3_xmxmx"] + pod._translation_0h0  #6=10
_matrix_3_2_mHmxtxmx_HmHH = pod.matrices_dict["3_mxxmx"] + pod._translation_00h  #7=11
_matrix_3_2_tmxHmxx_HHmH = pod.matrices_dict["3_mxmxx"] + pod._translation_h00  #8=12

_matrix_4_1_xmqh_q00 = pod.matrices_dict["4_x00"] + pod._translation_qqq + pod._translation_00h  #13=14
_matrix_2_oqmyy = pod.matrices_dict["2_0myy"] + pod._translation_qqq  #15
_matrix_2_1_3omqyy_0hh = pod.matrices_dict["2_0yy"] + pod._translation_qqq + pod._translation_h0h  #16
_matrix_4_3_hyq_03q0 = pod.matrices_dict["4_0y0"] + pod._translation_qqq + pod._translation_0hh  #17
_matrix_2_qmxox = pod.matrices_dict["2_mx0x"] + pod._translation_qqq  #19
_matrix_2_1_qx3ox_h0h = pod.matrices_dict["2_x0x"] + pod._translation_qqq + pod._translation_hh0  #20
_matrix_4_3_qhz_003q = pod.matrices_dict["4_00z"] + pod._translation_qqq + pod._translation_h0h  #21
_matrix_2_xqmxo = pod.matrices_dict["2_xmx0"] + pod._translation_qqq  #23
_matrix_2_1_xmqxo_hh0 = pod.matrices_dict["2_xx0"] + pod._translation_qqq + pod._translation_h00  #24
_matrix_c_0yz_00h = pod.matrices_dict["m_0yz"] + pod._translation_00h  #26
_matrix_a_x0z_h00 = pod.matrices_dict["m_x0z"] + pod._translation_h00  #27
_matrix_b_xy0_0h0 = pod.matrices_dict["m_xy0"] + pod._translation_0h0  #28
_matrix_m3_mhxhmxmx_mqqmq = pod.matrices_dict["m3_xmxmx"] + pod._translation_0h0  #30=34
_matrix_m3_mhmxxmx_mqmqq = pod.matrices_dict["m3_mxxmx"] + pod._translation_00h  #31=35
_matrix_m3_mxmhmxx_qmqmq = pod.matrices_dict["m3_mxmxx"] + pod._translation_h00  #32=36
_matrix_m4_xhq_ohq = pod.matrices_dict["-4_x00"] + pod._translation_qqq + pod._translation_00h  #37=38
_matrix_d_xyy_qqq = pod.matrices_dict["m_xyy"] + pod._translation_qqq  #39
_matrix_d_xhymy_3qmqq = pod.matrices_dict["m_xymy"] + pod._translation_qqq + pod._translation_h0h  #40
_matrix_m4_mqyh_mq3oh = pod.matrices_dict["-4_0y0"] + pod._translation_qqq + pod._translation_0hh  #41=42
_matrix_d_xyx_qqq = pod.matrices_dict["m_xyx"] + pod._translation_qqq  #43
_matrix_d_hxymx_q3qmq = pod.matrices_dict["m_xymx"] + pod._translation_qqq + pod._translation_hh0  #44
_matrix_m4_hmqz_hmq3o = pod.matrices_dict["-4_00z"] + pod._translation_qqq + pod._translation_h0h  #45=46
_matrix_d_xxz_qqq = pod.matrices_dict["m_xxz"] + pod._translation_qqq  #47
_matrix_d_hxmxz_qmqq = pod.matrices_dict["m_xmxz"] + pod._translation_qqq + pod._translation_h00  #48

# tI[h,h,h]
_matrix_3_mxhmxx = pod.matrices_dict["3_mxmxx"] + pod._translation_0hh  #56=60
_matrix_4_3_xqh_3q00 = pod.matrices_dict["4_x00"] + pod._translation_qqq + pod._translation_hh0  #61
_matrix_2_3o3qmyy = pod.matrices_dict["2_0myy"] + pod._translation_qqq + pod._translation_hhh  #63
_matrix_2_1_oqyy_0hh = pod.matrices_dict["2_0yy"] + pod._translation_qqq + pod._translation_0h0  #64
_matrix_4_1_hymq_0q0 = pod.matrices_dict["4_0y0"] + pod._translation_qqq + pod._translation_h00  #65
_matrix_2_3qmx3ox = pod.matrices_dict["2_mx0x"] + pod._translation_qqq + pod._translation_hhh  #67
_matrix_2_1_mqxox_h0h = pod.matrices_dict["2_x0x"] + pod._translation_qqq + pod._translation_00h  #68
_matrix_4_1_mqhz_00q = pod.matrices_dict["4_00z"] + pod._translation_qqq + pod._translation_0h0  #69
_matrix_2_x3qmx3o = pod.matrices_dict["2_xmx0"] + pod._translation_qqq + pod._translation_hhh  #71
_matrix_2_1_xqx3o_hh0 = pod.matrices_dict["2_xx0"] + pod._translation_qqq + pod._translation_0hh  #72
_matrix_m4_xhmq_3ohmq = pod.matrices_dict["-4_x00"] + pod._translation_qqq + pod._translation_hh0  #85
_matrix_d_xyy_3q3q3q = pod.matrices_dict["m_xyy"] + pod._translation_qqq + pod._translation_hhh  #87
_matrix_d_xhymy_qqmq = pod.matrices_dict["m_xyy"] + pod._translation_qqq + pod._translation_0h0  #88
_matrix_m4_qyh_qoh = pod.matrices_dict["-4_0y0"] + pod._translation_qqq + pod._translation_h00  #89
_matrix_d_xyx_3q3q3q = pod.matrices_dict["m_xyx"] + pod._translation_qqq + pod._translation_hhh  #91
_matrix_d_hxymx_mqqq = pod.matrices_dict["m_xymx"] + pod._translation_qqq + pod._translation_00h  #92
_matrix_m4_hqz_hqo = pod.matrices_dict["-4_00z"] + pod._translation_qqq + pod._translation_0h0  #93
_matrix_d_xxz_3q3q3q = pod.matrices_dict["m_xxz"] + pod._translation_qqq + pod._translation_00h  #95
_matrix_d_hxmxz_mqq3q = pod.matrices_dict["m_xmxz"] + pod._translation_qqq + pod._translation_0hh  #96

# Fd-3c

_matrix_4_1_x0q_q00 = pod.matrices_dict["4_x00"] + pod._translation_qqq  #13
_matrix_2_1_oyy_0qq = pod.matrices_dict["2_0yy"] + pod._translation_qqq  #16
_matrix_4_1_qy0_0q0 = pod.matrices_dict["4_0y0"] + pod._translation_qqq  #18
_matrix_2_1_xox_q0q = pod.matrices_dict["2_x0x"] + pod._translation_qqq  #20
_matrix_4_1_0qz_00q = pod.matrices_dict["4_00z"] + pod._translation_qqq  #21=22
_matrix_2_1_xxo_qq0 = pod.matrices_dict["2_xx0"] + pod._translation_qqq  #24
_matrix_inv_oo3o = pod.matrices_dict["inv_000"] + pod._translation_qqq + pod._translation_00h  #25
_matrix_d_oyz_0q3q = pod.matrices_dict["m_0yz"] + pod._translation_qqq + pod._translation_00h  #26
_matrix_d_xoz_q03q = pod.matrices_dict["m_x0z"] + pod._translation_qqq + pod._translation_00h  #27
_matrix_d_xy3o_qq0 = pod.matrices_dict["m_xy0"] + pod._translation_qqq + pod._translation_00h  #28
_matrix_m3_mhxxx_mo3o3o = pod.matrices_dict["m3_xxx"] + pod._translation_qqq + pod._translation_00h  #29=33
_matrix_m3_hxhmxmx_3o5oo = pod.matrices_dict["m3_xmxmx"] + pod._translation_qqq + pod._translation_00h  #30=34
_matrix_m3_m1mxhxmx_m3omo5o = pod.matrices_dict["m3_mxxmx"] + pod._translation_qqq + pod._translation_00h  #31=35
_matrix_m3_1mxmxx_5om3o3o = pod.matrices_dict["m3_mxmxx"] + pod._translation_qqq + pod._translation_00h  #32=36

# tA[0,h,h]
_matrix_4_1_x03q_q00 = pod.matrices_dict["4_x00"] + pod._translation_qqq + pod._translation_0hh  #61=62
_matrix_2_o3qmyy = pod.matrices_dict["2_0myy"] + pod._translation_qqq + pod._translation_0hh  #63
_matrix_2_1_oyy_03q3q = pod.matrices_dict["2_0yy"] + pod._translation_qqq + pod._translation_0hh  #64
_matrix_2_1_hmx3ox_mq0q = pod.matrices_dict["2_mx0x"] + pod._translation_qqq + pod._translation_0hh  #67
_matrix_2_1_mqx3ox_h0h = pod.matrices_dict["2_x0x"] + pod._translation_qqq + pod._translation_0hh  #68
_matrix_4_3_mqhz_003q = pod.matrices_dict["4_00z"] + pod._translation_qqq + pod._translation_0hh  #69=70
_matrix_2_1_xhmx3o_mqq0 = pod.matrices_dict["2_xmx0"] + pod._translation_qqq + pod._translation_0hh  #71
_matrix_inv_o3oo = pod.matrices_dict["inv_000"] + pod._translation_qqq + pod._translation_0h0  #73
_matrix_d_oyz_03qq = pod.matrices_dict["m_0yz"] + pod._translation_qqq + pod._translation_0h0  #74
_matrix_d_x3oz_q0q = pod.matrices_dict["m_x0z"] + pod._translation_qqq + pod._translation_0h0  #75
_matrix_d_xyo_q3q0 = pod.matrices_dict["m_xy0"] + pod._translation_qqq + pod._translation_0h0  #76
_matrix_m3_hxhxx_3o3omo = pod.matrices_dict["m3_xxx"] + pod._translation_qqq + pod._translation_0h0  #77=81
_matrix_m3_mhx1mxmx_mo5om3o = pod.matrices_dict["m3_xmxmx"] + pod._translation_qqq + pod._translation_0h0  #78=82
_matrix_m3_m1mx1xmx_m3o3o5o = pod.matrices_dict["m3_mxxmx"] + pod._translation_qqq + pod._translation_0h0  #79=83
_matrix_m3_1mxhmxx_5oo3o = pod.matrices_dict["m3_mxmxx"] + pod._translation_qqq + pod._translation_0h0  #80=84
_matrix_m4_qqz_qq0 = pod.matrices_dict["-4_00z"] + pod._translation_0h0  #93=94

# tB[h,0,h]
_matrix_4_3_xmqh_3q00 = pod.matrices_dict["4_x00"] + pod._translation_qqq + pod._translation_h0h  #109=110
_matrix_2_1_3ohmyy_0mqq = pod.matrices_dict["2_0yy"] + pod._translation_qqq + pod._translation_h0h  #111
_matrix_4_1_3qy0_0q0 = pod.matrices_dict["4_0y0"] + pod._translation_h0h  #113=114
_matrix_2_3qmxox = pod.matrices_dict["2_mx0x"] + pod._translation_qqq + pod._translation_h0h  #115
_matrix_2_1_xox_3q03q = pod.matrices_dict["2_x0x"] + pod._translation_qqq + pod._translation_h0h  #116
_matrix_2_1_xhmx3o_qmq0 = pod.matrices_dict["2_xmx0"] + pod._translation_qqq + pod._translation_h0h  #119
_matrix_2_1_xmqx3o_hh0 = pod.matrices_dict["2_xx0"] + pod._translation_qqq + pod._translation_h0h  #120
_matrix_inv_3ooo = pod.matrices_dict["inv_000"] + pod._translation_qqq + pod._translation_h00  #121
_matrix_d_3oyz_0qq = pod.matrices_dict["m_0yz"] + pod._translation_qqq + pod._translation_h00  #122
_matrix_d_xoz_3q0q = pod.matrices_dict["m_x0z"] + pod._translation_qqq + pod._translation_h00  #123
_matrix_d_xyo_3qq0 = pod.matrices_dict["m_xy0"] + pod._translation_qqq + pod._translation_h00  #124
_matrix_m3_xmhxx_3omo3o = pod.matrices_dict["m3_xxx"] + pod._translation_qqq + pod._translation_h00  #125=129
_matrix_m3_x1mxmx_3o5om3o = pod.matrices_dict["m3_xmxmx"] + pod._translation_qqq + pod._translation_h00  #126=130
_matrix_m3_mhmx1xmx_o3o5o = pod.matrices_dict["m3_mxxmx"] + pod._translation_qqq + pod._translation_h00  #127=131
_matrix_m3_hmxmhmxx_5om3omo = pod.matrices_dict["m3_mxmxx"] + pod._translation_qqq + pod._translation_h00  #128=132

# tC[h,h,0]
_matrix_2_1_3ohmyy_0qmq = pod.matrices_dict["2_0myy"] + pod._translation_qqq + pod._translation_hh0  #159
_matrix_2_1_3oqyy_0hh = pod.matrices_dict["2_0yy"] + pod._translation_qqq + pod._translation_hh0  #160
_matrix_4_3_hymq_03q0 = pod.matrices_dict["4_0y0"] + pod._translation_qqq + pod._translation_hh0  #161=162
_matrix_2_1_hmx3ox_q0mq = pod.matrices_dict["2_mx0x"] + pod._translation_qqq + pod._translation_hh0  #163
_matrix_4_1_03qz_00q = pod.matrices_dict["4_00z"] + pod._translation_qqq + pod._translation_hh0  #165=166
_matrix_2_x3qmxo = pod.matrices_dict["2_xmx0"] + pod._translation_qqq + pod._translation_hh0  #167
_matrix_2_1_xxo_3q3qo = pod.matrices_dict["2_xx0"] + pod._translation_qqq + pod._translation_hh0  #168
_matrix_inv_3o3o3o = pod.matrices_dict["inv_000"] + pod._translation_qqq + pod._translation_hhh  #169
_matrix_d_3oyz_03q3q = pod.matrices_dict["m_0yz"] + pod._translation_qqq + pod._translation_hhh  #170
_matrix_d_x3oz_3q03q = pod.matrices_dict["m_x0z"] + pod._translation_qqq + pod._translation_hhh  #171
_matrix_d_xy3o_3q3q0 = pod.matrices_dict["m_xy0"] + pod._translation_qqq + pod._translation_hhh  #172
_matrix_m3_xxx_3o3o3o = pod.matrices_dict["m3_xxx"] + pod._translation_qqq + pod._translation_hhh  #173=177
_matrix_m3_xhmxmx_3oom3o = pod.matrices_dict["m3_xmxmx"] + pod._translation_qqq + pod._translation_hhh  #174=178
_matrix_m3_mhmxhxmx_m3o3oo = pod.matrices_dict["m3_mxxmx"] + pod._translation_qqq + pod._translation_hhh  #175=179
_matrix_m3_hmxmxx_om3o3o = pod.matrices_dict["m3_mxmxx"] + pod._translation_qqq + pod._translation_hhh  #176=180

# P2_1
_matrix_2_1_0y0_0h0 = pod.matrices_dict["2_0y0"] + pod._translation_0h0  #2


_matrix_translation_h00 = pod._matrix_ID_000 + pod._translation_h00  #1
_matrix_translation_0h0 = pod._matrix_ID_000 + pod._translation_0h0  #2
_matrix_translation_00h = pod._matrix_ID_000 + pod._translation_00h  #3
_matrix_translation_0hh = pod._matrix_ID_000 + pod._translation_0hh  #4
_matrix_translation_h0h = pod._matrix_ID_000 + pod._translation_h0h  #5
_matrix_translation_hh0 = pod._matrix_ID_000 + pod._translation_hh0  #6
_matrix_translation_hhh = pod._matrix_ID_000 + pod._translation_hhh  #7
_matrix_translation_qqq = pod._matrix_ID_000 + pod._translation_qqq  #8
_matrix_translation_3qqq = pod._matrix_ID_000 + pod._translation_h00 + pod._translation_qqq  #9
_matrix_translation_q3qq = pod._matrix_ID_000 + pod._translation_0h0 + pod._translation_qqq  #10
_matrix_translation_qq3q = pod._matrix_ID_000 + pod._translation_00h + pod._translation_qqq  #11
_matrix_translation_q3q3q = pod._matrix_ID_000 + pod._translation_0hh + pod._translation_qqq  #12
_matrix_translation_3qq3q = pod._matrix_ID_000 + pod._translation_h0h + pod._translation_qqq  #13
_matrix_translation_3q3qq = pod._matrix_ID_000 + pod._translation_hh0 + pod._translation_qqq  #14
_matrix_translation_3q3q3q = pod._matrix_ID_000 + pod._translation_hhh + pod._translation_qqq  #15

all_matrix_translations = np.array([
    _matrix_translation_h00,
    _matrix_translation_0h0,
    _matrix_translation_00h,
    _matrix_translation_0hh,
    _matrix_translation_h0h,
    _matrix_translation_hh0,
    _matrix_translation_hhh,
    _matrix_translation_qqq,
    _matrix_translation_3qqq,
    _matrix_translation_q3qq,
    _matrix_translation_qq3q,
    _matrix_translation_q3q3q,
    _matrix_translation_3qq3q,
    _matrix_translation_3q3qq,
    _matrix_translation_3q3q3q],
    dtype=int
)

all_translations = all_matrix_translations[:, :-1, -1]

all_labels_trans = np.array([
    "t_h00",
    "t_0h0",
    "t_00h",
    "t_0hh",
    "t_h0h",
    "t_hh0",
    "t_hhh",
    "t_qqq",
    "t_3qqq",
    "t_q3qq",
    "t_qq3q",
    "t_q3q3q",
    "t_3qq3q",
    "t_3q3qq",
    "t_3q3q3q"
])

all_matrices = [
    pod._matrix_ID_000,
    pod._matrix_2_00z,
    pod._matrix_2_0myy,
    _matrix_2_0qmyy_0mqq,
    _matrix_2_0qyy_0qq,
    _matrix_2_0qz,
    pod._matrix_2_0y0,
    pod._matrix_2_0yy,
    _matrix_2_1_0qmyy_0qmq,
    _matrix_2_1_0qyy_0qq,
    _matrix_2_1_0qz_00h,
    _matrix_2_1_0y0_0h0,
    _matrix_2_1_0yq_0h0,
    _matrix_2_1_3ohmyy_0mqq,
    _matrix_2_1_3ohmyy_0qmq,
    _matrix_2_1_3omqyy_0hh,
    _matrix_2_1_3oqyy_0hh,
    _matrix_2_1_hmx3ox_mq0q,
    _matrix_2_1_hmx3ox_q0mq,
    _matrix_2_1_mqx0x_q0q,
    _matrix_2_1_mqx3ox_h0h,
    _matrix_2_1_mqxox_h0h,
    _matrix_2_1_oqyy_0hh,
    _matrix_2_1_oyy_03q3q,
    _matrix_2_1_oyy_0qq,
    _matrix_2_1_q0z_00h,
    _matrix_2_1_qmx0x_mq0q,
    _matrix_2_1_qmx0x_q0mq,
    _matrix_2_1_qqz_00h,
    _matrix_2_1_qx0x_q0mq,
    _matrix_2_1_qx3ox_h0h,
    _matrix_2_1_qy0_0h0,
    _matrix_2_1_qyq_0h0,
    _matrix_2_1_qyy_0hh,
    _matrix_2_1_x0q_h00,
    _matrix_2_1_xhmx3o_mqq0,
    _matrix_2_1_xhmx3o_qmq0,
    _matrix_2_1_xmqx0_qq0,
    _matrix_2_1_xmqx3o_hh0,
    _matrix_2_1_xmqxo_hh0,
    _matrix_2_1_xox_3q03q,
    _matrix_2_1_xox_q0q,
    _matrix_2_1_xq0_h00,
    _matrix_2_1_xqmx0_mqq0,
    _matrix_2_1_xqmx0_qmq0,
    _matrix_2_1_xqq_h00,
    _matrix_2_1_xqx0_qq0,
    _matrix_2_1_xqx3o_hh0,
    _matrix_2_1_xqx_q0q,
    _matrix_2_1_xxo_3q3qo,
    _matrix_2_1_xxo_qq0,
    _matrix_2_1_xxq_hh0,
    _matrix_2_3o3qmyy,
    _matrix_2_3qmx3ox,
    _matrix_2_3qmxox,
    _matrix_2_hmxqx,
    pod._matrix_2_mx0x,
    _matrix_2_mxqx,
    _matrix_2_o3qmyy,
    _matrix_2_oqmyy,
    _matrix_2_qhmyy,
    _matrix_2_qmxox,
    _matrix_2_qmyy,
    _matrix_2_qqz,
    _matrix_2_qy0,
    _matrix_2_qyq,
    _matrix_2_qyy,
    pod._matrix_2_x00,
    _matrix_2_x0q,
    pod._matrix_2_x0x,
    _matrix_2_x3qmx3o,
    _matrix_2_x3qmxo,
    _matrix_2_xhmxq,
    pod._matrix_2_xmx0,
    _matrix_2_xmxq,
    _matrix_2_xqmxo,
    _matrix_2_xqq,
    _matrix_2_xqx,
    pod._matrix_2_xx0,
    _matrix_2_xxq,
    _matrix_3_1_HxmHxx_ttt,
    _matrix_3_1_Hxtxx_ttt,
    _matrix_3_1_mtmHxx_ttt,
    _matrix_3_2_2txmtmxmx_mHHH,
    _matrix_3_2_HmxHxmx_tmtt,
    _matrix_3_2_Hmxtmxx_ttmt,
    _matrix_3_2_HxHmxmx_mHHH,
    _matrix_3_2_mHmxtxmx_HmHH,
    _matrix_3_2_tmx2tmxx_HHmH,
    _matrix_3_2_tmxHmxx_HHmH,
    _matrix_3_2_tmxtxmx_HmHH,
    _matrix_3_2_txmHmxmx_mttt,
    _matrix_3_hmxhmxx,
    _matrix_3_hmxxmx,
    _matrix_3_hxmhmxmx,
    _matrix_3_hxmxmx,
    _matrix_3_mxhmxx,
    _matrix_3_mxhxmx,
    pod._matrix_3_mxmxx,
    pod._matrix_3_mxxmx,
    pod._matrix_3_xmxmx,
    pod._matrix_3_xxx,
    _matrix_3_xxx_hhh,
    pod._matrix_4_00z,
    pod._matrix_4_0y0,
    _matrix_4_1_03qz_00q,
    _matrix_4_1_0qz_00q,
    _matrix_4_1_3qy0_0q0,
    _matrix_4_1_hymq_0q0,
    _matrix_4_1_mqhz_00q,
    _matrix_4_1_qy0_0q0,
    _matrix_4_1_x03q_q00,
    _matrix_4_1_x0q_q00,
    _matrix_4_1_xmqh_q00,
    _matrix_4_2_00z_00h,
    _matrix_4_2_0hz_00h,
    _matrix_4_2_0y0_0h0,
    _matrix_4_2_x00_h00,
    _matrix_4_2_x0h_h00,
    _matrix_4_3_hymq_03q0,
    _matrix_4_3_hyq_03q0,
    _matrix_4_3_mqhz_003q,
    _matrix_4_3_qhz_003q,
    _matrix_4_3_xmqh_3q00,
    _matrix_4_3_xqh_3q00,
    _matrix_4_mqqz,
    _matrix_4_qqz,
    _matrix_4_qy0_0h0,
    _matrix_4_qymq,
    _matrix_4_qyq,
    pod._matrix_4_x00,
    _matrix_4_xmqq,
    _matrix_4_xqq,
    _matrix_a_x0z_h00,
    _matrix_a_xhymy_h00,
    _matrix_a_xqz_h00,
    _matrix_a_xymy_h00,
    _matrix_a_xyq_h00,
    _matrix_a_xyy_h00,
    _matrix_b_hxymx_0h0,
    _matrix_b_qyz_0h0,
    _matrix_b_xy0_0h0,
    _matrix_b_xymx_0h0,
    _matrix_b_xyq_0h0,
    _matrix_b_xyx_0h0,
    _matrix_c_0yz_00h,
    _matrix_c_hxmxz_00h,
    _matrix_c_xmxz_00h,
    _matrix_c_xqz_00h,
    _matrix_c_xxz_00h,
    _matrix_d_3oyz_03q3q,
    _matrix_d_3oyz_03qq,
    _matrix_d_3oyz_0q3q,
    _matrix_d_3oyz_0qq,
    _matrix_d_hxmxz_mqq3q,
    _matrix_d_hxmxz_qmqq,
    _matrix_d_hxymx_mqqq,
    _matrix_d_hxymx_q3qmq,
    _matrix_d_oyz_03q3q,
    _matrix_d_oyz_03qq,
    _matrix_d_oyz_0q3q,
    _matrix_d_oyz_0qq,
    _matrix_d_x3oz_3q03q,
    _matrix_d_x3oz_3q0q,
    _matrix_d_x3oz_q03q,
    _matrix_d_x3oz_q0q,
    _matrix_d_xhymy_3qmqq,
    _matrix_d_xhymy_qqmq,
    _matrix_d_xoz_3q03q,
    _matrix_d_xoz_3q0q,
    _matrix_d_xoz_q03q,
    _matrix_d_xoz_q0q,
    _matrix_d_xxz_3q3q3q,
    _matrix_d_xxz_qqq,
    _matrix_d_xy3o_3q3q0,
    _matrix_d_xy3o_q3q0,
    _matrix_d_xy3o_qq0,
    _matrix_d_xyo_3q3q0,
    _matrix_d_xyo_3qq0,
    _matrix_d_xyo_q3q0,
    _matrix_d_xyo_qq0,
    _matrix_d_xyx_3q3q3q,
    _matrix_d_xyx_qqq,
    _matrix_d_xyy_3q3q3q,
    _matrix_d_xyy_qqq,
    _matrix_dxy3o_3qq0,
    pod._matrix_inv_000,
    _matrix_inv_0qq,
    _matrix_inv_3o3o3o,
    _matrix_inv_3o3oo,
    _matrix_inv_3oo3o,
    _matrix_inv_3ooo,
    _matrix_inv_o3o3o,
    _matrix_inv_o3oo,
    _matrix_inv_oo3o,
    _matrix_inv_ooo,
    _matrix_inv_q0q,
    _matrix_inv_qq0,
    _matrix_inv_qqq,
    _matrix_m3_1mxhmxx_5oo3o,
    _matrix_m3_1mxhmxx_h0h,
    _matrix_m3_1mxmxx_5om3o3o,
    _matrix_m3_hmxhxmx_00h,
    _matrix_m3_hmxmhmxx_5om3omo,
    _matrix_m3_hmxmhmxx_hmh0,
    _matrix_m3_hmxmxx_h00,
    _matrix_m3_hmxmxx_om3o3o,
    _matrix_m3_hxhmxmx_3o5oo,
    _matrix_m3_hxhmxmx_hh0,
    _matrix_m3_hxhxx_3o3omo,
    _matrix_m3_m1mx1xmx_m3o3o5o,
    _matrix_m3_m1mxhxmx_m3omo5o,
    _matrix_m3_m1mxhxmx_mh0h,
    _matrix_m3_mhmx1xmx_0hh,
    _matrix_m3_mhmx1xmx_o3o5o,
    _matrix_m3_mhmxhxmx_m3o3oo,
    _matrix_m3_mhmxxmx_mqmqq,
    _matrix_m3_mhx1mxmx_0hmh,
    _matrix_m3_mhx1mxmx_mo5om3o,
    _matrix_m3_mhxhmxmx_mqqmq,
    _matrix_m3_mhxmhxx_00h,
    _matrix_m3_mhxxx_h00,
    _matrix_m3_mhxxx_mo3o3o,
    _matrix_m3_mxmhmxx_qmqmq,
    pod._matrix_m3_mxmxx,
    _matrix_m3_mxmxx_3qmqq,
    pod._matrix_m3_mxxmx,
    _matrix_m3_mxxmx_mqq3q,
    _matrix_m3_x1mxmx_3o5om3o,
    _matrix_m3_xhmxmx_0h0,
    _matrix_m3_xhmxmx_3oom3o,
    _matrix_m3_xhxx_0h0,
    _matrix_m3_xmhxx_3omo3o,
    pod._matrix_m3_xmxmx,
    _matrix_m3_xmxmx_q3qmq,
    pod._matrix_m3_xxx,
    _matrix_m3_xxx_3o3o3o,
    _matrix_m3_xxx_qqq,
    pod._matrix_m4_00z,
    _matrix_m4_00z_00q,
    pod._matrix_m4_0y0,
    _matrix_m4_0y0_0q0,
    _matrix_m4_0yh_0qh,
    _matrix_m4_h0z_h0q,
    _matrix_m4_hmqz_hmq3o,
    _matrix_m4_hqz_hqo,
    _matrix_m4_mqyh_mq3oh,
    _matrix_m4_mqyq_mq0q,
    _matrix_m4_qmqz_qmq0,
    _matrix_m4_qqz_qq0,
    _matrix_m4_qyh_qoh,
    _matrix_m4_qyq_q0q,
    pod._matrix_m4_x00,
    _matrix_m4_x00_q00,
    _matrix_m4_xh0_qh0,
    _matrix_m4_xhmq_3ohmq,
    _matrix_m4_xhq_ohq,
    _matrix_m4_xqmq_0qmq,
    _matrix_m4_xqq_0qq,
    pod._matrix_m_0yz,
    pod._matrix_m_x0z,
    pod._matrix_m_xmxz,
    pod._matrix_m_xxz,
    pod._matrix_m_xy0,
    pod._matrix_m_xymx,
    pod._matrix_m_xymy,
    pod._matrix_m_xyx,
    pod._matrix_m_xyy,
    _matrix_n_0yz_0hh,
    _matrix_n_mqxxz_qq0,
    _matrix_n_mqxyx_q0q,
    _matrix_n_qxmxz_mqq0,
    _matrix_n_qxmxz_qmq0,
    _matrix_n_qxxz_qq0,
    _matrix_n_qxymx_mq0q,
    _matrix_n_qxymx_q0mq,
    _matrix_n_qxymx_q0q,
    _matrix_n_qyz_00h,
    _matrix_n_qyz_0hh,
    _matrix_n_x0z_h0h,
    _matrix_n_xmqyy_0qq,
    _matrix_n_xqymy_0mqq,
    _matrix_n_xqymy_0qmq,
    _matrix_n_xqyy_0qq,
    _matrix_n_xqz_h0h,
    _matrix_n_xxz_hhh,
    _matrix_n_xy0_hh0,
    _matrix_n_xyq_hh0,
    _matrix_n_xyx_hhh,
    _matrix_n_xyy_hhh,
#     HEX._matrix_hex_2_0y0,
#     HEX._matrix_hex_2_0yH,
#     HEX._matrix_hex_2_0yq,
#     HEX._matrix_hex_2_0yt,
#     HEX._matrix_hex_2_2xx0,
#     HEX._matrix_hex_2_2xxq,
#     HEX._matrix_hex_2_2xxv,
#     HEX._matrix_hex_2_x00,
#     HEX._matrix_hex_2_x0H,
#     HEX._matrix_hex_2_x0q,
#     HEX._matrix_hex_2_x0t,
#     HEX._matrix_hex_2_x2x0,
#     HEX._matrix_hex_2_x2xH,
#     HEX._matrix_hex_2_x2xq,
#     HEX._matrix_hex_2_x2xt,
#     HEX._matrix_hex_2_xmx5v,
#     HEX._matrix_hex_2_xmxH,
#     HEX._matrix_hex_2_xmxt,
#     HEX._matrix_hex_2_xxH,
#     HEX._matrix_hex_3_00z,
#     HEX._matrix_hex_3_1_00z_00t,
#     HEX._matrix_hex_3_2_00z_002t,
#     HEX._matrix_hex_6_00z,
#     HEX._matrix_hex_6_1_00z_00H,
#     HEX._matrix_hex_6_2_00z_00t,
#     HEX._matrix_hex_6_3_00z_00h,
#     HEX._matrix_hex_6_4_00z_002t,
#     HEX._matrix_hex_6_5_00z_005H,
#     HEX._matrix_hex_c_0yz_00h,
#     HEX._matrix_hex_c_2xxz_00h,
#     HEX._matrix_hex_c_x0z_00h,
#     HEX._matrix_hex_c_x2xz_00h,
#     HEX._matrix_hex_m3_00z,
#     HEX._matrix_hex_m6_00z,
#     HEX._matrix_hex_m_0yz,
#     HEX._matrix_hex_m_2xxz,
#     HEX._matrix_hex_m_x0z,
#     HEX._matrix_hex_m_x2xz,
    _matrix_translation_h00,
    _matrix_translation_0h0,
    _matrix_translation_00h,
    _matrix_translation_0hh,
    _matrix_translation_h0h,
    _matrix_translation_hh0,
    _matrix_translation_hhh,
    _matrix_translation_qqq,
    _matrix_translation_3qqq,
    _matrix_translation_q3qq,
    _matrix_translation_qq3q,
    _matrix_translation_q3q3q,
    _matrix_translation_3qq3q,
    _matrix_translation_3q3qq,
    _matrix_translation_3q3q3q,
]

names = [
    "ID_000",
    "2_00z",
    "2_0myy",
    "2_0qmyy_0mqq",
    "2_0qyy_0qq",
    "2_0qz",
    "2_0y0",
    "2_0yy",
    "2_1_0qmyy_0qmq",
    "2_1_0qyy_0qq",
    "2_1_0qz_00h",
    "2_1_0y0_0h0",
    "2_1_0yq_0h0",
    "2_1_3ohmyy_0mqq",
    "2_1_3ohmyy_0qmq",
    "2_1_3omqyy_0hh",
    "2_1_3oqyy_0hh",
    "2_1_hmx3ox_mq0q",
    "2_1_hmx3ox_q0mq",
    "2_1_mqx0x_q0q",
    "2_1_mqx3ox_h0h",
    "2_1_mqxox_h0h",
    "2_1_oqyy_0hh",
    "2_1_oyy_03q3q",
    "2_1_oyy_0qq",
    "2_1_q0z_00h",
    "2_1_qmx0x_mq0q",
    "2_1_qmx0x_q0mq",
    "2_1_qqz_00h",
    "2_1_qx0x_q0mq",
    "2_1_qx3ox_h0h",
    "2_1_qy0_0h0",
    "2_1_qyq_0h0",
    "2_1_qyy_0hh",
    "2_1_x0q_h00",
    "2_1_xhmx3o_mqq0",
    "2_1_xhmx3o_qmq0",
    "2_1_xmqx0_qq0",
    "2_1_xmqx3o_hh0",
    "2_1_xmqxo_hh0",
    "2_1_xox_3q03q",
    "2_1_xox_q0q",
    "2_1_xq0_h00",
    "2_1_xqmx0_mqq0",
    "2_1_xqmx0_qmq0",
    "2_1_xqq_h00",
    "2_1_xqx0_qq0",
    "2_1_xqx3o_hh0",
    "2_1_xqx_q0q",
    "2_1_xxo_3q3qo",
    "2_1_xxo_qq0",
    "2_1_xxq_hh0",
    "2_3o3qmyy",
    "2_3qmx3ox",
    "2_3qmxox",
    "2_hmxqx",
    "2_mx0x",
    "2_mxqx",
    "2_o3qmyy",
    "2_oqmyy",
    "2_qhmyy",
    "2_qmxox",
    "2_qmyy",
    "2_qqz",
    "2_qy0",
    "2_qyq",
    "2_qyy",
    "2_x00",
    "2_x0q",
    "2_x0x",
    "2_x3qmx3o",
    "2_x3qmxo",
    "2_xhmxq",
    "2_xmx0",
    "2_xmxq",
    "2_xqmxo",
    "2_xqq",
    "2_xqx",
    "2_xx0",
    "2_xxq",
    "3_1_HxmHxx_ttt",
    "3_1_Hxtxx_ttt",
    "3_1_mtmHxx_ttt",
    "3_2_2txmtmxmx_mHHH",
    "3_2_HmxHxmx_tmtt",
    "3_2_Hmxtmxx_ttmt",
    "3_2_HxHmxmx_mHHH",
    "3_2_mHmxtxmx_HmHH",
    "3_2_tmx2tmxx_HHmH",
    "3_2_tmxHmxx_HHmH",
    "3_2_tmxtxmx_HmHH",
    "3_2_txmHmxmx_mttt",
    "3_hmxhmxx",
    "3_hmxxmx",
    "3_hxmhmxmx",
    "3_hxmxmx",
    "3_mxhmxx",
    "3_mxhxmx",
    "3_mxmxx",
    "3_mxxmx",
    "3_xmxmx",
    "3_xxx",
    "3_xxx_hhh",
    "4_00z",
    "4_0y0",
    "4_1_03qz_00q",
    "4_1_0qz_00q",
    "4_1_3qy0_0q0",
    "4_1_hymq_0q0",
    "4_1_mqhz_00q",
    "4_1_qy0_0q0",
    "4_1_x03q_q00",
    "4_1_x0q_q00",
    "4_1_xmqh_q00",
    "4_2_00z_00h",
    "4_2_0hz_00h",
    "4_2_0y0_0h0",
    "4_2_x00_h00",
    "4_2_x0h_h00",
    "4_3_hymq_03q0",
    "4_3_hyq_03q0",
    "4_3_mqhz_003q",
    "4_3_qhz_003q",
    "4_3_xmqh_3q00",
    "4_3_xqh_3q00",
    "4_mqqz",
    "4_qqz",
    "4_qy0_0h0",
    "4_qymq",
    "4_qyq",
    "4_x00",
    "4_xmqq",
    "4_xqq",
    "a_x0z_h00",
    "a_xhymy_h00",
    "a_xqz_h00",
    "a_xymy_h00",
    "a_xyq_h00",
    "a_xyy_h00",
    "b_hxymx_0h0",
    "b_qyz_0h0",
    "b_xy0_0h0",
    "b_xymx_0h0",
    "b_xyq_0h0",
    "b_xyx_0h0",
    "c_0yz_00h",
    "c_hxmxz_00h",
    "c_xmxz_00h",
    "c_xqz_00h",
    "c_xxz_00h",
    "d_3oyz_03q3q",
    "d_3oyz_03qq",
    "d_3oyz_0q3q",
    "d_3oyz_0qq",
    "d_hxmxz_mqq3q",
    "d_hxmxz_qmqq",
    "d_hxymx_mqqq",
    "d_hxymx_q3qmq",
    "d_oyz_03q3q",
    "d_oyz_03qq",
    "d_oyz_0q3q",
    "d_oyz_0qq",
    "d_x3oz_3q03q",
    "d_x3oz_3q0q",
    "d_x3oz_q03q",
    "d_x3oz_q0q",
    "d_xhymy_3qmqq",
    "d_xhymy_qqmq",
    "d_xoz_3q03q",
    "d_xoz_3q0q",
    "d_xoz_q03q",
    "d_xoz_q0q",
    "d_xxz_3q3q3q",
    "d_xxz_qqq",
    "d_xy3o_3q3q0",
    "d_xy3o_q3q0",
    "d_xy3o_qq0",
    "d_xyo_3q3q0",
    "d_xyo_3qq0",
    "d_xyo_q3q0",
    "d_xyo_qq0",
    "d_xyx_3q3q3q",
    "d_xyx_qqq",
    "d_xyy_3q3q3q",
    "d_xyy_qqq",
    "dxy3o_3qq0",
    "inv_000",
    "inv_0qq",
    "inv_3o3o3o",
    "inv_3o3oo",
    "inv_3oo3o",
    "inv_3ooo",
    "inv_o3o3o",
    "inv_o3oo",
    "inv_oo3o",
    "inv_ooo",
    "inv_q0q",
    "inv_qq0",
    "inv_qqq",
    "m3_1mxhmxx_5oo3o",
    "m3_1mxhmxx_h0h",
    "m3_1mxmxx_5om3o3o",
    "m3_hmxhxmx_00h",
    "m3_hmxmhmxx_5om3omo",
    "m3_hmxmhmxx_hmh0",
    "m3_hmxmxx_h00",
    "m3_hmxmxx_om3o3o",
    "m3_hxhmxmx_3o5oo",
    "m3_hxhmxmx_hh0",
    "m3_hxhxx_3o3omo",
    "m3_m1mx1xmx_m3o3o5o",
    "m3_m1mxhxmx_m3omo5o",
    "m3_m1mxhxmx_mh0h",
    "m3_mhmx1xmx_0hh",
    "m3_mhmx1xmx_o3o5o",
    "m3_mhmxhxmx_m3o3oo",
    "m3_mhmxxmx_mqmqq",
    "m3_mhx1mxmx_0hmh",
    "m3_mhx1mxmx_mo5om3o",
    "m3_mhxhmxmx_mqqmq",
    "m3_mhxmhxx_00h",
    "m3_mhxxx_h00",
    "m3_mhxxx_mo3o3o",
    "m3_mxmhmxx_qmqmq",
    "m3_mxmxx",
    "m3_mxmxx_3qmqq",
    "m3_mxxmx",
    "m3_mxxmx_mqq3q",
    "m3_x1mxmx_3o5om3o",
    "m3_xhmxmx_0h0",
    "m3_xhmxmx_3oom3o",
    "m3_xhxx_0h0",
    "m3_xmhxx_3omo3o",
    "m3_xmxmx",
    "m3_xmxmx_q3qmq",
    "m3_xxx",
    "m3_xxx_3o3o3o",
    "m3_xxx_qqq",
    "m4_00z",
    "m4_00z_00q",
    "m4_0y0",
    "m4_0y0_0q0",
    "m4_0yh_0qh",
    "m4_h0z_h0q",
    "m4_hmqz_hmq3o",
    "m4_hqz_hqo",
    "m4_mqyh_mq3oh",
    "m4_mqyq_mq0q",
    "m4_qmqz_qmq0",
    "m4_qqz_qq0",
    "m4_qyh_qoh",
    "m4_qyq_q0q",
    "m4_x00",
    "m4_x00_q00",
    "m4_xh0_qh0",
    "m4_xhmq_3ohmq",
    "m4_xhq_ohq",
    "m4_xqmq_0qmq",
    "m4_xqq_0qq",
    "m_0yz",
    "m_x0z",
    "m_xmxz",
    "m_xxz",
    "m_xy0",
    "m_xymx",
    "m_xymy",
    "m_xyx",
    "m_xyy",
    "n_0yz_0hh",
    "n_mqxxz_qq0",
    "n_mqxyx_q0q",
    "n_qxmxz_mqq0",
    "n_qxmxz_qmq0",
    "n_qxxz_qq0",
    "n_qxymx_mq0q",
    "n_qxymx_q0mq",
    "n_qxymx_q0q",
    "n_qyz_00h",
    "n_qyz_0hh",
    "n_x0z_h0h",
    "n_xmqyy_0qq",
    "n_xqymy_0mqq",
    "n_xqymy_0qmq",
    "n_xqyy_0qq",
    "n_xqz_h0h",
    "n_xxz_hhh",
    "n_xy0_hh0",
    "n_xyq_hh0",
    "n_xyx_hhh",
    "n_xyy_hhh",
#     "hex_2_0y0",
#     "hex_2_0yH",
#     "hex_2_0yq",
#     "hex_2_0yt",
#     "hex_2_2xx0",
#     "hex_2_2xxq",
#     "hex_2_2xxv",
#     "hex_2_x00",
#     "hex_2_x0H",
#     "hex_2_x0q",
#     "hex_2_x0t",
#     "hex_2_x2x0",
#     "hex_2_x2xH",
#     "hex_2_x2xq",
#     "hex_2_x2xt",
#     "hex_2_xmx5v",
#     "hex_2_xmxH",
#     "hex_2_xmxt",
#     "hex_2_xxH",
#     "hex_3_00z",
#     "hex_3_1_00z_00t",
#     "hex_3_2_00z_002t",
#     "hex_6_00z",
#     "hex_6_1_00z_00H",
#     "hex_6_2_00z_00t",
#     "hex_6_3_00z_00h",
#     "hex_6_4_00z_002t",
#     "hex_6_5_00z_005H",
#     "hex_c_0yz_00h",
#     "hex_c_2xxz_00h",
#     "hex_c_x0z_00h",
#     "hex_c_x2xz_00h",
#     "hex_m3_00z",
#     "hex_m6_00z",
#     "hex_m_0yz",
#     "hex_m_2xxz",
#     "hex_m_x0z",
#     "hex_m_x2xz",
    "t_h00",
    "t_0h0",
    "t_00h",
    "t_0hh",
    "t_h0h",
    "t_hh0",
    "t_hhh",
    "t_qqq",
    "t_3qqq",
    "t_q3qq",
    "t_qq3q",
    "t_q3q3q",
    "t_3qq3q",
    "t_3q3qq",
    "t_3q3q3q",
]

def inverse(mat):
    new_mat = mat.copy()

    rot = new_mat[:-1, :-1]
    rot = rot.T

    trans = mat[:-1, -1] * -1
    mask_trans = trans < 0
    trans[mask_trans] += 12

    new_mat[:-1, :-1] = rot
    new_mat[:-1, -1] = trans

    return new_mat

l = []
ID = pod._matrix_ID_000
for i, mat in enumerate(all_matrices):
    new_mat = inverse(mat)
    if not np.array_equal(mat, new_mat):
        l.append((i, new_mat, mat, names[i]))
breakpoint()