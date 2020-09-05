from matrices_new_extended import all_matrices, _matrix_ID_000
from itertools import combinations
import numpy as np
# from names_of_matrices import names
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
    "hex_2_0y0",
    "hex_2_0yH",
    "hex_2_0yq",
    "hex_2_0yt",
    "hex_2_2xx0",
    "hex_2_2xxq",
    "hex_2_2xxv",
    "hex_2_x00",
    "hex_2_x0H",
    "hex_2_x0q",
    "hex_2_x0t",
    "hex_2_x2x0",
    "hex_2_x2xH",
    "hex_2_x2xq",
    "hex_2_x2xt",
    "hex_2_xmx5v",
    "hex_2_xmxH",
    "hex_2_xmxt",
    "hex_2_xxH",
    "hex_3_00z",
    "hex_3_1_00z_00t",
    "hex_3_2_00z_002t",
    "hex_6_00z",
    "hex_6_1_00z_00H",
    "hex_6_2_00z_00t",
    "hex_6_3_00z_00h",
    "hex_6_4_00z_002t",
    "hex_6_5_00z_005H",
    "hex_c_0yz_00h",
    "hex_c_2xxz_00h",
    "hex_c_x0z_00h",
    "hex_c_x2xz_00h",
    "hex_m3_00z",
    "hex_m6_00z",
    "hex_m_0yz",
    "hex_m_2xxz",
    "hex_m_x0z",
    "hex_m_x2xz",
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


class Matrix:
    def __init__(self, mat1, mat2):
        rot_cell, trans = Matrix._calculate_matrix(mat1, mat2)
        result = Matrix._compose_matrix(rot_cell, trans)
        self.result = result

    def __hash__(self):
        return self.result.tostring()

    @staticmethod
    def _calculate_matrix(mat1, mat2):
        rot1 = mat1[:-1, :-1]
        rot2 = mat2[:-1, :-1]
        new_rot_cell = rot1 @ rot2

        trans = mat1[:-1, -1] + mat2[:-1, -1]
        mask_above_cell = trans > 2
        trans[mask_above_cell] -= 2

        return new_rot_cell, trans

    @staticmethod
    def _compose_matrix(rot_cell, trans):
        result = np.empty((4, 4), dtype=float)
        result[:-1, :-1] = rot_cell
        result[:-1, -1] = trans
        result[-1, :-2] = 0
        result[-1, -1] = 1
        return result

    def __eq__(self, other):
        return np.array_equal(self.result, other.result)


# def clean_matrix(matrix):
#     mask_outside_cell_transform = matrix > 2
#     matrix[mask_outside_cell_transform] -= 2
#     mask_zero = matrix == 0
#     matrix[mask_zero] += 1
#     matrix[mask_zero] -= 1
#

def M(M1, M2):
    M = M1 @ M2
    mask = M[:-1, -1] < 0
    M[:-1, -1][mask] += 2
    mask = M[:-1, -1] >= 2
    M[:-1, -1][mask] -= 2
    mask = M == 0
    M[mask] -= 1
    M[mask] += 1
    return M

def transpose(mat):
    new_mat = mat.copy()
    rot = new_mat[:-1, :-1]
    rot = rot.T
    new_mat[:-1, :-1] = rot
    return new_mat

from time import time


all_hashed_M = {M.tostring(): name for M, name in zip(all_matrices, names)}
lol = []

for M1, M2 in combinations(range(1, len(all_matrices)), 2):
    start = time()
    group_str = {all_hashed_M[_matrix_ID_000.tostring()],
                 all_hashed_M[all_matrices[M1].tostring()],
                 all_hashed_M[all_matrices[M2].tostring()]}
    group_str_noname = set()
    group_lst = [_matrix_ID_000,
                 all_matrices[M1],
                 all_matrices[M2]]
    calculated = set()
    i = 1
    while i < len(group_str):
        j = 1
        while j < len(group_str):
            if (i, j) in calculated or i == j:
                j += 1
                continue

            temp_M = M(group_lst[i], group_lst[j])
            temp_M2 = transpose(temp_M)
            calculated.add((i, j))
            str_temp = temp_M.tostring()
            str_temp2 = temp_M2.tostring()
            val = all_hashed_M.get(str_temp)
            val2 = all_hashed_M.get(str_temp2)
            matrix_not_in_group = val not in group_str
            matrix_rev_not_in_group = val2 not in group_str
            if matrix_not_in_group or matrix_rev_not_in_group:
                group_lst.append(temp_M)
                # if val is None and not np.array_equal(temp_M, temp_M2):

                if val is not None:
                    group_str.add(val)
                elif val2 is not None:
                    group_str.add(val2)
                else:
                    int_temp = temp_M.astype(int)
                    int_temp2 = temp_M2.astype(int)
                    str_temp = int_temp.tostring()
                    str_temp2 = int_temp2.tostring()
                    val = all_hashed_M.get(str_temp)
                    val2 = all_hashed_M.get(str_temp2)
                    matrix_not_in_group = val not in group_str
                    matrix_rev_not_in_group = val2 not in group_str
                    if matrix_not_in_group or matrix_rev_not_in_group:
                        if val is not None:
                            group_str.add(val)
                        elif val2 is not None:
                            group_str.add(val2)
                        else:
                            group_str.add(str((i, j)))
                            group_str_noname.add((i, j))

                if i > 1:
                    i = 1
                    j = 2
                    continue
            j += 1

        if len(group_str) > 195:
            break
        i += 1
        # print(i, j)

    str_temp = all_matrices[M1].tostring()
    str_temp2 = all_matrices[M2].tostring()
    val = all_hashed_M.get(str_temp)
    val2 = all_hashed_M.get(str_temp2)
    with open(f"output_of_group_combinator/{val}, {val2}.txt", "w") as f:
        elapsed = time() - start
        string = "; ".join((str((M1, M2)), str((val, val2)), str(group_str), f"time elapsed = {elapsed}"))
        f.write(string)
        print(f"{val}, {val2} : time {elapsed}")


print()
pass
print(( group_lst, group_str))
#
#
# M6 = np.array([[ 1, 0, 0, 1],
#                [ 0,-1, 0, 1],
#                [ 0, 0,-1, 0],
#                [ 0, 0, 0, 1]])
#
# M8 = np.array([[-1, 0, 0, 1],
#                [ 0,-1, 0, 1],
#                [ 0, 0, 1, 1],
#                [ 0, 0, 0, 1]])
#
#
# group_str = {all_hashed_M[_matrix_ID_000.tostring()],
#              all_hashed_M[M6.tostring()],
#              all_hashed_M[M8.tostring()]}
#
# group_lst = [_matrix_ID_000,
#              M6,
#              M8]
# calculated = set()
# i = 1
# while i < len(group_str):
#     j = i + 1
#     while j < len(group_str):
#         if (i, j) in calculated:
#             j += 1
#             continue
#
#         temp_M = M(group_lst[i], group_lst[j])
#         calculated.add((i, j))
#         str_temp = temp_M.tostring()
#
#         if str_temp not in group_str:
#             group_lst.append(temp_M)
#             val = all_hashed_M.get(str_temp, None)
#             if val is not None:
#                 group_str.add(val)
#             else:
#                 group_str.add(str((i, j)))
#
#             if i > 1:
#                 i = 1
#                 j = 2
#                 continue
#         j += 1
#
#     if len(group_str) > 195:
#         break
#     i += 1
# pass
# print(( group_lst, group_str))