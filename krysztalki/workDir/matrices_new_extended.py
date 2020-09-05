import numpy as np

_matrix_ID_000 = np.array([[ 1, 0, 0, 0],
                           [ 0, 1, 0, 0],
                           [ 0, 0, 1, 0],
                           [ 0, 0, 0, 1]])

_matrix_inv_000 = np.array([[-1, 0, 0, 0],
                            [ 0,-1, 0, 0],
                            [ 0, 0,-1, 0],
                            [ 0, 0, 0, 1]])



_matrix_m_0yz = np.array([[-1, 0, 0, 0],
                          [ 0, 1, 0, 0],
                          [ 0, 0, 1, 0],
                          [ 0, 0, 0, 1]])

_matrix_m_x0z = np.array([[ 1, 0, 0, 0],
                          [ 0,-1, 0, 0],
                          [ 0, 0, 1, 0],
                          [ 0, 0, 0, 1]])

_matrix_m_xy0 = np.array([[ 1, 0, 0, 0],
                          [ 0, 1, 0, 0],
                          [ 0, 0,-1, 0],
                          [ 0, 0, 0, 1]])

_matrix_2_x00    = _matrix_m_0yz   @ _matrix_inv_000
_matrix_2_0y0    = _matrix_m_x0z   @ _matrix_inv_000
_matrix_2_00z    = _matrix_m_xy0   @ _matrix_inv_000

_matrix_m_xyy = np.array([[ 1, 0, 0, 0],
                          [ 0, 0, 1, 0],
                          [ 0, 1, 0, 0],
                          [ 0, 0, 0, 1]])

_matrix_m_xyx = np.array([[ 0, 0, 1, 0],
                          [ 0, 1, 0, 0],
                          [ 1, 0, 0, 0],
                          [ 0, 0, 0, 1]])

_matrix_m_xxz = np.array([[ 0, 1, 0, 0],
                          [ 1, 0, 0, 0],
                          [ 0, 0, 1, 0],
                          [ 0, 0, 0, 1]])


_matrix_m_xymy = np.array([[ 1, 0, 0, 0],
                           [ 0, 0,-1, 0],
                           [ 0,-1, 0, 0],
                           [ 0, 0, 0, 1]])

_matrix_m_xymx = np.array([[ 0, 0,-1, 0],
                           [ 0, 1, 0, 0],
                           [-1, 0, 0, 0],
                           [ 0, 0, 0, 1]])

_matrix_m_xmxz = np.array([[ 0,-1, 0, 0],
                           [-1, 0, 0, 0],
                           [ 0, 0, 1, 0],
                           [ 0, 0, 0, 1]])

_matrix_2_0myy = _matrix_m_xyy @ _matrix_inv_000
_matrix_2_mx0x = _matrix_m_xyx @ _matrix_inv_000
_matrix_2_xmx0 = _matrix_m_xxz @ _matrix_inv_000

_matrix_2_0yy = _matrix_m_xymy @ _matrix_inv_000
_matrix_2_x0x = _matrix_m_xymx @ _matrix_inv_000
_matrix_2_xx0 = _matrix_m_xmxz @ _matrix_inv_000



_matrix_3_xxx = np.array([[ 0, 0, 1, 0],
                          [ 1, 0, 0, 0],
                          [ 0, 1, 0, 0],
                          [ 0, 0, 0, 1]])

_matrix_3_xmxmx = np.array([[ 0, 0,-1, 0],
                            [-1, 0, 0, 0],
                            [ 0, 1, 0, 0],
                            [ 0, 0, 0, 1]])

_matrix_3_mxxmx = np.array([[ 0, 0, 1, 0],
                            [-1, 0, 0, 0],
                            [ 0,-1, 0, 0],
                            [ 0, 0, 0, 1]])

_matrix_3_mxmxx = np.array([[ 0, 0,-1, 0],
                            [ 1, 0, 0, 0],
                            [ 0,-1, 0, 0],
                            [ 0, 0, 0, 1]])


_matrix_4_x00 = np.array([[ 1, 0, 0, 0],
                          [ 0, 0,-1, 0],
                          [ 0, 1, 0, 0],
                          [ 0, 0, 0, 1]])

_matrix_4_0y0 = np.array([[ 0, 0, 1, 0],
                          [ 0, 1, 0, 0],
                          [-1, 0, 0, 0],
                          [ 0, 0, 0, 1]])

_matrix_4_00z = np.array([[ 0,-1, 0, 0],
                          [ 1, 0, 0, 0],
                          [ 0, 0, 1, 0],
                          [ 0, 0, 0, 1]])


_matrix_m3_xxx   = _matrix_3_xxx   @ _matrix_inv_000
_matrix_m3_xmxmx = _matrix_3_xmxmx @ _matrix_inv_000
_matrix_m3_mxxmx = _matrix_3_mxxmx @ _matrix_inv_000
_matrix_m3_mxmxx = _matrix_3_mxmxx @ _matrix_inv_000

_matrix_m4_x00   = _matrix_4_x00   @ _matrix_inv_000
_matrix_m4_0y0   = _matrix_4_0y0   @ _matrix_inv_000
_matrix_m4_00z   = _matrix_4_00z   @ _matrix_inv_000


matrices = np.array([_matrix_inv_000,

                     _matrix_m_0yz, _matrix_m_x0z, _matrix_m_xy0,
                     _matrix_m_xmxz, _matrix_m_xymy,_matrix_m_xymx,
                     _matrix_m_xyx, _matrix_m_xxz, _matrix_m_xyy,

                     _matrix_2_x00, _matrix_2_0y0, _matrix_2_00z,
                     _matrix_2_xx0, _matrix_2_x0x, _matrix_2_0yy,
                     _matrix_2_xmx0, _matrix_2_mx0x, _matrix_2_0myy,

                     _matrix_3_xxx, _matrix_3_xmxmx,
                     _matrix_3_mxxmx, _matrix_3_mxmxx,

                     _matrix_m3_xxx, _matrix_m3_xmxmx,
                     _matrix_m3_mxxmx, _matrix_m3_mxmxx,

                     _matrix_4_x00, _matrix_4_0y0, _matrix_4_00z,
                     _matrix_m4_x00, _matrix_m4_0y0, _matrix_m4_00z],

                    dtype=int)

# matrices_inverse = np.linalg.inv(matrices[-14:]).astype(int)

_translation_hhh = np.array([[ 0, 0, 0, 1],
                             [ 0, 0, 0, 1],
                             [ 0, 0, 0, 1],
                             [ 0, 0, 0, 0]])

_translation_0hh = np.array([[ 0, 0, 0, 0],
                             [ 0, 0, 0, 1],
                             [ 0, 0, 0, 1],
                             [ 0, 0, 0, 0]])

_translation_h0h = np.array([[ 0, 0, 0, 1],
                             [ 0, 0, 0, 0],
                             [ 0, 0, 0, 1],
                             [ 0, 0, 0, 0]])

_translation_hh0 = np.array([[ 0, 0, 0, 1],
                             [ 0, 0, 0, 1],
                             [ 0, 0, 0, 0],
                             [ 0, 0, 0, 0]])

_translation_00h = np.array([[ 0, 0, 0, 0],
                             [ 0, 0, 0, 0],
                             [ 0, 0, 0, 1],
                             [ 0, 0, 0, 0]])

_translation_0h0 = np.array([[ 0, 0, 0, 0],
                             [ 0, 0, 0, 1],
                             [ 0, 0, 0, 0],
                             [ 0, 0, 0, 0]])

_translation_h00 = np.array([[ 0, 0, 0, 1],
                             [ 0, 0, 0, 0],
                             [ 0, 0, 0, 0],
                             [ 0, 0, 0, 0]])

translations = np.array([
    _translation_h00,
    _translation_0h0,
    _translation_00h,
    _translation_hh0,
    _translation_h0h,
    _translation_0hh,
    _translation_hhh
])

_translation_qqq = np.array([[ 0, 0, 0, 0.5],
                             [ 0, 0, 0, 0.5],
                             [ 0, 0, 0, 0.5],
                             [ 0, 0, 0, 0  ]])


# TODO: separate by translation vector
#  (if there is slide then look for symmetry)


