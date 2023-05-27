from properties import *
from itertools import chain

def get_pivot(row: Row) -> tuple[int | None, F | None]:
    """Return the pivot_index of a row along with the column index received."""
    pivot_index = 0
    for val in row:
        if val == 0:
            pivot_index += 1
            continue
        else:
            return (pivot_index, row[pivot_index])
    return (None, None)

def get_pivots(m: M) -> list[tuple[int | None, F | None]]:
    return list(map(lambda row: get_pivot(row), m))


def scalar_mult(M1: M, k: F) -> M:
    """return k*m as scalar multiplication on matrix, k is from a field"""

    return [list(map(lambda t: k * t, M1[i])) for i in range(len(M1))]

def add(M1: M, M2: M) -> M:
    """element-wise addition of two matrices. naive iterative way."""

    assert len(M1) == len(M2) and len(M1[0]) == len(M2[0])  # extract to properties.py

    # element-wise addition, non-functional
    M_sum = []
    for row_index in range(len(M1)):
        row_sum = []
        for col_index in range(len(M1[0])):
            row_sum.append(M1[row_index][col_index] + M2[row_index][col_index])
        M_sum.append(row_sum)
    return M_sum


def column(M1: M, c: int) -> Row:
    assert c <= len(M1[0])
    return [M1[i][c] for i in range(len(M1))]


def mult(M1: M, M2: M) -> M:
    """matrix multiplication, using naive method"""

    assert len(M1[0]) == len(M2)
    if is_identity_matrix(M2):
        return M1
    return [
        [sum(x * y for x, y in zip(row, column(M2, c))) for c in range(len(M2[0]))]
        for row in M1
    ]


def blocking(M1: M, b: int) -> tuple[M, M, M, M]:
    return (
        [n[:b] for n in M1[:b]],
        [n[b:] for n in M1[:b]],
        [n[:b] for n in M1[b:]],
        [n[b:] for n in M1[b:]],
    )


def mult_strassen(M1: M, M2: M) -> M:
    """matrix multiplication, using Strassen's algorithm"""

    # TODO: check dimensions

    if len(M1) == 1:
        return mult(M1, M2)

    b = len(M1) // 2
    A11, A12, A21, A22 = blocking(M1, b)
    B11, B12, B21, B22 = blocking(M2, b)

    K1 = mult_strassen(add(A11, A22), add(B11, B22))
    K2 = mult_strassen(add(A21, A22), B11)
    K3 = mult_strassen(A11, add(B12, scalar_mult(B22, -1)))
    K4 = mult_strassen(A22, add(B21, scalar_mult(B11, -1)))
    K5 = mult_strassen(add(A11, A12), B22)
    K6 = mult_strassen(
        add(A21, scalar_mult(A11, -1)), add(B11, B12)
    )
    K7 = mult_strassen(
        add(A12, scalar_mult(A22, -1)), add(B21, B22)
    )

    C11 = add(K1, add(K4, add(scalar_mult(K5, -1), K7)))
    C12 = add(K3, K5)
    C21 = add(K2, K4)
    C22 = add(K1, add(scalar_mult(K2, -1), add(K3, K6)))

    C = []
    for block in [[C11, C12], [C21, C22]]:
        for row in zip(*block):
            C.append(list(chain.from_iterable(row)))
    return C

def all_pivots_are_one(m: M) -> bool:
    pivots = list(map(lambda t : t[1] ,get_pivots(m)))
    if(next((k for k in pivots if k != 1), 1) != 1):
        return True
    else:
        return False

def below_pivots_only_zeroes(m: M) -> bool:
    pivots_index = list(map(lambda t : t[0], get_pivots(m)))
    for (i,c) in enumerate(pivots_index):
        if(sum(column(m, c)[i + 1:]) != 0) :
            return False
    return True

def is_row_echelon_form(m: M) -> bool:
    """Function to check if Matrix m is in row_echelon_form."""
    return all_pivots_are_one(m) and below_pivots_only_zeroes(m)

