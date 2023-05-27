from gauss import *
from random import uniform

Rational_Matrix = [
    [Fraction(2, 1), Fraction(1, 1), Fraction(0, 1), Fraction(0, 1)],
    [Fraction(3, 1), Fraction(5, 1), Fraction(-1, 1), Fraction(-3, 1)],
    [Fraction(0, 1), Fraction(3, 1), Fraction(-1, 1), Fraction(0, 1)],
    [Fraction(1, 1), Fraction(4, 1), Fraction(0, 1), Fraction(-2, 1)]
]

Real_Matrix = [
    [3.5, -2.0, 1.0],
    [-3.1, 5,6, 0.0],
    [4.7, 0.0, -1.3]
]

Small_Matrix = [[1]]

Big_Matrix = [list(uniform(0, 100) for i in range(100)) for j in range(100)]
