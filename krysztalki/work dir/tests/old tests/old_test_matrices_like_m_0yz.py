import matrices_new_extended as mne
import numpy as np

points = np.array([
    [1,-2,3,1],
    [1,0,-1,1],
    [1,1,1,1],
    [0,0,0,1]
])


def test_matrix_m_0yz():
    points_tr = (mne._matrix_m_0yz @ points.T).T
    assert np.array_equal(points_tr[0], np.array([-1,-2, 3, 1]))
    assert np.array_equal(points_tr[1], np.array([-1, 0,-1, 1]))
    assert np.array_equal(points_tr[2], np.array([-1, 1, 1, 1]))
    assert np.array_equal(points_tr[3], np.array([ 0, 0, 0, 1]))


def test_matrix_b_qyz():
    points_tr = (mne._matrix_b_qyz_0h0 @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 0,-1, 3, 1]))
    assert np.array_equal(points_tr[1], np.array([ 0, 1,-1, 1]))
    assert np.array_equal(points_tr[2], np.array([ 0, 2, 1, 1]))
    assert np.array_equal(points_tr[3], np.array([ 1, 1, 0, 1]))


def test_matrix_d_oyz_0qq():
    points_tr = (mne._matrix_d_oyz_0qq @ points.T).T
    assert np.array_equal(points_tr[0], np.array([-0.5,-1.5, 3.5, 1]))
    assert np.array_equal(points_tr[1], np.array([-0.5, 0.5,-0.5, 1]))
    assert np.array_equal(points_tr[2], np.array([-0.5, 1.5, 1.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 0.5, 0.5, 0.5, 1]))


def test_matrix_d_oyz_03q3q():
    points_tr = (mne._matrix_d_oyz_03q3q @ points.T).T
    assert np.array_equal(points_tr[0], np.array([-0.5,-0.5, 4.5, 1]))
    assert np.array_equal(points_tr[1], np.array([-0.5, 1.5, 0.5, 1]))
    assert np.array_equal(points_tr[2], np.array([-0.5, 2.5, 2.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 0.5, 1.5, 1.5, 1]))


def test_matrix_d_3oyz_0q3q():
    points_tr = (mne._matrix_d_3oyz_0q3q @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 0.5,-1.5, 4.5, 1]))
    assert np.array_equal(points_tr[1], np.array([ 0.5, 0.5, 0.5, 1]))
    assert np.array_equal(points_tr[2], np.array([ 0.5, 1.5, 2.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 1.5, 0.5, 1.5, 1]))


def test_matrix_d_3oyz_03qq():
    points_tr = (mne._matrix_d_3oyz_03qq @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 0.5,-0.5, 3.5, 1]))
    assert np.array_equal(points_tr[1], np.array([ 0.5, 1.5,-0.5, 1]))
    assert np.array_equal(points_tr[2], np.array([ 0.5, 2.5, 1.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 1.5, 1.5, 0.5, 1]))


def test_matrix_c_0yz_00h():
    points_tr = (mne._matrix_c_0yz_00h @ points.T).T
    assert np.array_equal(points_tr[0], np.array([-1,-2, 4, 1]))
    assert np.array_equal(points_tr[1], np.array([-1, 0, 0, 1]))
    assert np.array_equal(points_tr[2], np.array([-1, 1, 2, 1]))
    assert np.array_equal(points_tr[3], np.array([ 0, 0, 1, 1]))


def test_matrix_d_oyz_0q3q():
    points_tr = (mne._matrix_d_oyz_0q3q @ points.T).T
    assert np.array_equal(points_tr[0], np.array([-0.5,-1.5, 4.5, 1]))
    assert np.array_equal(points_tr[1], np.array([-0.5, 0.5, 0.5, 1]))
    assert np.array_equal(points_tr[2], np.array([-0.5, 1.5, 2.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 0.5, 0.5, 1.5, 1]))


def test_matrix_d_oyz_03qq():
    points_tr = (mne._matrix_d_oyz_03qq @ points.T).T
    assert np.array_equal(points_tr[0], np.array([-0.5,-0.5, 3.5, 1]))
    assert np.array_equal(points_tr[1], np.array([-0.5, 1.5,-0.5, 1]))
    assert np.array_equal(points_tr[2], np.array([-0.5, 2.5, 1.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 0.5, 1.5, 0.5, 1]))


def test_matrix_d_3oyz_0qq():
    points_tr = (mne._matrix_d_3oyz_0qq @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 0.5,-1.5, 3.5, 1]))
    assert np.array_equal(points_tr[1], np.array([ 0.5, 0.5,-0.5, 1]))
    assert np.array_equal(points_tr[2], np.array([ 0.5, 1.5, 1.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 1.5, 0.5, 0.5, 1]))


def test_matrix_d_3oyz_03q3q():
    points_tr = (mne._matrix_d_3oyz_03q3q @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 0.5,-0.5, 4.5, 1]))
    assert np.array_equal(points_tr[1], np.array([ 0.5, 1.5, 0.5, 1]))
    assert np.array_equal(points_tr[2], np.array([ 0.5, 2.5, 2.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 1.5, 1.5, 1.5, 1]))

#
# def test_matrix_m_0yz():
#     points_tr = (mne._matrix_m_0yz @ points.T).T
#     assert np.array_equal(points_tr[0], np.array([-1,-2, 3, 1]))
#     assert np.array_equal(points_tr[1], np.array([-1, 0,-1, 1]))
#     assert np.array_equal(points_tr[2], np.array([-1, 1, 1, 1]))
#     assert np.array_equal(points_tr[3], np.array([ 0, 0, 0, 1]))

