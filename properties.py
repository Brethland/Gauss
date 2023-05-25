"""This file contains definitions of mathematical properties."""

from fractions import Fraction

# Custom data types:

#Supported fields are now \QQ and \RR
#TODO: Add an inclusion of \ZZ into \QQ so that it's mathematically correct
F = Fraction | float | int 

Row = list[F]

# Matrix is a list of list of ints. This is a list of rows.
M = list[Row]

def show(m: M):
    print('\n'.join(['\t'.join([str(ele) for ele in row]) for row in m]))
