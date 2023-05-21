"""Generator functions of elementary matrices."""

# identity matrix
def I(n):
    return [[(i, 1)] for i in range(n)]


# r1 = r2, r2 = r1

# TODO: Maybe these functions should receive the matrix as input instead of just n? not sure
def S(n, r1, r2):
    """elementary matrix to swap rows r1 and r2"""
    s = I(n)
    s[r2], s[r1] = s[r1], s[r2]
    return s


# r1 = r1 * scalar
def M(n, r1, scalar):
    """elementary matrix to multiply (scale) a row"""
    assert scalar < 0 or scalar > 0
    elementary_scaled = I(n)
    #m[r1] = [(r1, scalar)]
    elementary_scaled[r1] = scalar
    return elementary_scaled


# r1 = r1 + r2 * scalar
def A(n, r1, r2, scalar):
    """elementary matrix to add a multiple of r2 to r1"""
    assert scalar < 0 or scalar > 0
    elementary_added = I(n)
    # appending is wrong, no? a[r1].append((r2, a)). also there was a name clash with variable `a`
    elementary_added[r1][r2] = scalar
    
    return elementary_added
