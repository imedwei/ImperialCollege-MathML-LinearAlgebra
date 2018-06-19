import unittest
import numpy as np
import identifying_special_matrices as impl


class IdentifyingSpecialMatricesTest(unittest.TestCase):

    def test_isSingular(self):
        A = np.array([
            [2, 0, 0, 0],
            [0, 3, 0, 0],
            [0, 0, 4, 4],
            [0, 0, 5, 5]
        ], dtype=np.float_)
        self.assertTrue(impl.isSingular(A))

    def test_fixRowZero(self):
        A = np.array([
            [0, 7, -5, 3],
            [2, 8, 0, 4],
            [3, 12, 0, 5],
            [1, 3, 1, 3]
        ], dtype=np.float_)
        impl.fixRowZero(A)
        self.assertEqual(A[0][0], 1)

    def test_fixRowOne(self):
        A = np.array([
            [0, 7, -5, 3],
            [2, 8, 0, 4],
            [3, 12, 0, 5],
            [1, 3, 1, 3]
        ], dtype=np.float_)
        impl.fixRowZero(A)
        impl.fixRowOne(A)
        self.assertEqual(A[1][0], 0)
        self.assertEqual(A[1][1], 1)

    def test_fixRowTwo(self):
        A = np.array([
            [0, 7, -5, 3],
            [2, 8, 0, 4],
            [3, 12, 0, 5],
            [1, 3, 1, 3]
        ], dtype=np.float_)
        impl.fixRowZero(A)
        impl.fixRowOne(A)
        impl.fixRowTwo(A)
        self.assertEqual(A[2][0], 0)
        self.assertEqual(A[2][1], 0)
        self.assertEqual(A[2][2], 1)

    def test_fixRowThree(self):
        A = np.array([
            [0, 7, -5, 3],
            [2, 8, 0, 4],
            [3, 12, 0, 5],
            [1, 3, 1, 3]
        ], dtype=np.float_)
        impl.fixRowZero(A)
        impl.fixRowOne(A)
        impl.fixRowTwo(A)
        impl.fixRowThree(A)
        self.assertEqual(A[3][0], 0)
        self.assertEqual(A[3][1], 0)
        self.assertEqual(A[3][2], 0)
        self.assertEqual(A[3][3], 1)

    def test_convertToEchelon(self):
        A = np.array([
            [0, 7, -5, 3],
            [2, 8, 0, 4],
            [3, 12, 0, 5],
            [1, 3, 1, 3]
        ], dtype=np.float_)
        impl.convertToEchelon(A)
        print(A)

    #
    # def test_singular(self):
    #     A = np.array([
    #         [0, 1, 1],
    #         [1, 0, 1],
    #         [0, 1, 0],
    #     ], dtype=np.float_)
    #     impl.convertToEchelon(A)
    #     print(A)
    #     print(np.linalg.det(A))