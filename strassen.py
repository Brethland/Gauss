def blocking(M1: M, b: int) -> tuple[M, M, M, M]:
    return (
        [n[:b] for n in M1[:b]],
        [n[b:] for n in M1[:b]],
        [n[:b] for n in M1[b:]],
        [n[b:] for n in M1[b:]],
    )


def mult_strassen(M1: M, M2: M) -> M:
    """matrix multiplication, using Strassen's algorithm"""

    # TODO: check dimensions

    if len(M1) == 1:
        return mult(M1, M2)

    b = len(M1) // 2
    A11, A12, A21, A22 = blocking(M1, b)
    B11, B12, B21, B22 = blocking(M2, b)

    K1 = mult_strassen(add(A11, A22), add(B11, B22))
    K2 = mult_strassen(add(A21, A22), B11)
    K3 = mult_strassen(A11, add(B12, scalar_mult(B22, -1)))
    K4 = mult_strassen(A22, add(B21, scalar_mult(B11, -1)))
    K5 = mult_strassen(add(A11, A12), B22)
    K6 = mult_strassen(
        add(A21, scalar_mult(A11, -1)), add(B11, B12)
    )
    K7 = mult_strassen(
        add(A12, scalar_mult(A22, -1)), add(B21, B22)
    )

    C11 = add(K1, add(K4, add(scalar_mult(K5, -1), K7)))
    C12 = add(K3, K5)
    C21 = add(K2, K4)
    C22 = add(K1, add(scalar_mult(K2, -1), add(K3, K6)))

    C = []
    for block in [[C11, C12], [C21, C22]]:
        for row in zip(*block):
            C.append(list(chain.from_iterable(row)))
    return C

