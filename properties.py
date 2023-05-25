"""This file contains definitions of mathematical properties and check-functions."""

from fractions import Fraction

# Custom data types:

#Supported fields are now \QQ and \RR
#TODO: Add an inclusion of \ZZ into \QQ so that it's mathematically correct
F = Fraction | float | int 

Row = list[F]

# Matrix is a list of list of ints. This is a list of rows.
M = list[Row]

