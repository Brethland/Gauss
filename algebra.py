from properties import *
from itertools import chain

# def fill(R):
#     ex_index = list(map(lambda t: t[0], R))
#     m = max(ex_index)
#     return [_ for i in range(m)]


# def to_normal_form(M):
#     return [list(map(fill, M[i])) for i in range(len(M))]


# def to_reduced_form(M):
#     return

# Get pivot coordinate for a single Row. Pass Matrix or Row as input?


def get_pivot(n: int, row: Row) -> tuple[int, int]:
    """Return the pivot_index of a row along with the row index received."""
    pivot_index = 0
    for val in row:
        if val == 0:
            pivot_index += 1
            continue
        else:
            return (pivot_index, n)


assert get_pivot(0, [1, 2, 3]) == (0, 0)
assert get_pivot(0, [0, 2, 3]) == (1, 0)


def get_pivots(m: M) -> list[tuple[int, int]]:
    pivots = []
    for i, row in enumerate(m):
        pivots.append(get_pivot(i, row))
    return pivots

    # return [ get_pivot(*enumerate(m)) ]

    # return list(map(get_pivot, *enumerate(m)))


print(get_pivots([[1, 2, 3], [0, 2, 3], [0, 0, 3]]))
assert get_pivots([[1, 2, 3], [0, 2, 3], [0, 0, 3]]) == [(0, 0), (1, 1), (2, 2)]


def scalar_mult(M1: M, k: F) -> M:
    """return k*m as scalar multiplication on matrix, k is from a field"""

    # TODO: Nicolas implement
    return [list(map(lambda t: k * t, M1[i])) for i in range(len(M1))]


def add(M1: M, M2: M) -> tuple[M, str]:
    """element-wise addition of two matrices. in functional style.

    fp alternative approch using map:
    >>> from operator import add
    >>> list( map(add, list1, list2) )
    [5, 7, 9]
    """

    if len(M1) != len(M2):
        return ((), "Rank is not identified")
    return ([sum(x) for x in zip(M1, M2)], "")


def add_iterative(M1: M, M2: M) -> M:
    """element-wise addition of two matrices. naive iterative way."""

    assert len(M1) == len(M2)  # extract to properties.py

    # element-wise addition, non-functional
    M_sum = []
    for row_index in range(len(M1)):
        row_sum = []
        for col_index in range(len(M1[0])):
            row_sum.append(M1[row_index][col_index] + M2[row_index][col_index])
        M_sum.append(row_sum)
    return M_sum


# M1 = [[1,2,3], [3,2,1]]
# M2 = [[1,1,1], [0,0,0]]
# print(M1)
# print(M2)
# print(add_iterative(M1, M2))


def column(M1: M, c: int) -> M:
    assert c <= len(M1[0])
    return [M1[i][c] for i in range(len(M1))]


def mult(M1: M, M2: M) -> M:
    """matrix multiplication, using naive method"""

    assert len(M1[0]) == len(M2)
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

    K1 = mult_strassen(add_iterative(A11, A22), add_iterative(B11, B22))
    K2 = mult_strassen(add_iterative(A21, A22), B11)
    K3 = mult_strassen(A11, add_iterative(B12, scalar_mult(B22, -1)))
    K4 = mult_strassen(A22, add_iterative(B21, scalar_mult(B11, -1)))
    K5 = mult_strassen(add_iterative(A11, A12), B22)
    K6 = mult_strassen(
        add_iterative(A21, scalar_mult(A11, -1)), add_iterative(B11, B12)
    )
    K7 = mult_strassen(
        add_iterative(A12, scalar_mult(A22, -1)), add_iterative(B21, B22)
    )

    C11 = add_iterative(K1, add_iterative(K4, add_iterative(scalar_mult(K5, -1), K7)))
    C12 = add_iterative(K3, K5)
    C21 = add_iterative(K2, K4)
    C22 = add_iterative(K1, add_iterative(scalar_mult(K2, -1), add_iterative(K3, K6)))

    C = []
    for block in [[C11, C12], [C21, C22]]:
        for row in zip(*block):
            C.append(list(chain.from_iterable(row)))
    return C


# M1 = [[1, 2], [3, 4]]
# M2 = [[1, 1], [1, 1]]
# print(mult_strassen(M1, M2))
