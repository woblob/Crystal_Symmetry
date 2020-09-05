import matrices_new_extended as mne
import numpy as np

points = np.array([
    [1,-2,3,1],
    [1,0,-1,1],
    [1,1,1,1],
    [0,0,0,1]
])


def test_matrix_m_x0z():
    points_tr = (mne._matrix_m_x0z @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 1, 2, 3, 1]))
    assert np.array_equal(points_tr[1], np.array([ 1, 0,-1, 1]))
    assert np.array_equal(points_tr[2], np.array([ 1,-1, 1, 1]))
    assert np.array_equal(points_tr[3], np.array([ 0, 0, 0, 1]))


def test_matrix_c_xqz_00h():
    points_tr = (mne._matrix_c_xqz_00h @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 1, 3, 4, 1]))
    assert np.array_equal(points_tr[1], np.array([ 1, 1, 0, 1]))
    assert np.array_equal(points_tr[2], np.array([ 1, 0, 2, 1]))
    assert np.array_equal(points_tr[3], np.array([ 0, 1, 1, 1]))


def test_matrix_a_xqz_h00():
    points_tr = (mne._matrix_a_xqz_h00 @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 2, 3, 3, 1]))
    assert np.array_equal(points_tr[1], np.array([ 2, 1,-1, 1]))
    assert np.array_equal(points_tr[2], np.array([ 2, 0, 1, 1]))
    assert np.array_equal(points_tr[3], np.array([ 1, 1, 0, 1]))


def test_matrix_n_xqz_h0h():
    points_tr = (mne._matrix_n_xqz_h0h @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 2, 3, 4, 1]))
    assert np.array_equal(points_tr[1], np.array([ 2, 1, 0, 1]))
    assert np.array_equal(points_tr[2], np.array([ 2, 0, 2, 1]))
    assert np.array_equal(points_tr[3], np.array([ 1, 1, 1, 1]))


def test_matrix_d_xoz_q0q():
    points_tr = (mne._matrix_d_xoz_q0q @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 1.5, 2.5, 3.5, 1]))
    assert np.array_equal(points_tr[1], np.array([ 1.5, 0.5,-0.5, 1]))
    assert np.array_equal(points_tr[2], np.array([ 1.5,-0.5, 1.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 0.5, 0.5, 0.5, 1]))


def test_matrix_d_x3oz_q03q():
    points_tr = (mne._matrix_d_x3oz_q03q @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 1.5, 3.5, 4.5, 1]))
    assert np.array_equal(points_tr[1], np.array([ 1.5, 1.5, 0.5, 1]))
    assert np.array_equal(points_tr[2], np.array([ 1.5, 0.5, 2.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 0.5, 1.5, 1.5, 1]))


def test_matrix_d_xoz_3q03q():
    points_tr = (mne._matrix_d_xoz_3q03q @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 2.5, 2.5, 4.5, 1]))
    assert np.array_equal(points_tr[1], np.array([ 2.5, 0.5, 0.5, 1]))
    assert np.array_equal(points_tr[2], np.array([ 2.5,-0.5, 2.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 1.5, 0.5, 1.5, 1]))


def test_matrix_d_x3oz_3q0q():
    points_tr = (mne._matrix_d_x3oz_3q0q @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 2.5, 3.5, 3.5, 1]))
    assert np.array_equal(points_tr[1], np.array([ 2.5, 1.5,-0.5, 1]))
    assert np.array_equal(points_tr[2], np.array([ 2.5, 0.5, 1.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 1.5, 1.5, 0.5, 1]))


def test_matrix_a_x0z_h00():
    points_tr = (mne._matrix_a_x0z_h00 @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 2, 2, 3, 1]))
    assert np.array_equal(points_tr[1], np.array([ 2, 0,-1, 1]))
    assert np.array_equal(points_tr[2], np.array([ 2,-1, 1, 1]))
    assert np.array_equal(points_tr[3], np.array([ 1, 0, 0, 1]))


def test_matrix_d_xoz_q03q():
    points_tr = (mne._matrix_d_xoz_q03q @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 1.5, 2.5, 4.5, 1]))
    assert np.array_equal(points_tr[1], np.array([ 1.5, 0.5, 0.5, 1]))
    assert np.array_equal(points_tr[2], np.array([ 1.5,-0.5, 2.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 0.5, 0.5, 1.5, 1]))


def test_matrix_d_x3oz_q0q():
    points_tr = (mne._matrix_d_x3oz_q0q @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 1.5, 3.5, 3.5, 1]))
    assert np.array_equal(points_tr[1], np.array([ 1.5, 1.5,-0.5, 1]))
    assert np.array_equal(points_tr[2], np.array([ 1.5, 0.5, 1.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 0.5, 1.5, 0.5, 1]))


def test_matrix_d_xoz_3q0q():
    points_tr = (mne._matrix_d_xoz_3q0q @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 2.5, 2.5, 3.5, 1]))
    assert np.array_equal(points_tr[1], np.array([ 2.5, 0.5,-0.5, 1]))
    assert np.array_equal(points_tr[2], np.array([ 2.5,-0.5, 1.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 1.5, 0.5, 0.5, 1]))


def test_matrix_d_x3oz_3q03q():
    points_tr = (mne._matrix_d_x3oz_3q03q @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 2.5, 3.5, 4.5, 1]))
    assert np.array_equal(points_tr[1], np.array([ 2.5, 1.5, 0.5, 1]))
    assert np.array_equal(points_tr[2], np.array([ 2.5, 0.5, 2.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 1.5, 1.5, 1.5, 1]))

#
# def test_matrix_m_x0z():
#     points_tr = (mne._matrix_m_x0z @ points.T).T
#     assert np.array_equal(points_tr[0], np.array([ 1, 2, 3, 1]))
#     assert np.array_equal(points_tr[1], np.array([ 1, 0,-1, 1]))
#     assert np.array_equal(points_tr[2], np.array([ 1,-1, 1, 1]))
#     assert np.array_equal(points_tr[3], np.array([ 0, 0, 0, 1]))
#
