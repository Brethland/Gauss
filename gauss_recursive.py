from gauss import *

def find_pivot_row_index(column: Row) -> int:
    """ Assuming `column` contains a non-zero value, find it's (row) index"""
    for i in range(len(column)):
        if column[i] != 0:
            return i
        else:
            i += 1
            continue

def gauss_rec(m : M, nowrow: int, nowcol: int, n_rows: int, n_cols: int, stack) -> M:
    """
    lastrow holds index of last nonzero-row.

    # NOT necessary. 0. Put all nullrows to the bottom
    1. Establish a useful toprow by finding left-most pivot row. Swap if necessary

    """
    # TODO: check if stack works like that

    #if is_nullrow(m[nowrow])  # if first row is null row this exits right away.
    if nowrow == n_rows - 1:
        return m, stack
    
    # 1. Skip any zero columns
    while is_nullrow(col(nowcol)):
           nowcol += 1

    # 2. Establish a useful toprow, swap if necessary
    pivot = m[nowrow][nowcol]
    if pivot == 0:
        elem_swap = S(n_cols, nowrow, find_pivot_row_index(col(now_col))) 
        if trace:
            trace.append(elem_swap)
        m = mult(m, elem_swap)
    print(m)

    # 3. Create zeroes below the pivot
    for rowindex in range(n_rows - nowrow): # TODO: check range for recursive calls!
        if m[rowindex][nowcol] == 0:
            # as a heuristic, bubble those zero-leading rows down
            continue
        else:
            inv_scalar = -( m[rowindex][nowcol] / pivot)
            elem_add = A(n_rows, rowindex, nowrow, inv_scalar)
        # TODO: Collect all elementary matrices, reduce them, then apply to m.
        m = mult(m, elem_add)
        print(m)

    return gauss_rec(m, nowrow + 1, nowcol + 1, n_rows, n_cols, stack)
    

def gauss_rec_go(m: M):
    """run recursive gauss_split with initial values"""
    return gauss_rec(m, 0, 0, len(m), len(m[0]), []) # lastrow as len(m) - 1)