matrices_dict = {
    "inv_000": _matrix_inv_000,

    "m_0yz": _matrix_m_0yz, "m_x0z": _matrix_m_x0z, "m_xy0": _matrix_m_xy0,
    "m_xmxz": _matrix_m_xmxz, "m_xymy": _matrix_m_xymy, "m_xymx": _matrix_m_xymx,
    "m_xyx": _matrix_m_xyx, "m_xxz": _matrix_m_xxz, "m_xyy": _matrix_m_xyy,

    "2_x00": _matrix_2_x00, "2_0y0": _matrix_2_0y0, "2_00z": _matrix_2_00z,
    "2_xx0": _matrix_2_xx0, "2_x0x": _matrix_2_x0x, "2_0yy": _matrix_2_0yy,
    "2_xmx0": _matrix_2_xmx0, "2_mx0x": _matrix_2_mx0x, "2_0myy": _matrix_2_0myy,

    "3_xxx": _matrix_3_xxx, "3_xmxmx": _matrix_3_xmxmx,
    "3_mxxmx": _matrix_3_mxxmx, "3_mxmxx": _matrix_3_mxmxx,

    "m3_xxx": _matrix_m3_xxx, "m3_xmxmx": _matrix_m3_xmxmx,
    "m3_mxxmx": _matrix_m3_mxxmx, "m3_mxmxx": _matrix_m3_mxmxx,

    "4_x00": _matrix_4_x00, "4_0y0": _matrix_4_0y0, "4_00z": _matrix_4_00z,
    "-4_x00": _matrix_m4_x00, "-4_0y0": _matrix_m4_0y0, "-4_00z": _matrix_m4_00z
}

labels = np.array(("inv_000",

                   "m_0yz", "m_x0z", "m_xy0",
                   "m_xmxz", "m_xymy", "m_xymx",
                   "m_xyx", "m_xxz", "m_xyy",

                   "2_x00", "2_0y0", "2_00z",
                   "2_xx0", "2_x0x",  "2_0yy",
                   "2_xmx0","2_mx0x", "2_0myy",

                   "3_xxx", "3_xmxmx",
                   "3_mxxmx", "3_mxmxx",

                   "m3_xxx", "m3_xmxmx",
                   "m3_mxxmx", "m3_mxmxx",

                   "4_x00", "4_0y0", "4_00z",

                   "-4_x00","-4_0y0","-4_00z"))


# Fm-3c

_matrix_4_xmqq = matrices_dict["4_x00"] + _translation_00h #13=14
_matrix_2_0qmyy_0mqq = matrices_dict["2_0myy"] + _translation_00h #15
_matrix_2_0qyy_0qq = matrices_dict["2_0yy"] + _translation_00h #16
_matrix_4_qyq = matrices_dict["4_0y0"] + _translation_00h  #17=18
_matrix_2_1_qmx0x_mq0q = matrices_dict["2_mx0x"] + _translation_00h  #19
_matrix_2_1_mqx0x_q0q = matrices_dict["2_x0x"] + _translation_00h  #20
_matrix_4_2_00z_00h = matrices_dict["4_00z"] + _translation_00h  #21=22
_matrix_2_xmxq = matrices_dict["2_xmx0"] + _translation_00h  #23
_matrix_2_xxq = matrices_dict["2_xx0"] + _translation_00h  #24
_matrix_m4_xqq_0qq = matrices_dict["-4_x00"] + _translation_00h  # 37=38
_matrix_n_xmqyy_0qq = matrices_dict["m_xymy"] + _translation_00h  #39
_matrix_n_xqymy_0mqq = matrices_dict["m_xyy"] + _translation_00h  #40
_matrix_m4_mqyq_mq0q = matrices_dict["-4_0y0"] + _translation_00h  #41=42
_matrix_n_mqxyx_q0q = matrices_dict["m_xyx"] + _translation_00h  #43
_matrix_n_qxymx_mq0q = matrices_dict["m_xymx"] + _translation_00h  #44
_matrix_m4_00z_00q = matrices_dict["-4_00z"] + _translation_00h  #45=46
_matrix_c_xxz_00h = matrices_dict["m_xxz"] + _translation_00h  #47
_matrix_c_xmxz_00h = matrices_dict["m_xmxz"] + _translation_00h  #48

# tA [0,h,h]

_matrix_2_xqq = matrices_dict["2_x00"] + _translation_0hh  #50
_matrix_2_1_0yq_0h0 = matrices_dict["2_0y0"] + _translation_0hh  #51
_matrix_2_1_0qz_00h = matrices_dict["2_00z"] + _translation_0hh  #52
_matrix_3_1_mtmHxx_ttt = matrices_dict["3_xxx"] + _translation_0hh  #53=57
_matrix_3_2_txmHmxmx_mttt = matrices_dict["3_xmxmx"] + _translation_0hh  #54=58
_matrix_3_mxhxmx = matrices_dict["3_mxxmx"] + _translation_0hh  #55=59

_matrix_4_xqq = matrices_dict["4_x00"] + _translation_0h0  #61=62
_matrix_2_1_0qmyy_0qmq = matrices_dict["2_0myy"] + _translation_0h0  #63
_matrix_2_1_0qyy_0qq = matrices_dict["2_0yy"] + _translation_0h0  #64
_matrix_4_2_0y0_0h0 = matrices_dict["4_0y0"] + _translation_0h0  #65=66
_matrix_2_mxqx = matrices_dict["2_mx0x"] + _translation_0h0  #67
_matrix_2_xqx = matrices_dict["2_x0x"] + _translation_0h0  #68
_matrix_4_mqqz = matrices_dict["4_00z"] + _translation_0h0  #69=70
_matrix_2_1_xqmx0_mqq0 = matrices_dict["2_xmx0"] + _translation_0h0  #71
_matrix_2_1_xqx0_qq0 = matrices_dict["2_xx0"] + _translation_0h0  #72

_matrix_inv_0qq = matrices_dict["inv_000"] + _translation_0hh  #73
_matrix_n_0yz_0hh = matrices_dict["m_0yz"] + _translation_0hh  #74
_matrix_c_xqz_00h = matrices_dict["m_x0z"] + _translation_0hh  #75
_matrix_b_xyq_0h0 = matrices_dict["m_xy0"] + _translation_0hh  #76
_matrix_m3_xhxx_0h0 = matrices_dict["m3_xxx"] + _translation_0hh  #77=81
_matrix_m3_xhmxmx_0h0 = matrices_dict["m3_xmxmx"] + _translation_0hh  #78=82
_matrix_m3_m1mxhxmx_mh0h = matrices_dict["m3_mxxmx"] + _translation_0hh  #79=83
_matrix_m3_1mxhmxx_h0h = matrices_dict["m3_mxmxx"] + _translation_0hh  #80=84

_matrix_m4_xqmq_0qmq = matrices_dict["-4_x00"] + _translation_0h0  #85=86
_matrix_n_xqyy_0qq = matrices_dict["m_xyy"] + _translation_0h0  #87
_matrix_n_xqymy_0qmq = matrices_dict["m_xymy"] + _translation_0h0  #88
_matrix_m4_0y0_0q0 = matrices_dict["-4_0y0"] + _translation_0h0  #89=90
_matrix_b_xyx_0h0 = matrices_dict["m_xyx"] + _translation_0h0  #91
_matrix_b_xymx_0h0 = matrices_dict["m_xymx"] + _translation_0h0  #92
_matrix_n_mqxxz_qq0 = matrices_dict["m_xxz"] + _translation_0h0  #95
_matrix_n_qxmxz_mqq0 = matrices_dict["m_xmxz"] + _translation_0h0  #96


# tB [h,0,h]  #97
_matrix_2_1_x0q_h00 = matrices_dict["2_x00"] + _translation_h0h  #98
_matrix_2_qyq = matrices_dict["2_0y0"] + _translation_h0h  #99
_matrix_2_1_q0z_00h = matrices_dict["2_00z"] + _translation_h0h  #100
_matrix_3_1_HxmHxx_ttt = matrices_dict["3_xxx"] + _translation_h0h  #101=105
_matrix_3_hxmhmxmx = matrices_dict["3_xmxmx"] + _translation_h0h  #102=106
_matrix_3_2_HmxHxmx_tmtt = matrices_dict["3_mxxmx"] + _translation_h0h  #103=107
_matrix_3_hmxhmxx = matrices_dict["3_mxmxx"] + _translation_h0h  #104=108

_matrix_4_2_x00_h00 = matrices_dict["4_x00"] + _translation_h00  #109=110
_matrix_2_qmyy = matrices_dict["2_0myy"] + _translation_h00  #111
_matrix_2_qyy = matrices_dict["2_0yy"] + _translation_h00  #112
_matrix_4_qymq = matrices_dict["4_0y0"] + _translation_h00  #113=114
_matrix_2_1_qmx0x_q0mq = matrices_dict["2_mx0x"] + _translation_h00  #115
_matrix_2_1_qx0x_q0mq = matrices_dict["2_x0x"] + _translation_h00  #116
_matrix_4_qqz = matrices_dict["4_00z"] + _translation_h00  #117=118
_matrix_2_1_xqmx0_qmq0 = matrices_dict["2_xmx0"] + _translation_h00  #119
_matrix_2_1_xmqx0_qq0 = matrices_dict["2_xx0"] + _translation_h00  #120

