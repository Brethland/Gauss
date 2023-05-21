"""This file contains definitions of mathematical properties and check-functions."""

from typing import Union

# Custom data types:

# Matrix is a list of list of ints. This is a list of rows.
M = list[list[int]]

# Rationals as Integer-Tuples (are named tuples possible/better?)
Rat = tuple[int, int]  

#Supported fields are now \QQ and \RR
#TODO: Add an inclusion of \ZZ into \QQ so that it's mathematically correct
F = Union[Rat, float, int] 

#Num = union[int, float, Rat]
