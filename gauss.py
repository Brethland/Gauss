
# TODO: Generate list (queue) of row/column indices of the places that should become a zero
# TODO: Generate elementary matrices based on the queue

def gauss_algorithm_iterative(is_traced=False):
    """
    Perform Gauss algorithm (iterative)
    1. Get most-left column with non-zero values
    2. If the top-row value is zero --> SWAP R0 with first non-zero row (or put to bottom?)
    3. Normalize row 0, making the pivot 1.
    4. Make zeroes below the pivot (by adding the respective inverse multiple
    5. Perform 1-4 with remaining rows.

    Preparation:
    Sorting the rows decreasing top-down/left-right
    """
    return

def gauss_algorithm(is_traced=False):
    """
    Gauss algorithm generating the necessary elementary matrices
    """
    return

def normalize(is_traced=False):
    return


def echelon_form(M):
    return gauss_algorithm()[0]


def reduced_echelon_form(M):
    return


def trace_echelon_form(M):
    return gauss_algorithm(True)


def trace_reduced_echelon_form(M):
    return