_matrix_inv_q0q = matrices_dict["inv_000"] + _translation_h0h  #121
_matrix_n_qyz_00h = matrices_dict["m_0yz"] + _translation_h0h  #122
_matrix_n_x0z_h0h = matrices_dict["m_x0z"] + _translation_h0h  #123
_matrix_a_xyq_h00 = matrices_dict["m_xy0"] + _translation_h0h  #124
_matrix_m3_mhxmhxx_00h = matrices_dict["m3_xxx"] + _translation_h0h  #125=129
_matrix_m3_hxhmxmx_hh0 = matrices_dict["m3_xmxmx"] + _translation_h0h  #126=130
_matrix_m3_hmxhxmx_00h = matrices_dict["m3_mxxmx"] + _translation_h0h  #127=131
_matrix_m3_hmxmhmxx_hmh0 = matrices_dict["m3_mxmxx"] + _translation_h0h #128=132

_matrix_m4_x00_q00 = matrices_dict["-4_x00"] + _translation_h00  #133=134
_matrix_a_xyy_h00 = matrices_dict["m_xyy"] + _translation_h00  #135
_matrix_a_xymy_h00 = matrices_dict["m_xymy"] + _translation_h00  #136
_matrix_m4_qyq_q0q = matrices_dict["-4_0y0"] + _translation_h00  #137=138
_matrix_n_qxymx_q0q = matrices_dict["m_xyx"] + _translation_h00  #139
_matrix_n_qxymx_q0mq = matrices_dict["m_xymx"] + _translation_h00  #140
_matrix_m4_qmqz_qmq0 = matrices_dict["-4_00z"] + _translation_h00  #141=142
_matrix_n_qxxz_qq0 = matrices_dict["m_xxz"] + _translation_h00  #143
_matrix_n_qxmxz_qmq0 = matrices_dict["m_xmxz"] + _translation_h00 #144


# tC [h,h,0]  #145
_matrix_2_1_xq0_h00 = matrices_dict["2_x00"] + _translation_hh0  #146
_matrix_2_1_qy0_0h0 = matrices_dict["2_0y0"] + _translation_hh0  #147
_matrix_2_qqz = matrices_dict["2_00z"] + _translation_hh0  #148

_matrix_3_1_Hxtxx_ttt = matrices_dict["3_xxx"] + _translation_hh0  #149=153
_matrix_3_hxmxmx = matrices_dict["3_xmxmx"] + _translation_hh0  #150=154
_matrix_3_hmxxmx = matrices_dict["3_mxxmx"] + _translation_hh0  #151=155
_matrix_3_2_Hmxtmxx_ttmt = matrices_dict["3_mxmxx"] + _translation_hh0  #152=156

_matrix_4_2_x0h_h00 = matrices_dict["4_x00"] + _translation_hhh  #157=158
_matrix_2_qhmyy = matrices_dict["2_0myy"] + _translation_hhh  #159
_matrix_2_1_qyy_0hh = matrices_dict["2_0yy"] + _translation_hhh  #160 dupa
_matrix_4_qy0_0h0 = matrices_dict["4_0y0"] + _translation_hhh  #161=162
_matrix_2_hmxqx = matrices_dict["2_mx0x"] + _translation_hhh  #163
_matrix_2_1_xqx_q0q = matrices_dict["2_x0x"] + _translation_hhh  #164
_matrix_4_2_0hz_00h = matrices_dict["4_00z"] + _translation_hhh  #165=166
_matrix_2_xhmxq = matrices_dict["2_xmx0"] + _translation_hhh  #167
_matrix_2_1_xxq_hh0 = matrices_dict["2_xx0"] + _translation_hhh  #168

_matrix_inv_qq0 = matrices_dict["inv_000"] + _translation_hh0  #169
_matrix_b_qyz_0h0 = matrices_dict["m_0yz"] + _translation_hh0  #170
_matrix_a_xqz_h00 = matrices_dict["m_x0z"] + _translation_hh0  #171
_matrix_n_xy0_hh0 = matrices_dict["m_xy0"] + _translation_hh0  #172
_matrix_m3_mhxxx_h00 = matrices_dict["m3_xxx"] + _translation_hh0  #173=177
_matrix_m3_mhx1mxmx_0hmh = matrices_dict["m3_xmxmx"] + _translation_hh0 #174=178
_matrix_m3_mhmx1xmx_0hh = matrices_dict["m3_mxxmx"] + _translation_hh0  #175=179
_matrix_m3_hmxmxx_h00 = matrices_dict["m3_mxmxx"] + _translation_hh0 #176=180

_matrix_m4_xh0_qh0 = matrices_dict["-4_x00"] + _translation_hhh  #181=182
_matrix_n_xyy_hhh = matrices_dict["m_xyy"] + _translation_hhh  #183
_matrix_a_xhymy_h00 = matrices_dict["m_xymy"] + _translation_hhh  #184
_matrix_m4_0yh_0qh = matrices_dict["-4_0y0"] + _translation_hhh  #185=186
_matrix_n_xyx_hhh = matrices_dict["m_xyx"] + _translation_hhh  #187
_matrix_b_hxymx_0h0 = matrices_dict["m_xymx"] + _translation_hhh  #188
_matrix_m4_h0z_h0q = matrices_dict["-4_00z"] + _translation_hhh  #189=190
_matrix_n_xxz_hhh = matrices_dict["m_xxz"] + _translation_hhh  #191
_matrix_c_hxmxz_00h = matrices_dict["m_xmxz"] + _translation_hhh #192


# Im-3m

# tI [h,h,h]

_matrix_2_1_xqq_h00 = matrices_dict["2_x00"] + _translation_hhh  #50
_matrix_2_1_qyq_0h0 = matrices_dict["2_0y0"] + _translation_hhh  #51
_matrix_2_1_qqz_00h = matrices_dict["2_00z"] + _translation_hhh  #52
_matrix_3_xxx_hhh = matrices_dict["3_xxx"] + _translation_hhh  #53=57
_matrix_3_2_2txmtmxmx_mHHH = matrices_dict["3_xmxmx"] + _translation_hhh  #54=58
_matrix_3_2_tmxtxmx_HmHH = matrices_dict["3_mxxmx"] + _translation_hhh  #55=59
_matrix_3_2_tmx2tmxx_HHmH = matrices_dict["3_mxmxx"] + _translation_hhh  #56=60
_matrix_inv_qqq = matrices_dict["inv_000"] + _translation_hhh  #73
_matrix_n_qyz_0hh = matrices_dict["m_0yz"] + _translation_hhh  #74
_matrix_n_xqz_h0h = matrices_dict["m_x0z"] + _translation_hhh  #75
_matrix_n_xyq_hh0 = matrices_dict["m_xy0"] + _translation_hhh  #76
_matrix_m3_xxx_qqq = matrices_dict["m3_xxx"] + _translation_hhh  #77=81
_matrix_m3_xmxmx_q3qmq = matrices_dict["m3_xmxmx"] + _translation_hhh  #78=82
_matrix_m3_mxxmx_mqq3q = matrices_dict["m3_mxxmx"] + _translation_hhh  #79=83
_matrix_m3_mxmxx_3qmqq = matrices_dict["m3_mxmxx"] + _translation_hhh  #80=84


# Fddd

_matrix_d_oyz_0qq = matrices_dict["m_0yz"] + _translation_qqq
_matrix_d_xoz_q0q = matrices_dict["m_x0z"] + _translation_qqq
_matrix_d_xyo_qq0 = matrices_dict["m_xy0"] + _translation_qqq
_matrix_inv_ooo   = matrices_dict["inv_000"] + _translation_qqq

_matrix_d_oyz_03q3q = matrices_dict["m_0yz"] + _translation_qqq + _translation_0hh
_matrix_d_x3oz_q03q = matrices_dict["m_x0z"] + _translation_qqq + _translation_0hh
_matrix_d_xy3o_q3q0 = matrices_dict["m_xy0"] + _translation_qqq + _translation_0hh
_matrix_inv_o3o3o   = matrices_dict["inv_000"] + _translation_qqq + _translation_0hh

_matrix_d_3oyz_0q3q = matrices_dict["m_0yz"] + _translation_qqq + _translation_h0h
_matrix_d_xoz_3q03q = matrices_dict["m_x0z"] + _translation_qqq + _translation_h0h
_matrix_dxy3o_3qq0  = matrices_dict["m_xy0"] + _translation_qqq + _translation_h0h
_matrix_inv_3oo3o   = matrices_dict["inv_000"] + _translation_qqq + _translation_h0h

_matrix_d_3oyz_03qq = matrices_dict["m_0yz"] + _translation_qqq + _translation_hh0
_matrix_d_x3oz_3q0q = matrices_dict["m_x0z"] + _translation_qqq + _translation_hh0
_matrix_d_xyo_3q3q0 = matrices_dict["m_xy0"] + _translation_qqq + _translation_hh0
_matrix_inv_3o3oo   = matrices_dict["inv_000"] + _translation_qqq + _translation_hh0


