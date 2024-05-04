import numpy as np

from Crystal_Symmetry.krysztalki.workDir.Matrix.eigen.eigenvectors import resize_vectors


class TestResizeVectors:
    def test_same_shape(self):
        vectors = np.array([[1, 2, 3], [4, 5, 6]])
        result = resize_vectors(vectors)

        print("hello")
        assert result.shape == vectors.shape

    def test_empty_array(self):
        vectors = np.array([])
        result = resize_vectors(vectors)

        assert result.size == 0

    def test_scale_between_minus_one_and_one(self):
        vectors = np.array([[1, 2, 3], [4, 5, 6]])
        result = resize_vectors(vectors)

        assert np.all(result >= -1) and np.all(result <= 1)

    def test_vectors_with_small_values(self):
        vectors = np.array([[0.001, 0.002, 0.003], [0.004, 0.005, 0.006]])
        resized_vectors = resize_vectors(vectors)

        assert np.all(resized_vectors >= -1)
        assert np.all(resized_vectors <= 1)

    def test_handle_vectors_with_all_values_zero(self):
        vectors = np.zeros((2, 3))
        result = resize_vectors(vectors)

        assert np.all(result == 0)

    def test_handles_negative_values(self):
        vectors = np.array([[-1, 2, -3], [4, -5, 6], [-7, 8, -9]])
        resized_vectors = resize_vectors(vectors)

        expected_result = np.array(
            [[-1 / 7, 2 / 8, -3 / 9], [4 / 7, -5 / 8, 6 / 9], [-7 / 7, 8 / 8, -9 / 9]]
        )
        np.testing.assert_array_equal(resized_vectors, expected_result)

    # def test_handles_vectors_close_to_zero(self):
    #     vectors = np.array([[1e-10, 2e-10, 3e-10], [4e-10, 5e-10, 6e-10]])
    #     mocker.patch("numpy.max", return_value=np.array([4e-10, 5e-10, 6e-10]))
    #     result = resize_vectors(vectors)
    #     assert False
    #     assert np.array_equal(
    #         result,
    #         np.array(
    #             [
    #                 [1e-10 / 4e-10, 2e-10 / 5e-10, 3e-10 / 6e-10],
    #                 [4e-10 / 4e-10, 5e-10 / 5e-10, 6e-10 / 6e-10],
    #             ]
    #         ),
    #     )

    def test_handles_vectors_with_different_scales(self):
        vectors = np.array([[1, 2, 3], [10, 20, 30], [100, 200, 300]])
        resized_vectors = resize_vectors(vectors)

        expected_result = np.array([[0.01, 0.01, 0.01], [0.1, 0.1, 0.1], [1, 1, 1]])
        np.testing.assert_array_almost_equal(resized_vectors, expected_result)
