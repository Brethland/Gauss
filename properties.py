"""This file contains definitions of mathematical properties."""

from fractions import Fraction

# Custom data types:

#Supported fields are now \QQ and \RR
#TODO: Add an inclusion of \ZZ into \QQ so that it's mathematically correct
F = Fraction | float | int 

Row = list[F]

# Matrix is a list of list of ints. This is a list of rows.
M = list[Row]


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
    print('\n'.join(['\t'.join([str(ele) for ele in row]) for row in m]))

    # 2 digits after floating point, only works for floating point though!
    #print('\n'.join(['\t'.join([f"{ele:.2f}" for ele in row]) for row in m]))
    print()