#Ia-3d

_matrix_2_x0q = matrices_dict["2_x00"] + _translation_00h  #2
_matrix_2_qy0 = matrices_dict["2_0y0"] + _translation_h00  #3
_matrix_2_0qz = matrices_dict["2_00z"] + _translation_0h0  #4

_matrix_3_2_HxHmxmx_mHHH = matrices_dict["3_xmxmx"] + _translation_0h0  #6=10
_matrix_3_2_mHmxtxmx_HmHH = matrices_dict["3_mxxmx"] + _translation_00h  #7=11
_matrix_3_2_tmxHmxx_HHmH = matrices_dict["3_mxmxx"] + _translation_h00  #8=12

_matrix_4_1_xmqh_q00 = matrices_dict["4_x00"] + _translation_qqq + _translation_00h  #13=14
_matrix_2_oqmyy = matrices_dict["2_0myy"] + _translation_qqq  #15
_matrix_2_1_3omqyy_0hh = matrices_dict["2_0yy"] + _translation_qqq + _translation_h0h  #16
_matrix_4_3_hyq_03q0 = matrices_dict["4_0y0"] + _translation_qqq + _translation_0hh  #17
_matrix_2_qmxox = matrices_dict["2_mx0x"] + _translation_qqq  #19
_matrix_2_1_qx3ox_h0h = matrices_dict["2_x0x"] + _translation_qqq + _translation_hh0  #20
_matrix_4_3_qhz_003q = matrices_dict["4_00z"] + _translation_qqq + _translation_h0h  #21
_matrix_2_xqmxo = matrices_dict["2_xmx0"] + _translation_qqq  #23
_matrix_2_1_xmqxo_hh0 = matrices_dict["2_xx0"] + _translation_qqq + _translation_h00  #24
_matrix_c_0yz_00h = matrices_dict["m_0yz"] + _translation_00h  #26
_matrix_a_x0z_h00 = matrices_dict["m_x0z"] + _translation_h00  #27
_matrix_b_xy0_0h0 = matrices_dict["m_xy0"] + _translation_0h0  #28
_matrix_m3_mhxhmxmx_mqqmq = matrices_dict["m3_xmxmx"] + _translation_0h0  #30=34
_matrix_m3_mhmxxmx_mqmqq = matrices_dict["m3_mxxmx"] + _translation_00h  #31=35
_matrix_m3_mxmhmxx_qmqmq = matrices_dict["m3_mxmxx"] + _translation_h00  #32=36
_matrix_m4_xhq_ohq = matrices_dict["-4_x00"] + _translation_qqq + _translation_00h  #37=38
_matrix_d_xyy_qqq = matrices_dict["m_xyy"] + _translation_qqq  #39
_matrix_d_xhymy_3qmqq = matrices_dict["m_xymy"] + _translation_qqq + _translation_h0h  #40
_matrix_m4_mqyh_mq3oh = matrices_dict["-4_0y0"] + _translation_qqq + _translation_0hh  #41=42
_matrix_d_xyx_qqq = matrices_dict["m_xyx"] + _translation_qqq  #43
_matrix_d_hxymx_q3qmq = matrices_dict["m_xymx"] + _translation_qqq + _translation_hh0  #44
_matrix_m4_hmqz_hmq3o = matrices_dict["-4_00z"] + _translation_qqq + _translation_h0h  #45=46
_matrix_d_xxz_qqq = matrices_dict["m_xxz"] + _translation_qqq  #47
_matrix_d_hxmxz_qmqq = matrices_dict["m_xmxz"] + _translation_qqq + _translation_h00  #48

# tI[h,h,h]
_matrix_3_mxhmxx = matrices_dict["3_mxmxx"] + _translation_0hh  #56=60
_matrix_4_3_xqh_3q00 = matrices_dict["4_x00"] + _translation_qqq + _translation_hh0  #61
_matrix_2_3o3qmyy = matrices_dict["2_0myy"] + _translation_qqq + _translation_hhh  #63
_matrix_2_1_oqyy_0hh = matrices_dict["2_0yy"] + _translation_qqq + _translation_0h0  #64
_matrix_4_1_hymq_0q0 = matrices_dict["4_0y0"] + _translation_qqq + _translation_h00  #65
_matrix_2_3qmx3ox = matrices_dict["2_mx0x"] + _translation_qqq + _translation_hhh  #67
_matrix_2_1_mqxox_h0h = matrices_dict["2_x0x"] + _translation_qqq + _translation_00h  #68
_matrix_4_1_mqhz_00q = matrices_dict["4_00z"] + _translation_qqq + _translation_0h0  #69
_matrix_2_x3qmx3o = matrices_dict["2_xmx0"] + _translation_qqq + _translation_hhh  #71
_matrix_2_1_xqx3o_hh0 = matrices_dict["2_xx0"] + _translation_qqq + _translation_0hh  #72
_matrix_m4_xhmq_3ohmq = matrices_dict["-4_x00"] + _translation_qqq + _translation_hh0  #85
_matrix_d_xyy_3q3q3q = matrices_dict["m_xyy"] + _translation_qqq + _translation_hhh  #87
_matrix_d_xhymy_qqmq = matrices_dict["m_xyy"] + _translation_qqq + _translation_0h0  #88
_matrix_m4_qyh_qoh = matrices_dict["-4_0y0"] + _translation_qqq + _translation_h00  #89
_matrix_d_xyx_3q3q3q = matrices_dict["m_xyx"] + _translation_qqq + _translation_hhh  #91
_matrix_d_hxymx_mqqq = matrices_dict["m_xymx"] + _translation_qqq + _translation_00h  #92
_matrix_m4_hqz_hqo = matrices_dict["-4_00z"] + _translation_qqq + _translation_0h0  #93
_matrix_d_xxz_3q3q3q = matrices_dict["m_xxz"] + _translation_qqq + _translation_00h  #95
_matrix_d_hxmxz_mqq3q = matrices_dict["m_xmxz"] + _translation_qqq + _translation_0hh  #96

# Fd-3c

_matrix_4_1_x0q_q00 = matrices_dict["4_x00"] + _translation_qqq  #13
_matrix_2_1_oyy_0qq = matrices_dict["2_0yy"] + _translation_qqq  #16
_matrix_4_1_qy0_0q0 = matrices_dict["4_0y0"] + _translation_qqq  #18
_matrix_2_1_xox_q0q = matrices_dict["2_x0x"] + _translation_qqq  #20
_matrix_4_1_0qz_00q = matrices_dict["4_00z"] + _translation_qqq  #21=22
_matrix_2_1_xxo_qq0 = matrices_dict["2_xx0"] + _translation_qqq  #24
_matrix_inv_oo3o = matrices_dict["inv_000"] + _translation_qqq + _translation_00h  #25
_matrix_d_oyz_0q3q = matrices_dict["m_0yz"] + _translation_qqq + _translation_00h  #26
_matrix_d_xoz_q03q = matrices_dict["m_x0z"] + _translation_qqq + _translation_00h  #27
_matrix_d_xy3o_qq0 = matrices_dict["m_xy0"] + _translation_qqq + _translation_00h  #28
_matrix_m3_mhxxx_mo3o3o = matrices_dict["m3_xxx"] + _translation_qqq + _translation_00h  #29=33
_matrix_m3_hxhmxmx_3o5oo = matrices_dict["m3_xmxmx"] + _translation_qqq + _translation_00h  #30=34
_matrix_m3_m1mxhxmx_m3omo5o = matrices_dict["m3_mxxmx"] + _translation_qqq + _translation_00h  #31=35
_matrix_m3_1mxmxx_5om3o3o = matrices_dict["m3_mxmxx"] + _translation_qqq + _translation_00h  #32=36

