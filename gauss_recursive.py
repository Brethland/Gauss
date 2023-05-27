from gauss import *

def gauss_split(m : M, nowrow: int, nowcol: int) -> M:
    """
    0. Put all nullrows to the bottom
    1. Establish a useful toprow by finding left-most pivot row. Swap if necessary

    """
    # TODO: establish base case handling!
    n_rows = len(m)
    n_cols = len(m[0])

    # TODO: put to function, reestablish/update after any operation that can create 0-rows.
    # 0. All nullrows to the bottom
    n_zerorows = 0
    for i, row in enumerate(m):
        if is_nullrow(row):
            m = S(n_cols, i, )
            n_zerorows += 1
    rank = n_rows - n_zerorows

    
    #    last_useful_row = rank

    # 1. Establish a useful toprow
    ## Skip zero cols:
    while is_nullrow(col(nowcol)):
           nowcol += 1
    #if m[nowrow][0] == 0: #we need to swap
    better_candidate = nowrow
    for rowindex, value in enumerate(col(nowcol)):
        pass
    for rowindex in range()

    return gauss_split()

def gauss_split_go(m: M):
    """run recursive gauss_split with initial values"""
    return gauss_split(m, len(m), len(m[0]))

