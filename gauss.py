from algebra import *
from elementary_matrix import *
from functools import reduce

# TODO: Add step-by-step application of the elementary matrix stack for demonstration


def find_better_candidate(m : M, c: int, end_column: int, now_row: int) -> int:
    row_dim = len(m)
    if(c == end_column):
        return now_row
    
    col = column(m, c)
    for s in range(now_row + 1, row_dim) :
        if col[s] != 0:
            return s
    find_better_candidate(m, c + 1, end_column, now_row)

def gauss_algorithm_iterative(m : M, is_traced=False) -> tuple[M, int, list[M]]:
    """
    Perform Gauss algorithm (iterative)
    1. Get most-left column with non-zero values (find best row for first column, otherwise remove this column
    2. If the top-row value is zero --> SWAP R0 with last non-zero row (or put to bottom using nullrow_cnt)
    3. Normalize row 0, making the pivot 1. (not necessary)
    4. Make zeroes below the pivot (by adding the respective inverse multiple
    5. Perform 1-4 with remaining rows.
    """

    nullrow_cnt = 0
    now_row = 0
    now_column = 0
    row_dim = len(m)
    trace = []
    while(now_row < row_dim - nullrow_cnt):
        (pivot_index, pivot) = get_pivot(m[now_row])

        if(pivot_index == None) : #it's a nullrow
            swap = S(row_dim, now_row, row_dim - 1 - nullrow_cnt)
            trace.append(swap)
            m = mult(swap, m)
            nullrow_cnt += 1
        else:
            if(pivot_index > now_column): #there's still better pivot column at left
                better_candidate = find_better_candidate(m, now_column, pivot_index, now_row)
                swap = S(row_dim, now_row, better_candidate)
                trace.append(swap)
                m = mult(swap, m)
                (pivot_index, pivot) = get_pivot(m[now_row]) #after swapping, we must get the pivot again
            col = column(m, pivot_index)
            scalar = list(map(lambda c: c / pivot, col))
            for k in range(now_row + 1, row_dim - nullrow_cnt):
                if(-scalar[k] < 0 or -scalar[k] > 0): #if already 0, we don't need to do anything
                    addition = A(row_dim, k, now_row, -scalar[k])
                    trace.append(addition)
                    m = mult(addition, m)
            now_row += 1
            now_column += 1
    if(is_traced) :
        return (m, row_dim - nullrow_cnt, trace)
    else:
        return (m, row_dim - nullrow_cnt, None)

def normalize(m: M, is_traced=False) -> tuple[M, int, list[M]]:
    row_dim = len(m)
    (m, rank, trace) = gauss_algorithm_iterative(m, is_traced)
    pivots = get_pivots(m)
    for k in range(rank):
        mul = M(row_dim, rank - k - 1, 1 / pivots[rank - k - 1][1])
        if(is_traced):
            trace.append(mul)
        m = mult(mul, m)
        col_index = pivots[rank - k - 1][0]
        for r in range(rank - k - 1):
            if(-m[r][col_index] < 0 or -m[r][col_index] > 0):
                addition = A(row_dim, r, rank - k - 1, -m[r][col_index])
                if(is_traced) :
                    trace.append(addition)
                m = mult(addition, m)
    if(is_traced):
        return (m, rank, trace)
    else:
        return (m, rank, None)

def echelon_form(m : M):
    return gauss_algorithm_iterative(m)[0]

def rank(m: M) -> M:
    return gauss_algorithm_iterative(m)[1]

def reduced_echelon_form(m : M):
    return normalize(m)[0]

def inverse(m: M) -> M:
    (id, rank, trace) = normalize(m, True)
    assert(rank == len(m))
    trace.reverse()
    # if(rank != 1 and (rank & (rank - 1) != 0)):
    #     return reduce(mult_strassen, trace, I(rank))
    # else:
    return reduce(mult, trace, I(rank))
    
# show(inverse([[1, 1, 0], [0, 1, 1], [1, 1, 1]]))

def one_step(m: M, t: list[M]) -> tuple[M, list[M]]:
    assert(len(t) > 0)
    m = mult(t[0], m)
    show(m)
    return (m, t[1:])