# tA[0,h,h]
_matrix_4_1_x03q_q00 = matrices_dict["4_x00"] + _translation_qqq + _translation_0hh  #61=62
_matrix_2_o3qmyy = matrices_dict["2_0myy"] + _translation_qqq + _translation_0hh  #63
_matrix_2_1_oyy_03q3q = matrices_dict["2_0yy"] + _translation_qqq + _translation_0hh  #64
_matrix_2_1_hmx3ox_mq0q = matrices_dict["2_mx0x"] + _translation_qqq + _translation_0hh  #67
_matrix_2_1_mqx3ox_h0h = matrices_dict["2_x0x"] + _translation_qqq + _translation_0hh  #68
_matrix_4_3_mqhz_003q = matrices_dict["4_00z"] + _translation_qqq + _translation_0hh  #69=70
_matrix_2_1_xhmx3o_mqq0 = matrices_dict["2_xmx0"] + _translation_qqq + _translation_0hh  #71
_matrix_inv_o3oo = matrices_dict["inv_000"] + _translation_qqq + _translation_0h0  #73
_matrix_d_oyz_03qq = matrices_dict["m_0yz"] + _translation_qqq + _translation_0h0  #74
_matrix_d_x3oz_q0q = matrices_dict["m_x0z"] + _translation_qqq + _translation_0h0  #75
_matrix_d_xyo_q3q0 = matrices_dict["m_xy0"] + _translation_qqq + _translation_0h0  #76
_matrix_m3_hxhxx_3o3omo = matrices_dict["m3_xxx"] + _translation_qqq + _translation_0h0  #77=81
_matrix_m3_mhx1mxmx_mo5om3o = matrices_dict["m3_xmxmx"] + _translation_qqq + _translation_0h0  #78=82
_matrix_m3_m1mx1xmx_m3o3o5o = matrices_dict["m3_mxxmx"] + _translation_qqq + _translation_0h0  #79=83
_matrix_m3_1mxhmxx_5oo3o = matrices_dict["m3_mxmxx"] + _translation_qqq + _translation_0h0  #80=84
_matrix_m4_qqz_qq0 = matrices_dict["-4_00z"] + _translation_0h0  #93=94

# tB[h,0,h]
_matrix_4_3_xmqh_3q00 = matrices_dict["4_x00"] + _translation_qqq + _translation_h0h  #109=110
_matrix_2_1_3ohmyy_0mqq = matrices_dict["2_0yy"] + _translation_qqq + _translation_h0h  #111
_matrix_4_1_3qy0_0q0 = matrices_dict["4_0y0"] + _translation_h0h  #113=114
_matrix_2_3qmxox = matrices_dict["2_mx0x"] + _translation_qqq + _translation_h0h  #115
_matrix_2_1_xox_3q03q = matrices_dict["2_x0x"] + _translation_qqq + _translation_h0h  #116
_matrix_2_1_xhmx3o_qmq0 = matrices_dict["2_xmx0"] + _translation_qqq + _translation_h0h  #119
_matrix_2_1_xmqx3o_hh0 = matrices_dict["2_xx0"] + _translation_qqq + _translation_h0h  #120
_matrix_inv_3ooo = matrices_dict["inv_000"] + _translation_qqq + _translation_h00  #121
_matrix_d_3oyz_0qq = matrices_dict["m_0yz"] + _translation_qqq + _translation_h00  #122
_matrix_d_xoz_3q0q = matrices_dict["m_x0z"] + _translation_qqq + _translation_h00  #123
_matrix_d_xyo_3qq0 = matrices_dict["m_xy0"] + _translation_qqq + _translation_h00  #124
_matrix_m3_xmhxx_3omo3o = matrices_dict["m3_xxx"] + _translation_qqq + _translation_h00  #125=129
_matrix_m3_x1mxmx_3o5om3o = matrices_dict["m3_xmxmx"] + _translation_qqq + _translation_h00  #126=130
_matrix_m3_mhmx1xmx_o3o5o = matrices_dict["m3_mxxmx"] + _translation_qqq + _translation_h00  #127=131
_matrix_m3_hmxmhmxx_5om3omo = matrices_dict["m3_mxmxx"] + _translation_qqq + _translation_h00  #128=132

# tC[h,h,0]
_matrix_2_1_3ohmyy_0qmq = matrices_dict["2_0myy"] + _translation_qqq + _translation_hh0  #159
_matrix_2_1_3oqyy_0hh = matrices_dict["2_0yy"] + _translation_qqq + _translation_hh0  #160
_matrix_4_3_hymq_03q0 = matrices_dict["4_0y0"] + _translation_qqq + _translation_hh0  #161=162
_matrix_2_1_hmx3ox_q0mq = matrices_dict["2_mx0x"] + _translation_qqq + _translation_hh0  #163
_matrix_4_1_03qz_00q = matrices_dict["4_00z"] + _translation_qqq + _translation_hh0  #165=166
_matrix_2_x3qmxo = matrices_dict["2_xmx0"] + _translation_qqq + _translation_hh0  #167
_matrix_2_1_xxo_3q3qo = matrices_dict["2_xx0"] + _translation_qqq + _translation_hh0  #168
_matrix_inv_3o3o3o = matrices_dict["inv_000"] + _translation_qqq + _translation_hhh  #169
_matrix_d_3oyz_03q3q = matrices_dict["m_0yz"] + _translation_qqq + _translation_hhh  #170
_matrix_d_x3oz_3q03q = matrices_dict["m_x0z"] + _translation_qqq + _translation_hhh  #171
_matrix_d_xy3o_3q3q0 = matrices_dict["m_xy0"] + _translation_qqq + _translation_hhh  #172
_matrix_m3_xxx_3o3o3o = matrices_dict["m3_xxx"] + _translation_qqq + _translation_hhh  #173=177
_matrix_m3_xhmxmx_3oom3o = matrices_dict["m3_xmxmx"] + _translation_qqq + _translation_hhh  #174=178
_matrix_m3_mhmxhxmx_m3o3oo = matrices_dict["m3_mxxmx"] + _translation_qqq + _translation_hhh  #175=179
_matrix_m3_hmxmxx_om3o3o = matrices_dict["m3_mxmxx"] + _translation_qqq + _translation_hhh  #176=180

# P2_1
_matrix_2_1_0y0_0h0 = matrices_dict["2_0y0"] + _translation_0h0  #2

# rest unscripted 'full_list'

_matrix_inv_h00_un = matrices_dict["inv_000"] + _translation_h00 #0
_matrix_m_0yz_h00_un = matrices_dict["m_0yz"] + _translation_h00 #1
_matrix_m_xy0_h00_un = matrices_dict["m_xy0"] + _translation_h00 #3
_matrix_2_x00_h00_un = matrices_dict["2_x00"] + _translation_h00 #10
_matrix_2_00z_h00_un = matrices_dict["2_00z"] + _translation_h00 #12
# _matrix_inv_0h0_un = matrices_dict[""] + _translation_
# _matrix_ = matrices_dict[""] + _translation_
# _matrix_ = matrices_dict[""] + _translation_
# _matrix_ = matrices_dict[""] + _translation_
# _matrix_ = matrices_dict[""] + _translation_
# _matrix_ = matrices_dict[""] + _translation_
# _matrix_ = matrices_dict[""] + _translation_
# _matrix_ = matrices_dict[""] + _translation_

