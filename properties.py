"""This file contains definitions of mathematical properties and check-functions."""

from typing import Union

# Custom data types:

#
Row = list[int]

# Matrix is a list of list of ints. This is a list of rows.
M = list[Row]

# Rationals as Integer-Tuples (are named tuples possible/better?)
Rat = tuple[int, int]  

#Supported fields are now \QQ and \RR
#TODO: Add an inclusion of \ZZ into \QQ so that it's mathematically correct
F = Union[Rat, float, int] 

#Num = union[int, float, Rat]


def all_pivots_are_one(m: M) -> bool:

    # TODO: Simplify by using a "get pivots" function
    for row in m:
        for val in row:
            if val == 0:
                continue
            if val != 1:
                return False
    return True

def below_pivots_only_zeroes(m: M) -> bool:
    return False

def is_row_echelon_form(m: M) -> bool:
    """Function to check if Matrix m is in row_echelon_form."""
    return all_pivots_are_one(m) and below_pivots_only_zeroes(m)

