from properties import *

def I(n: int) -> M:
    """return an identity matrix with dimension n"""

    return [[0 if j != i else 1 for j in range(n)] for i in range(n)]

# TODO: Maybe these functions should receive the matrix as input instead of just n? not sure
def S(n: int, r1: int, r2: int) -> M:
    """return a swap matrix by row r1 and r2 with dimension n"""

    id = I(n)
    id[r2], id[r1] = id[r1], id[r2]
    return id

def M(n: int, r1: int, a: int)  -> M:
    """return a scale matrix by row r1 with argument a and dimension n"""

    # assert a < 0 or a > 0 #it's fine when a = 0
    id = I(n)
    id[r1][r1] = a
    return id

def A(n: int, r1: int, r2: int, a: int) -> M:
    """return an append matrix by row r1 and r2 with argument a and dimension n
    
    r1 = r1 + r2 * a
    """

    id = I(n)
    id[r1][r2] = 1 + a if r1 == r2 else a
    return id