# _matrix_inv_000_h00 = matrices_dict["inv_000"] + _translation_h00  #0 0
# _matrix_m_0yz_h00 = matrices_dict["m_0yz"] + _translation_h00  #1 1
# _matrix_m_xy0_h00 = matrices_dict["m_xy0"] + _translation_h00  #3 3
# _matrix_2_x00_h00 = matrices_dict["2_x00"] + _translation_h00  #10 10
# _matrix_2_00z_h00 = matrices_dict["2_00z"] + _translation_h00  #12 12
# _matrix_inv_000_0h0 = matrices_dict["inv_000"] + _translation_0h0  #15 15
# _matrix_m_0yz_0h0 = matrices_dict["m_0yz"] + _translation_0h0  #16 16
# _matrix_m_x0z_0h0 = matrices_dict["m_x0z"] + _translation_0h0  #17 17
# _matrix_2_x00_0h0 = matrices_dict["2_x00"] + _translation_0h0  #25 25
# _matrix_inv_000_00h = matrices_dict["inv_000"] + _translation_00h  #30 30
# _matrix_m_x0z_00h = matrices_dict["m_x0z"] + _translation_00h  #32 32
# _matrix_m_xy0_00h = matrices_dict["m_xy0"] + _translation_00h  #33 33
# _matrix_2_0y0_00h = matrices_dict["2_0y0"] + _translation_00h  #41 41
# _matrix_2_00z_00h = matrices_dict["2_00z"] + _translation_00h  #42 42
# _matrix_m_xmxz_0hh = matrices_dict["m_xmxz"] + _translation_0hh  #49 49
# _matrix_m_xymy_0hh = matrices_dict["m_xymy"] + _translation_0hh  #50 50
# _matrix_m_xymx_0hh = matrices_dict["m_xymx"] + _translation_0hh  #51 51
# _matrix_m_xyx_0hh = matrices_dict["m_xyx"] + _translation_0hh  #52 52
# _matrix_m_xxz_0hh = matrices_dict["m_xxz"] + _translation_0hh  #53 53
# _matrix_m_xyy_0hh = matrices_dict["m_xyy"] + _translation_0hh  #54 54
# _matrix_2_xx0_0hh = matrices_dict["2_xx0"] + _translation_0hh  #58 58
# _matrix_2_x0x_0hh = matrices_dict["2_x0x"] + _translation_0hh  #59 59
# _matrix_m_xmxz_h0h = matrices_dict["m_xmxz"] + _translation_h0h  #64 64
# _matrix_m_xymy_h0h = matrices_dict["m_xymy"] + _translation_h0h  #65 65
# _matrix_m_xymx_h0h = matrices_dict["m_xymx"] + _translation_h0h  #66 66
# _matrix_m_xyx_h0h = matrices_dict["m_xyx"] + _translation_h0h  #67 67
# _matrix_m_xxz_h0h = matrices_dict["m_xxz"] + _translation_h0h  #68 68
# _matrix_m_xyy_h0h = matrices_dict["m_xyy"] + _translation_h0h  #69 69
# _matrix_2_xx0_h0h = matrices_dict["2_xx0"] + _translation_h0h  #73 73
# _matrix_2_x0x_h0h = matrices_dict["2_x0x"] + _translation_h0h  #74 74
# _matrix_m_xmxz_hh0 = matrices_dict["m_xmxz"] + _translation_hh0  #79 79
# _matrix_m_xymy_hh0 = matrices_dict["m_xymy"] + _translation_hh0  #80 80
# _matrix_m_xymx_hh0 = matrices_dict["m_xymx"] + _translation_hh0  #81 81
# _matrix_m_xyx_hh0 = matrices_dict["m_xyx"] + _translation_hh0  #82 82
# _matrix_m_xxz_hh0 = matrices_dict["m_xxz"] + _translation_hh0  #83 83
# _matrix_m_xyy_hh0 = matrices_dict["m_xyy"] + _translation_hh0  #84 84
# _matrix_2_xx0_hh0 = matrices_dict["2_xx0"] + _translation_hh0  #88 88
# _matrix_2_x0x_hh0 = matrices_dict["2_x0x"] + _translation_hh0  #89 89
# _matrix_m_xmxz_qqq = matrices_dict["m_xmxz"] + _translation_qqq  #109 109
# _matrix_m_xymy_qqq = matrices_dict["m_xymy"] + _translation_qqq  #110 110
# _matrix_m_xymx_qqq = matrices_dict["m_xymx"] + _translation_qqq  #111 111
# _matrix_2_x00_qqq = matrices_dict["2_x00"] + _translation_qqq  #115 115
# _matrix_2_0y0_qqq = matrices_dict["2_0y0"] + _translation_qqq  #116 116
# _matrix_2_00z_qqq = matrices_dict["2_00z"] + _translation_qqq  #117 117
# _matrix_m_xymy_3qqq = matrices_dict["m_xymy"] + _translation_3qqq  #125 125
# _matrix_m_xymx_3qqq = matrices_dict["m_xymx"] + _translation_3qqq  #126 126
# _matrix_m_xyx_3qqq = matrices_dict["m_xyx"] + _translation_3qqq  #127 127
# _matrix_m_xxz_3qqq = matrices_dict["m_xxz"] + _translation_3qqq  #128 128
# _matrix_m_xyy_3qqq = matrices_dict["m_xyy"] + _translation_3qqq  #129 129
# _matrix_2_x00_3qqq = matrices_dict["2_x00"] + _translation_3qqq  #130 130
# _matrix_2_0y0_3qqq = matrices_dict["2_0y0"] + _translation_3qqq  #131 131
# _matrix_2_00z_3qqq = matrices_dict["2_00z"] + _translation_3qqq  #132 132
# _matrix_2_x0x_3qqq = matrices_dict["2_x0x"] + _translation_3qqq  #134 134
# _matrix_m_xmxz_q3qq = matrices_dict["m_xmxz"] + _translation_q3qq  #139 139
# _matrix_m_xymy_q3qq = matrices_dict["m_xymy"] + _translation_q3qq  #140 140
# _matrix_m_xymx_q3qq = matrices_dict["m_xymx"] + _translation_q3qq  #141 141
# _matrix_m_xyx_q3qq = matrices_dict["m_xyx"] + _translation_q3qq  #142 142
# _matrix_m_xxz_q3qq = matrices_dict["m_xxz"] + _translation_q3qq  #143 143
# _matrix_2_x00_q3qq = matrices_dict["2_x00"] + _translation_q3qq  #145 145
# _matrix_2_0y0_q3qq = matrices_dict["2_0y0"] + _translation_q3qq  #146 146
# _matrix_2_00z_q3qq = matrices_dict["2_00z"] + _translation_q3qq  #147 147
# _matrix_2_xx0_q3qq = matrices_dict["2_xx0"] + _translation_q3qq  #148 148
# _matrix_2_x0x_q3qq = matrices_dict["2_x0x"] + _translation_q3qq  #149 149
# _matrix_m_xmxz_qq3q = matrices_dict["m_xmxz"] + _translation_qq3q  #154 154
# _matrix_m_xymy_qq3q = matrices_dict["m_xymy"] + _translation_qq3q  #155 155
# _matrix_m_xyx_qq3q = matrices_dict["m_xyx"] + _translation_qq3q  #157 157
# _matrix_m_xyy_qq3q = matrices_dict["m_xyy"] + _translation_qq3q  #159 159
# _matrix_2_x00_qq3q = matrices_dict["2_x00"] + _translation_qq3q  #160 160
# _matrix_2_0y0_qq3q = matrices_dict["2_0y0"] + _translation_qq3q  #161 161
# _matrix_2_00z_qq3q = matrices_dict["2_00z"] + _translation_qq3q  #162 162
# _matrix_2_xx0_qq3q = matrices_dict["2_xx0"] + _translation_qq3q  #163 163
# _matrix_m_xymy_q3q3q = matrices_dict["m_xymy"] + _translation_q3q3q  #170 170
# _matrix_m_xymx_q3q3q = matrices_dict["m_xymx"] + _translation_q3q3q  #171 171
# _matrix_m_xyx_q3q3q = matrices_dict["m_xyx"] + _translation_q3q3q  #172 172
# _matrix_m_xxz_q3q3q = matrices_dict["m_xxz"] + _translation_q3q3q  #173 173
# _matrix_m_xyy_q3q3q = matrices_dict["m_xyy"] + _translation_q3q3q  #174 174
# _matrix_2_x00_q3q3q = matrices_dict["2_x00"] + _translation_q3q3q  #175 175
# _matrix_2_0y0_q3q3q = matrices_dict["2_0y0"] + _translation_q3q3q  #176 176
# _matrix_2_00z_q3q3q = matrices_dict["2_00z"] + _translation_q3q3q  #177 177
# _matrix_m_xmxz_3qq3q = matrices_dict["m_xmxz"] + _translation_3qq3q  #184 184
# _matrix_m_xymx_3qq3q = matrices_dict["m_xymx"] + _translation_3qq3q  #186 186
# _matrix_m_xyx_3qq3q = matrices_dict["m_xyx"] + _translation_3qq3q  #187 187
# _matrix_m_xxz_3qq3q = matrices_dict["m_xxz"] + _translation_3qq3q  #188 188
# _matrix_m_xyy_3qq3q = matrices_dict["m_xyy"] + _translation_3qq3q  #189 189
# _matrix_2_x00_3qq3q = matrices_dict["2_x00"] + _translation_3qq3q  #190 190
# _matrix_2_0y0_3qq3q = matrices_dict["2_0y0"] + _translation_3qq3q  #191 191
# _matrix_2_00z_3qq3q = matrices_dict["2_00z"] + _translation_3qq3q  #192 192
# _matrix_m_xmxz_3q3qq = matrices_dict["m_xmxz"] + _translation_3q3qq  #199 199
# _matrix_m_xymy_3q3qq = matrices_dict["m_xymy"] + _translation_3q3qq  #200 200
# _matrix_m_xyx_3q3qq = matrices_dict["m_xyx"] + _translation_3q3qq  #202 202
# _matrix_m_xxz_3q3qq = matrices_dict["m_xxz"] + _translation_3q3qq  #203 203
# _matrix_m_xyy_3q3qq = matrices_dict["m_xyy"] + _translation_3q3qq  #204 204
# _matrix_2_x00_3q3qq = matrices_dict["2_x00"] + _translation_3q3qq  #205 205
# _matrix_2_0y0_3q3qq = matrices_dict["2_0y0"] + _translation_3q3qq  #206 206
# _matrix_2_00z_3q3qq = matrices_dict["2_00z"] + _translation_3q3qq  #207 207
# _matrix_m_xmxz_3q3q3q = matrices_dict["m_xmxz"] + _translation_3q3q3q  #214 214
# _matrix_m_xymy_3q3q3q = matrices_dict["m_xymy"] + _translation_3q3q3q  #215 215
# _matrix_m_xymx_3q3q3q = matrices_dict["m_xymx"] + _translation_3q3q3q  #216 216
# _matrix_m_xxz_3q3q3q = matrices_dict["m_xxz"] + _translation_3q3q3q  #218 218
# _matrix_2_x00_3q3q3q = matrices_dict["2_x00"] + _translation_3q3q3q  #220 220
# _matrix_2_0y0_3q3q3q = matrices_dict["2_0y0"] + _translation_3q3q3q  #221 221
# _matrix_2_00z_3q3q3q = matrices_dict["2_00z"] + _translation_3q3q3q  #222 222
# _matrix_2_xx0_3q3q3q = matrices_dict["2_xx0"] + _translation_3q3q3q  #223 223
# _matrix_2_x0x_3q3q3q = matrices_dict["2_x0x"] + _translation_3q3q3q  #224 224
# _matrix_2_0yy_3q3q3q = matrices_dict["2_0yy"] + _translation_3q3q3q  #225 225
# _matrix_3_xxx_3q3q3q = matrices_dict["3_xxx"] + _translation_3q3q3q  #229 229
# _matrix_3_xmxmx_3q3q3q = matrices_dict["3_xmxmx"] + _translation_3q3q3q  #230 230
# _matrix_3_mxxmx_3q3q3q = matrices_dict["3_mxxmx"] + _translation_3q3q3q  #231 231
# _matrix_3_mxmxx_3q3q3q = matrices_dict["3_mxmxx"] + _translation_3q3q3q  #232 232
# _matrix_4_x00_3q3q3q = matrices_dict["4_x00"] + _translation_3q3q3q  #237 237
# _matrix_4_0y0_3q3q3q = matrices_dict["4_0y0"] + _translation_3q3q3q  #238 238
# _matrix_4_00z_3q3q3q = matrices_dict["4_00z"] + _translation_3q3q3q  #239 239
# _matrix_m4_x00_3q3q3q = matrices_dict["-4_x00"] + _translation_3q3q3q  #240 240
# _matrix_m4_0y0_3q3q3q = matrices_dict["-4_0y0"] + _translation_3q3q3q  #241 241
# _matrix_m4_00z_3q3q3q = matrices_dict["-4_00z"] + _translation_3q3q3q  #242 242


