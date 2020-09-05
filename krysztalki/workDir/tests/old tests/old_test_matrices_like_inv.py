import matrices_new_extended as mne
import numpy as np

points = np.array([
    [1,-2,3,1],
    [1,0,-1,1],
    [1,1,1,1],
    [0,0,0,1]
])


def test_matrix_inv_000():
    points_tr = (mne._matrix_inv_000 @ points.T).T
    assert np.array_equal(points_tr[0], np.array([-1, 2,-3, 1]))
    assert np.array_equal(points_tr[1], np.array([-1, 0, 1, 1]))
    assert np.array_equal(points_tr[2], np.array([-1,-1,-1, 1]))
    assert np.array_equal(points_tr[3], np.array([ 0, 0, 0, 1]))

def test_matrix_inv_qq0():
    points_tr = (mne._matrix_inv_qq0 @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 0, 3,-3, 1]))
    assert np.array_equal(points_tr[1], np.array([ 0, 1, 1, 1]))
    assert np.array_equal(points_tr[2], np.array([ 0, 0,-1, 1]))
    assert np.array_equal(points_tr[3], np.array([ 1, 1, 0, 1]))


def test_matrix_inv_0qq():
    points_tr = (mne._matrix_inv_0qq @ points.T).T
    assert np.array_equal(points_tr[0], np.array([-1, 3,-2, 1]))
    assert np.array_equal(points_tr[1], np.array([-1, 1, 2, 1]))
    assert np.array_equal(points_tr[2], np.array([-1, 0, 0, 1]))
    assert np.array_equal(points_tr[3], np.array([ 0, 1, 1, 1]))


def test_matrix_inv_q0q():
    points_tr = (mne._matrix_inv_q0q @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 0, 2,-2, 1]))
    assert np.array_equal(points_tr[1], np.array([ 0, 0, 2, 1]))
    assert np.array_equal(points_tr[2], np.array([ 0,-1, 0, 1]))
    assert np.array_equal(points_tr[3], np.array([ 1, 0, 1, 1]))


def test_matrix_inv_qqq():
    points_tr = (mne._matrix_inv_qqq @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 0, 3,-2, 1]))
    assert np.array_equal(points_tr[1], np.array([ 0, 1, 2, 1]))
    assert np.array_equal(points_tr[2], np.array([ 0, 0, 0, 1]))
    assert np.array_equal(points_tr[3], np.array([ 1, 1, 1, 1]))


def test_matrix_inv_ooo():
    points_tr = (mne._matrix_inv_ooo @ points.T).T
    assert np.array_equal(points_tr[0], np.array([-0.5, 2.5,-2.5, 1]))
    assert np.array_equal(points_tr[1], np.array([-0.5, 0.5, 1.5, 1]))
    assert np.array_equal(points_tr[2], np.array([-0.5,-0.5,-0.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 0.5, 0.5, 0.5, 1]))


def test_matrix_inv_o3o3o():
    points_tr = (mne._matrix_inv_o3o3o @ points.T).T
    assert np.array_equal(points_tr[0], np.array([-0.5, 3.5,-1.5, 1]))
    assert np.array_equal(points_tr[1], np.array([-0.5, 1.5, 2.5, 1]))
    assert np.array_equal(points_tr[2], np.array([-0.5, 0.5, 0.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 0.5, 1.5, 1.5, 1]))


def test_matrix_inv_3oo3o():
    points_tr = (mne._matrix_inv_3oo3o @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 0.5, 2.5,-1.5, 1]))
    assert np.array_equal(points_tr[1], np.array([ 0.5, 0.5, 2.5, 1]))
    assert np.array_equal(points_tr[2], np.array([ 0.5,-0.5, 0.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 1.5, 0.5, 1.5, 1]))


def test_matrix_inv_3o3oo():
    points_tr = (mne._matrix_inv_3o3oo @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 0.5, 3.5,-2.5, 1]))
    assert np.array_equal(points_tr[1], np.array([ 0.5, 1.5, 1.5, 1]))
    assert np.array_equal(points_tr[2], np.array([ 0.5, 0.5,-0.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 1.5, 1.5, 0.5, 1]))


def test_matrix_inv_oo3o():
    points_tr = (mne._matrix_inv_oo3o @ points.T).T
    assert np.array_equal(points_tr[0], np.array([-0.5, 2.5,-1.5, 1]))
    assert np.array_equal(points_tr[1], np.array([-0.5, 0.5, 2.5, 1]))
    assert np.array_equal(points_tr[2], np.array([-0.5,-0.5, 0.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 0.5, 0.5, 1.5, 1]))


def test_matrix_inv_o3oo():
    points_tr = (mne._matrix_inv_o3oo @ points.T).T
    assert np.array_equal(points_tr[0], np.array([-0.5, 3.5,-2.5, 1]))
    assert np.array_equal(points_tr[1], np.array([-0.5, 1.5, 1.5, 1]))
    assert np.array_equal(points_tr[2], np.array([-0.5, 0.5,-0.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 0.5, 1.5, 0.5, 1]))


def test_matrix_inv_3ooo():
    points_tr = (mne._matrix_inv_3ooo @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 0.5, 2.5,-2.5, 1]))
    assert np.array_equal(points_tr[1], np.array([ 0.5, 0.5, 1.5, 1]))
    assert np.array_equal(points_tr[2], np.array([ 0.5,-0.5,-0.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 1.5, 0.5, 0.5, 1]))


def test_matrix_inv_3o3o3o():
    points_tr = (mne._matrix_inv_3o3o3o @ points.T).T
    assert np.array_equal(points_tr[0], np.array([ 0.5, 3.5,-1.5, 1]))
    assert np.array_equal(points_tr[1], np.array([ 0.5, 1.5, 2.5, 1]))
    assert np.array_equal(points_tr[2], np.array([ 0.5, 0.5, 0.5, 1]))
    assert np.array_equal(points_tr[3], np.array([ 1.5, 1.5, 1.5, 1]))

