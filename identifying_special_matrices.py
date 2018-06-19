# GRADED FUNCTION
import numpy as np


def convertToEchelon(A):
    fixRowZero(A)
    fixRowOne(A)
    fixRowTwo(A)
    fixRowThree(A)
    return A


# Our function will go through the matrix replacing each row in order turning it into echelon form.
# If at any point it fails because it can't put a 1 in the leading diagonal,
# we will return the value True, otherwise, we will return False.
# There is no need to edit this function.
def isSingular(A):
    B = np.array(A, dtype=np.float_)  # Make B as a copy of A, since we're going to alter it's values.
    try:
        convertToEchelon(B)
    except MatrixIsSingular:
        return True
    return False


# This next line defines our error flag. For when things go wrong if the matrix is singular.
# There is no need to edit this line.
class MatrixIsSingular(Exception): pass


# For Row Zero, all we require is the first element is equal to 1.
# We'll divide the row by the value of A[0, 0].
# This will get us in trouble though if A[0, 0] equals 0, so first we'll test for that,
# and if this is true, we'll add one of the lower rows to the first one before the division.
# We'll repeat the test going down each lower row until we can do the division.
# There is no need to edit this function.
def fixRowZero(A):
    if A[0, 0] == 0:
        A[0] = A[0] + A[1]
    if A[0, 0] == 0:
        A[0] = A[0] + A[2]
    if A[0, 0] == 0:
        A[0] = A[0] + A[3]
    if A[0, 0] == 0:
        raise MatrixIsSingular()
    A[0] = A[0] / A[0, 0]
    return A


# First we'll set the sub-diagonal elements to zero, i.e. A[1,0].
# Next we want the diagonal element to be equal to one.
# We'll divide the row by the value of A[1, 1].
# Again, we need to test if this is zero.
# If so, we'll add a lower row and repeat setting the sub-diagonal elements to zero.
# There is no need to edit this function.
def fixRowOne(A):
    A[1] = A[1] - A[1, 0] * A[0]
    if A[1, 1] == 0:
        A[1] = A[1] + A[2]
        A[1] = A[1] - A[1, 0] * A[0]
    if A[1, 1] == 0:
        A[1] = A[1] + A[3]
        A[1] = A[1] - A[1, 0] * A[0]
    if A[1, 1] == 0:
        raise MatrixIsSingular()
    A[1] = A[1] / A[1, 1]
    return A


def addLowerRowUntilDiagonalIsNonZero(A, row):
    setLeadingElementsToZero(A, row)
    for i in range(row + 1, len(A)):
        if A[row][row] != 0:
            break
        A[row] = A[row] + A[i]
        setLeadingElementsToZero(A, row)
    if A[row][row] == 0:
        raise MatrixIsSingular


def setLeadingElementsToZero(A, row):
    for i in range(0, row):
        A[row] = A[row] - A[row][i] * A[i]


def setDiagonalToOne(A, row):
    A[row] = A[row] / A[row][row]


def setRowToEchelon(A, row):
    addLowerRowUntilDiagonalIsNonZero(A, row)
    if A[row, row] == 0:
        raise MatrixIsSingular()
    # Finally set the diagonal element to one by dividing the whole row by that element.
    setDiagonalToOne(A, row)
    return A

# This is the first function that you should complete.
# Follow the instructions inside the function at each comment.
def fixRowTwo(A):
    return setRowToEchelon(A, 2)

# You should also complete this function
# Follow the instructions inside the function at each comment.
def fixRowThree(A):
    return setRowToEchelon(A, 3)