# 6_mmm

_matrix_hex_m_x2xz = np.array([[-1, 1, 0, 0],
                               [ 0, 1, 0, 0],
                               [ 0, 0, 1, 0],
                               [ 0, 0, 0, 1]]) #8

_matrix_hex_m_2xxz = np.array([[ 1, 0, 0, 0],
                               [ 1,-1, 0, 0],
                               [ 0, 0, 1, 0],
                               [ 0, 0, 0, 1]]) #9

_matrix_hex_m_x0z = np.array([[ 1,-1, 0, 0],
                              [ 0,-1, 0, 0],
                              [ 0, 0, 1, 0],
                              [ 0, 0, 0, 1]]) #11

_matrix_hex_m_0yz = np.array([[-1, 0, 0, 0],
                              [-1, 1, 0, 0],
                              [ 0, 0, 1, 0],
                              [ 0, 0, 0, 1]]) #12

_matrix_hex_2_x00  = _matrix_hex_m_x2xz @ _matrix_inv_000
_matrix_hex_2_0y0  = _matrix_hex_m_2xxz @ _matrix_inv_000
_matrix_hex_2_x2x0 = _matrix_hex_m_x0z @ _matrix_inv_000
_matrix_hex_2_2xx0 = _matrix_hex_m_0yz @ _matrix_inv_000


_matrix_hex_3_00z = np.array([[0, -1, 0, 0],
                              [ 1,-1, 0, 0],
                              [ 0, 0, 1, 0],
                              [ 0, 0, 0, 1]])



_matrix_hex_m3_00z = _matrix_hex_3_00z @ _matrix_inv_000

_matrix_hex_6_00z  = np.array([[1, -1, 0, 0],
                               [ 1, 0, 0, 0],
                               [ 0, 0, 1, 0],
                               [ 0, 0, 0, 1]])

_matrix_hex_m6_00z = _matrix_hex_6_00z @ _matrix_inv_000

matrices_dict_hex = {
    "hex_m_x2xz": _matrix_hex_m_x2xz,
    "hex_m_2xxz": _matrix_hex_m_2xxz,
    "hex_m_x0z": _matrix_hex_m_x0z,
    "hex_m_0yz": _matrix_hex_m_0yz,
    "hex_2_x00": _matrix_hex_2_x00,
    "hex_2_0y0": _matrix_hex_2_0y0,
    "hex_2_x2x0": _matrix_hex_2_x2x0,
    "hex_2_2xx0": _matrix_hex_2_2xx0,
    "3_00z": _matrix_hex_3_00z,
    "m3_00z": _matrix_hex_m3_00z,
    "6_00z": _matrix_hex_6_00z,
    "m6_00z": _matrix_hex_m6_00z,
}


_translation_00H = np.array([[ 0, 0, 0, 0],
                             [ 0, 0, 0, 0],
                             [ 0, 0, 0, 1/3],
                             [ 0, 0, 0, 0]])

_translation_002H = np.array([[ 0, 0, 0, 0],
                              [ 0, 0, 0, 0],
                              [ 0, 0, 0, 2/3],
                              [ 0, 0, 0, 0]])

_translation_003H = np.array([[ 0, 0, 0, 0],
                              [ 0, 0, 0, 0],
                              [ 0, 0, 0, 3/3],
                              [ 0, 0, 0, 0]])

_translation_004H = np.array([[ 0, 0, 0, 0],
                              [ 0, 0, 0, 0],
                              [ 0, 0, 0, 4/3],
                              [ 0, 0, 0, 0]])

_translation_005H = np.array([[ 0, 0, 0, 0],
                              [ 0, 0, 0, 0],
                              [ 0, 0, 0, 5/3],
                              [ 0, 0, 0, 0]])

#P6_3/mcm

_matrix_hex_6_3_00z_00h = matrices_dict_hex["6_00z"] + _translation_003H  #5


#P6/mcc

_matrix_hex_c_x2xz_00h = matrices_dict_hex["hex_m_x2xz"] + _translation_003H  #8
_matrix_hex_c_2xxz_00h = matrices_dict_hex["hex_m_2xxz"] + _translation_003H  #9
_matrix_hex_c_x0z_00h = matrices_dict_hex["hex_m_x0z"] + _translation_003H  #11
_matrix_hex_c_0yz_00h = matrices_dict_hex["hex_m_0yz"] + _translation_003H  #12
_matrix_hex_2_x0q = matrices_dict_hex["hex_2_x00"] + _translation_003H  #20
_matrix_hex_2_0yq = matrices_dict_hex["hex_2_0y0"] + _translation_003H  #21
_matrix_hex_2_x2xq = matrices_dict_hex["hex_2_x2x0"] + _translation_003H  #23
_matrix_hex_2_2xxq = matrices_dict_hex["hex_2_2xx0"] + _translation_003H  #24

#P6_1_22
_matrix_hex_3_1_00z_00t = matrices_dict_hex["3_00z"] + _translation_002H  #2
_matrix_hex_6_1_00z_00H = matrices_dict_hex["6_00z"] + _translation_00H  #5
_matrix_hex_2_xxH = matrices_dict["2_xx0"] + _translation_002H  #7
_matrix_hex_2_0yt = matrices_dict_hex["hex_2_0y0"] + _translation_004H  #9
_matrix_hex_2_xmx5v = matrices_dict["2_xmx0"] + _translation_005H  #
_matrix_hex_2_2xxv = matrices_dict_hex["hex_2_2xx0"] + _translation_00H  #


_matrix_hex_6_2_00z_00t = matrices_dict_hex["6_00z"] + _translation_002H  #
_matrix_hex_6_4_00z_002t = matrices_dict_hex["6_00z"] + _translation_004H  #
_matrix_hex_6_5_00z_005H = matrices_dict_hex["6_00z"] + _translation_005H  #


#P3_2_21

_matrix_hex_3_2_00z_002t = matrices_dict_hex["3_00z"] + _translation_004H  #
_matrix_hex_2_x0H = matrices_dict_hex["hex_2_x00"] + _translation_002H  #


#P3_2_12

_matrix_hex_2_xmxH = matrices_dict["2_xmx0"] + _translation_002H  #4
_matrix_hex_2_x2xt = matrices_dict_hex["hex_2_x2x0"] + _translation_004H  #5


#3_1_12
_matrix_hex_2_xmxt = matrices_dict["2_xmx0"] + _translation_004H  #
_matrix_hex_2_x2xH = matrices_dict_hex["hex_2_x2x0"] + _translation_002H  #


#3_1_21
_matrix_hex_2_x0t = matrices_dict_hex["hex_2_x00"] + _translation_004H  #
_matrix_hex_2_0yH = matrices_dict_hex["hex_2_0y0"] + _translation_002H  #


