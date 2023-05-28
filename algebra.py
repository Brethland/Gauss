"""Generator functions of elementary matrices."""

from itertools import chain
from fractions import Fraction

# Custom data types:

#Supported fields are now \QQ and \RR
#TODO: Add an inclusion of \ZZ into \QQ so that it's mathematically correct
F = Fraction | float | int 

Row = list[F]

# Matrix is a list of list of ints. This is a list of rows.
M = list[Row]

### Elementary Matrices

def I(n: int) -> M:
    """return an identity matrix with dimension n"""

    return [[0 if j != i else 1 for j in range(n)] for i in range(n)]

def S(n: int, r1: int, r2: int) -> M:
    """return a swap matrix by row r1 and r2 with dimension n"""

    s = I(n)
    s[r2], s[r1] = s[r1], s[r2]
    return s

def M(n: int, r1: int, a: F)  -> M:
    """return a scale matrix by row r1 with argument a and dimension n"""

    assert a < 0 or a > 0
    elementary_scaled = I(n)
    elementary_scaled[r1][r1] = a
    return elementary_scaled

def A(n: int, r1: int, r2: int, a: F) -> M:
    """return an append matrix by row r1 and r2 with argument a and dimension n
    
    r1 = r1 + r2 * a
    """

    assert a < 0 or a > 0
    elementary_added = I(n)
    elementary_added[r1][r2] = 1 + a if r1 == r2 else a
    return elementary_added

### Properties

def is_nullrow(row: Row) -> bool:
    for value in row:
        if value != 0:
            return False
    return True

# duplicate to not introduce circular imports...
def I(n: int) -> M:
    """return an identity matrix with dimension n"""
    return [[0 if j != i else 1 for j in range(n)] for i in range(n)]


def is_identity_matrix(m: M) -> bool:
    """Tests if matrix m is identity matrix"""
    return m == I(len(m))


def show(m: M):
    isfloat = isinstance(m[0][0], float)
    print('\n'.join(['\t'.join([f"{ele:.2f}" if isfloat else str(ele) for ele in row]) for row in m]))

    # 2 digits after floating point, only works for floating point though!
    #print('\n'.join(['\t'.join([f"{ele:.2f}" for ele in row]) for row in m]))
    print()

def show_ident(m: M, indent: int):
    indentation = '\t' * indent
    isfloat = isinstance(m[0][0], float)
    for row in m:
        print(indentation, end='')
        print('\t'.join([f"{elem:.2f}" if isfloat else str(elem) for elem in row]))

def get_pivot(row: Row) -> tuple[int | None, F | None]:
    # TODO: this doc-string is not uptodate
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


def one_step(m: M, t: list[M]) -> tuple[M, list[M]]:
    """
    Takes inverted list of elementary matrices, pops the first matrix
    to apply and returns the transformed matrix as well as the remaining
    elementary matrices.

    Thus this performs a single action of Gauss elimination.
    """
    assert(len(t) > 0)
    m = mult(t[0], m)
    show(m)
    return (m, t[1:])


class StepByStep:
    """A class containing matrix and a stack of elementary operations,
    applying them one by one"""
    def __init__(self, matrix, stack):
        self.matrix = matrix
        self.elementary_stack = stack
    def __next__(self):
        if len(self.matrix) == 0:
            print()
        else:
            self.matrix = mult(self.elementary_stack[0], self.matrix)
            show(self.matrix)
            self.elementary_stack = self.elementary_stack[1:]
        return self.matrix

