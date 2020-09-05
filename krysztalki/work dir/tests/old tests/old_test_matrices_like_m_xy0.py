import matrices_new_extended as mne
import numpy as np

points = np.array([
    [1,-2,3,1],
    [1,0,-1,1],
    [1,1,1,1],
    [0,0,0,1]
])


def test_matrix_m_xy0():
    points_tr = (mne._matrix_m_xy0 @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 1,-2,-3, 1]))
    assert np.array_equal(points_tr[1], np.array([ 1, 0, 1, 1]))
    assert np.array_equal(points_tr[2], np.array([ 1, 1,-1, 1]))
    assert np.array_equal(points_tr[3], np.array([ 0, 0, 0, 1]))


def test_matrix_b_xyq_0h0():
    points_tr = (mne._matrix_b_xyq_0h0 @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 1,-1,-2, 1]))
    assert np.array_equal(points_tr[1], np.array([ 1, 1, 2, 1]))
    assert np.array_equal(points_tr[2], np.array([ 1, 2, 0, 1]))
    assert np.array_equal(points_tr[3], np.array([ 0, 1, 1, 1]))


def test_matrix_a_xyq_h00():
    points_tr = (mne._matrix_a_xyq_h00 @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 2,-2,-2, 1]))
    assert np.array_equal(points_tr[1], np.array([ 2, 0, 2, 1]))
    assert np.array_equal(points_tr[2], np.array([ 2, 1, 0, 1]))
    assert np.array_equal(points_tr[3], np.array([ 1, 0, 1, 1]))


def test_matrix_n_xy0_hh0():
    points_tr = (mne._matrix_n_xy0_hh0 @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 2,-1,-3, 1]))
    assert np.array_equal(points_tr[1], np.array([ 2, 1, 1, 1]))
    assert np.array_equal(points_tr[2], np.array([ 2, 2,-1, 1]))
    assert np.array_equal(points_tr[3], np.array([ 1, 1, 0, 1]))


def test_matrix_n_xyq_hh0():
    points_tr = (mne._matrix_n_xyq_hh0 @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 2,-1,-2, 1]))
    assert np.array_equal(points_tr[1], np.array([ 2, 1, 2, 1]))
    assert np.array_equal(points_tr[2], np.array([ 2, 2, 0, 1]))
    assert np.array_equal(points_tr[3], np.array([ 1, 1, 1, 1]))


def test_matrix_d_xyo_qq0():
    points_tr = (mne._matrix_d_xyo_qq0 @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 1.5,-1.5,-2.5, 1]))
    assert np.array_equal(points_tr[1], np.array([ 1.5, 0.5, 1.5, 1]))
    assert np.array_equal(points_tr[2], np.array([ 1.5, 1.5,-0.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 0.5, 0.5, 0.5, 1]))


def test_matrix_d_xy3o_q3q0():
    points_tr = (mne._matrix_d_xy3o_q3q0 @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 1.5,-0.5,-1.5, 1]))
    assert np.array_equal(points_tr[1], np.array([ 1.5, 1.5, 2.5, 1]))
    assert np.array_equal(points_tr[2], np.array([ 1.5, 2.5, 0.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 0.5, 1.5, 1.5, 1]))


def test_matrix_dxy3o_3qq0():
    points_tr = (mne._matrix_dxy3o_3qq0 @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 2.5,-1.5,-1.5, 1]))
    assert np.array_equal(points_tr[1], np.array([ 2.5, 0.5, 2.5, 1]))
    assert np.array_equal(points_tr[2], np.array([ 2.5, 1.5, 0.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 1.5, 0.5, 1.5, 1]))


def test_matrix_d_xyo_3q3q0():
    points_tr = (mne._matrix_d_xyo_3q3q0 @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 2.5,-0.5,-2.5, 1]))
    assert np.array_equal(points_tr[1], np.array([ 2.5, 1.5, 1.5, 1]))
    assert np.array_equal(points_tr[2], np.array([ 2.5, 2.5,-0.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 1.5, 1.5, 0.5, 1]))


def test_matrix_b_xy0_0h0():
    points_tr = (mne._matrix_b_xy0_0h0 @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 1,-1,-3, 1]))
    assert np.array_equal(points_tr[1], np.array([ 1, 1, 1, 1]))
    assert np.array_equal(points_tr[2], np.array([ 1, 2,-1, 1]))
    assert np.array_equal(points_tr[3], np.array([ 0, 1, 0, 1]))


def test_matrix_d_xy3o_qq0():
    points_tr = (mne._matrix_d_xy3o_qq0 @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 1.5,-1.5,-1.5, 1]))
    assert np.array_equal(points_tr[1], np.array([ 1.5, 0.5, 2.5, 1]))
    assert np.array_equal(points_tr[2], np.array([ 1.5, 1.5, 0.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 0.5, 0.5, 1.5, 1]))


def test_matrix_d_xyo_q3q0():
    points_tr = (mne._matrix_d_xyo_q3q0 @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 1.5,-0.5,-2.5, 1]))
    assert np.array_equal(points_tr[1], np.array([ 1.5, 1.5, 1.5, 1]))
    assert np.array_equal(points_tr[2], np.array([ 1.5, 2.5,-0.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 0.5, 1.5, 0.5, 1]))


def test_matrix_d_xyo_3qq0():
    points_tr = (mne._matrix_d_xyo_3qq0 @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 2.5,-1.5,-2.5, 1]))
    assert np.array_equal(points_tr[1], np.array([ 2.5, 0.5, 1.5, 1]))
    assert np.array_equal(points_tr[2], np.array([ 2.5, 1.5,-0.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 1.5, 0.5, 0.5, 1]))


def test_matrix_d_xy3o_3q3q0():
    points_tr = (mne._matrix_d_xy3o_3q3q0 @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 2.5,-0.5,-1.5, 1]))
    assert np.array_equal(points_tr[1], np.array([ 2.5, 1.5, 2.5, 1]))
    assert np.array_equal(points_tr[2], np.array([ 2.5, 2.5, 0.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 1.5, 1.5, 1.5, 1]))


# def test_matrix_m_xy0():
#     points_tr = (mne._matrix_m_xy0 @ points.T).T
#     assert np.array_equal(points_tr[0], np.array([ 1,-2,-3, 1]))
#     assert np.array_equal(points_tr[1], np.array([ 1, 0, 1, 1]))
#     assert np.array_equal(points_tr[2], np.array([ 1, 1,-1, 1]))
#     assert np.array_equal(points_tr[3], np.array([ 0, 0, 0, 1]))