_matrix_translation_h00 = _matrix_ID_000 + _translation_h00  #
_matrix_translation_0h0 = _matrix_ID_000 + _translation_0h0  #
_matrix_translation_00h = _matrix_ID_000 + _translation_00h  #
_matrix_translation_0hh = _matrix_ID_000 + _translation_0hh  #
_matrix_translation_h0h = _matrix_ID_000 + _translation_h0h  #
_matrix_translation_hh0 = _matrix_ID_000 + _translation_hh0  #
_matrix_translation_hhh = _matrix_ID_000 + _translation_hhh  #
_matrix_translation_qqq = _matrix_ID_000 + _translation_qqq  #
_matrix_translation_3qqq = _matrix_ID_000 + _translation_h00 + _translation_qqq  #
_matrix_translation_q3qq = _matrix_ID_000 + _translation_0h0 + _translation_qqq  #
_matrix_translation_qq3q = _matrix_ID_000 + _translation_00h + _translation_qqq  #
_matrix_translation_q3q3q = _matrix_ID_000 + _translation_0hh + _translation_qqq  #
_matrix_translation_3qq3q = _matrix_ID_000 + _translation_h0h + _translation_qqq  #
_matrix_translation_3q3qq = _matrix_ID_000 + _translation_hh0 + _translation_qqq  #
_matrix_translation_3q3q3q = _matrix_ID_000 + _translation_hhh + _translation_qqq  #
# _matrix_translation_ = _matrix_ID_000 + _translation_  #
# _matrix_translation_ = _matrix_ID_000 + _translation_  #




# _matrix_ = matrices_dict_hex[] + _translation_  #

all_matrices = [
    _matrix_ID_000,
    _matrix_2_00z,
    _matrix_2_0myy,
    _matrix_2_0qmyy_0mqq,
    _matrix_2_0qyy_0qq,
    _matrix_2_0qz,
    _matrix_2_0y0,
    _matrix_2_0yy,
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
    _matrix_2_mx0x,
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
    _matrix_2_x00,
    _matrix_2_x0q,
    _matrix_2_x0x,
    _matrix_2_x3qmx3o,
    _matrix_2_x3qmxo,
    _matrix_2_xhmxq,
    _matrix_2_xmx0,
    _matrix_2_xmxq,
    _matrix_2_xqmxo,
    _matrix_2_xqq,
    _matrix_2_xqx,
    _matrix_2_xx0,
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
    _matrix_3_mxmxx,
    _matrix_3_mxxmx,
    _matrix_3_xmxmx,
    _matrix_3_xxx,
    _matrix_3_xxx_hhh,
    _matrix_4_00z,
    _matrix_4_0y0,
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
    _matrix_4_x00,
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
    _matrix_inv_000,
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
    _matrix_m3_mxmxx,
    _matrix_m3_mxmxx_3qmqq,
    _matrix_m3_mxxmx,
    _matrix_m3_mxxmx_mqq3q,
    _matrix_m3_x1mxmx_3o5om3o,
    _matrix_m3_xhmxmx_0h0,
    _matrix_m3_xhmxmx_3oom3o,
    _matrix_m3_xhxx_0h0,
    _matrix_m3_xmhxx_3omo3o,
    _matrix_m3_xmxmx,
    _matrix_m3_xmxmx_q3qmq,
    _matrix_m3_xxx,
    _matrix_m3_xxx_3o3o3o,
    _matrix_m3_xxx_qqq,
    _matrix_m4_00z,
    _matrix_m4_00z_00q,
    _matrix_m4_0y0,
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
    _matrix_m4_x00,
    _matrix_m4_x00_q00,
    _matrix_m4_xh0_qh0,
    _matrix_m4_xhmq_3ohmq,
    _matrix_m4_xhq_ohq,
    _matrix_m4_xqmq_0qmq,
    _matrix_m4_xqq_0qq,
    _matrix_m_0yz,
    _matrix_m_x0z,
    _matrix_m_xmxz,
    _matrix_m_xxz,
    _matrix_m_xy0,
    _matrix_m_xymx,
    _matrix_m_xymy,
    _matrix_m_xyx,
    _matrix_m_xyy,
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
    _matrix_hex_2_0y0,
    _matrix_hex_2_0yH,
    _matrix_hex_2_0yq,
    _matrix_hex_2_0yt,
    _matrix_hex_2_2xx0,
    _matrix_hex_2_2xxq,
    _matrix_hex_2_2xxv,
    _matrix_hex_2_x00,
    _matrix_hex_2_x0H,
    _matrix_hex_2_x0q,
    _matrix_hex_2_x0t,
    _matrix_hex_2_x2x0,
    _matrix_hex_2_x2xH,
    _matrix_hex_2_x2xq,
    _matrix_hex_2_x2xt,
    _matrix_hex_2_xmx5v,
    _matrix_hex_2_xmxH,
    _matrix_hex_2_xmxt,
    _matrix_hex_2_xxH,
    _matrix_hex_3_00z,
    _matrix_hex_3_1_00z_00t,
    _matrix_hex_3_2_00z_002t,
    _matrix_hex_6_00z,
    _matrix_hex_6_1_00z_00H,
    _matrix_hex_6_2_00z_00t,
    _matrix_hex_6_3_00z_00h,
    _matrix_hex_6_4_00z_002t,
    _matrix_hex_6_5_00z_005H,
    _matrix_hex_c_0yz_00h,
    _matrix_hex_c_2xxz_00h,
    _matrix_hex_c_x0z_00h,
    _matrix_hex_c_x2xz_00h,
    _matrix_hex_m3_00z,
    _matrix_hex_m6_00z,
    _matrix_hex_m_0yz,
    _matrix_hex_m_2xxz,
    _matrix_hex_m_x0z,
    _matrix_hex_m_x2xz,
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


# powtorki sprawdzic


# _matrix_ = matrices_dict[] + _translation_

# labels = np.array(("inv_000",

#                       1        2        3
#                    "m_0yz", "m_x0z", "m_xy0",

#                       4        5        6
#                    "m_xmxz", "m_xymy", "m_xymx",

#                       7         8         9
#                    "m_xyx", "m_xxz", "m_xyy",

#                       10       11       12
#                    "2_x00", "2_0y0", "2_00z",

#                       13       14        15
#                    "2_xx0", "2_x0x",  "2_0yy",

#                       16       17        18
#                    "2_xmx0","2_mx0x", "2_0myy",


#                       19        20
#                    "3_xxx", "3_xmxmx",

#                       21        22
#                    "3_mxxmx", "3_mxmxx",

#                        23        24
#                    "m3_xxx", "m3_xmxmx",

#                        25         26
#                    "m3_mxxmx", "m3_mxmxx",

#                       27       28       29
#                    "4_x00", "4_0y0", "4_00z",

#                        30       31       32
#                    "-4_x00","-4_0y0","-4_00z"))


# operations = np.array([1,
#
#                        1, 1, 1,
#                        1, 1, 1,
#                        1, 1, 1,
#
#                        1, 1, 1,
#                        1, 1, 1,
#                        1, 1, 1,
#
#                        2, 2,
#                        2, 2,
#
#                        2, 2,
#                        2, 2,
#
#                        3, 3, 3,
#
#                        3, 3, 3])

def pick_matrices_by_index(masked_indexes, matrices=matrices):
    return np.ma.masked_where(masked_indexes, matrices).compressed().reshape((-1, 3, 3))

# def pick_matrices_by_label(masked_labels, labels=labels, matrices=matrices):
#     mask_id = np.ma.masked_where(masked_labels, all_labels)
#     return pick_matrices_by_index(mask_id)

def is_ortogonal(matrix):
    iloczyn = matrix.T @ matrix
    identity = np.eye(len(matrix), dtype=int)
    return np.array_equal(iloczyn, identity)


def make_matrix_multiplication_table():
    import pandas as pd

    def translate_matrix_to_name(matrices):
        mapper = {m.tostring(): labels[i]  for i, m in enumerate(matrices)}
        I = np.eye(3, dtype=int)
        mapper[I.tostring()] = "I_000"

        multi_table = np.empty((len(matrices), len(matrices)), dtype=object)
        x, y = multi_table.shape
        for ix in range(x):
            for iy in range(y):
                result = matrices[ix] @ matrices[iy]
                multi_table[ix, iy] = mapper[result.tostring()]
        return multi_table

    result = translate_matrix_to_name(matrices)
    data = pd.Dataframe(result)
    print(data)


# class Matrices:
#     def __init__(self, matrices, matrices_inverse, labels, indices):
#         self.matrices = matrices
#         self.matrices_inverse = matrices_inverse
#         self.labels = labels
#         self.indices = indices
#
#     def get_labels(self, mask=None):
#         if mask is None:
#             return self.labels
#         return self.labels[mask]

