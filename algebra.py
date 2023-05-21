# Custom data types:

# Matrix is a list of list of ints. This is a list of rows.

M = List[List[int]]

Rat = Tuple[int, int]  # Rationals as Integer-Tuples (are named tuples possible/better?)

Num = Union[int, float, Rat]


def fill(R):
    ex_index = list(map(lambda t: t[0], R))
    m = max(ex_index)
    return [_ for i in range(m)]


def to_normal_form(M):
    return [list(map(fill, M[i])) for i in range(len(M))]


def to_reduced_form(M):
    return


def scalar_mult(M, k):
    return [list(map(lambda t: (t[0], k * t[1]), M[i])) for i in range(len(M))]


def add(M1, M2):
    if len(M1) != len(M2):
        return ((), "Rank is not identified")
    return


def mult(M1, M2):
    return
