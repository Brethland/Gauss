from algebra import *
from elementary_matrix import *

# TODO: Add step-by-step application of the elementary matrix stack for demonstration


def gauss_algorithm_iterative(m : M, is_traced=False) -> tuple[M, int, list[M]]:
    """
    Perform Gauss algorithm (iterative)
    1. Get most-left column with non-zero values (find best row for first column, otherwise remove this column
    2. If the top-row value is zero --> SWAP R0 with last non-zero row (or put to bottom using nullrow_cnt)
    3. Normalize row 0, making the pivot 1. (not necessary)
    4. Make zeroes below the pivot (by adding the respective inverse multiple
    5. Perform 1-4 with remaining rows.

    Preparation:
    Sorting the rows absolutely decreasing top-down/left-right
    """
    nullrow_cnt = 0
    now_row = 0
    row_dim = len(m)
    col_dim = len(m[0])
    trace = []
    while(now_row < row_dim - nullrow_cnt):
        # print(now_row)
        (pivot_index, pivot) = get_pivot(now_row, m[now_row])
        if(pivot_index == None) :
            trace.append(S(row_dim, now_row, row_dim - 1 - nullrow_cnt))
            m[now_row], m[row_dim - 1 - nullrow_cnt] = m[row_dim - 1 - nullrow_cnt], m[now_row]
            nullrow_cnt += 1
        else:
            col = column(m, pivot_index)
            scalar = list(map(lambda c: c / pivot, col))
            for k in range(now_row + 1, row_dim - nullrow_cnt) :
                trace.append(A(row_dim, k, now_row, scalar[k]))
                m[k] = [m[k][i] - scalar[k] * m[now_row][i] for i in range(col_dim)]
            now_row += 1
    #TODO: sort rows with pivots index
    if(is_traced) :
        return (m, row_dim - nullrow_cnt, trace)
    else:
        return (m, row_dim - nullrow_cnt, None)

def gauss_algorithm(is_traced=False):
    """
    Gauss algorithm generating the necessary elementary matrices
    """
    return

def normalize(m: M, is_traced=False) -> tuple[M, int, list[M]]:
    row_dim = len(m)
    col_dim = len(m[0])
    (m, rank, trace) = gauss_algorithm_iterative(m, is_traced)
    pivots = get_pivots(m)
    for k in range(rank):
        if(is_traced):
            trace.append(M(row_dim, rank - k - 1, 1 / pivots[rank - k - 1][1]))
        m[rank - k - 1] = [m[rank - k - 1][i] / pivots[rank - k - 1][1] for i in range(col_dim)]
        col_index = pivots[rank - k - 1][0]
        for r in range(rank - k - 1):
            if(is_traced) :
                trace.append(A(row_dim, r, rank - k - 1, m[r][col_index]))
            m[r] = [m[r][i] - m[r][col_index] * m[rank - k - 1][i] for i in range(col_dim)]
    if(is_traced):
        return (m, rank, trace)
    else:
        return (m, rank, None)

print(normalize([[1, 2, 2], [2, 1, 3], [1, 1, 0]], True))
# print(gauss_algorithm_iterative([[0, 1, 1], [1, 0, 1], [1, 1, 1]]))

def echelon_form(m : M):
    return gauss_algorithm(m)[0]


def reduced_echelon_form(m : M):
    return


def trace_echelon_form(M):
    return gauss_algorithm(True)


def trace_reduced_echelon_form(M):
    return
