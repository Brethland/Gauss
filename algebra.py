# Custom data types:

# Matrix is a list of list of ints. This is a list of rows.

M = list[list[int]]

Rat = tuple[int, int]  # Rationals as Integer-Tuples (are named tuples possible/better?)

#Num = union[int, float, Rat]


def fill(R):
    ex_index = list(map(lambda t: t[0], R))
    m = max(ex_index)
    return [_ for i in range(m)]


def to_normal_form(M):
    return [list(map(fill, M[i])) for i in range(len(M))]


def to_reduced_form(M):
    return


def scalar_mult(M, k):
    # TODO: docstring
    # TODO: Nicolas implement
    return [list(map(lambda t: (t[0], k * t[1]), M[i])) for i in range(len(M))]


def add(M1: M, M2: M) -> M:
    # TODO: docstring
    # TODO: Nicolas: implement

    assert len(M1) == len(M2) # extract to properties.py

    # element-wise addition, non-functional
    M_sum = []
    for row_index in range(len(M1)):
        row_sum = []
        for col_index in range(len(M1[0])):
            row_sum.append(M1[row_index][col_index] + M2[row_index][col_index])
        M_sum.append(row_sum)

    #if len(M1) != len(M2):
    #    return ((), "Rank is not identified")
    return M_sum

M1 = [[1,2,3], [3,2,1]]
M2 = [[1,1,1], [0,0,0]]
print(M1)
print(M2)
print(add(M1, M2))

def mult(M1, M2):
    return
