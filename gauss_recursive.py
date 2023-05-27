from gauss import *

trace = True

def find_pivot_row_index(column: Row) -> int:
    """ Assuming `column` contains a non-zero value, find it's (row) index"""
    for i in range(len(column)):
        if column[i] != 0:
            return i
        else:
            i += 1
            continue

def gauss_rec(m : M, nowrow: int, nowcol: int, n_rows: int, n_cols: int, stack, depth: int) -> M:
    """
    lastrow holds index of last nonzero-row.

    # NOT necessary. 0. Put all nullrows to the bottom
    1. Establish a useful toprow by finding left-most pivot row. Swap if necessary

    """
    # TODO: check if stack works like that
    # TODO: consider renaming "nowrow" to "toprow"

    indentation = '\t' * depth

    print(f"\n{indentation}Working on matrix of size {n_rows - nowrow} x {n_cols - nowcol}")

    if nowrow == n_rows - 1:
        return m, stack
    
    # 1. Skip any zero columns
    while is_nullrow(column(m, nowcol)):
        print(f"\n{indentation}Skipping at least one zero-column...")
        nowcol += 1

    print(f"\n{indentation}-- Establish a useful toprow --")

    # 2. Establish a useful toprow, swap if necessary. column(m, nowcol) is guaranteed to have a pivotrow
    pivot = m[nowrow][nowcol]
    if pivot == 0:
        elem_swap = S(n_rows, nowrow, find_pivot_row_index(column(m, nowcol))) 
        if trace:
            stack.append(elem_swap)
        m = mult(elem_swap, m)
        #show(elem_swap)
        if trace:
            #print(f"Swapped with good pivot row (using: S({n_rows}, {nowrow}, {find_pivot_row_index(column(m, nowcol))}))")
            print(f"\n{indentation}Swapped row {nowrow + 1} with good pivot row {find_pivot_row_index(column(m, nowcol)) + 1}\n")
            show_ident(m, depth)
    elif trace:
        print(f"\n{indentation}No need to swap rows. Current pivot is fine\n")
    

    pivot = m[nowrow][nowcol]
    assert pivot != 0

    print(f"\n{indentation}-- Create zeroes below the pivot --")
    # 3. Create zeroes below the pivot
    for rowindex in range(nowrow+1, n_rows): # TODO: create correct range definition!
    #for rowindex in range(1, n_rows - nowrow): # TODO: check range for recursive calls! Yep, there was a off-by-one bug
        if m[rowindex][nowcol] == 0: continue  # entry below pivot is already 0
        else:
            #list(map(show, stack))
            inv_scalar = -( m[rowindex][nowcol] / pivot)
            elem_add = A(n_rows, rowindex, nowrow, inv_scalar)
        # TODO: Collect all elementary matrices, reduce them, then apply to m.
        if trace:
            stack.append(elem_add)
        m = mult(elem_add, m)
        if trace:
            #print(f"Created 0 below pivot (using A({n_rows}, {rowindex}, {nowrow}, {inv_scalar}))")
            print(f"\n{indentation}Created 0 below pivot in row {rowindex + 1} by adding {inv_scalar} * row {nowrow + 1} to it.\n")
            show_ident(m, depth)


    return gauss_rec(m, nowrow + 1, nowcol + 1, n_rows, n_cols, stack, depth+1)
    

def gauss_rec_go(m: M):
    """run recursive gauss_split with initial values"""
    n_rows = len(m)
    n_cols = len(m[0])
    if n_rows == 1 and n_cols == 1: return m
    return gauss_rec(m, 0, 0, n_rows, n_cols, [], 0)

