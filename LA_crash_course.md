# Linear Algebra Crash Course

Concepts and Terminology relevant to our project.


## Basic Data Structures

- Matrix: A matrix is a list of rows (vectors), where all rows have equal length. `Mat = list[Vec]`
- Vector: A vector is a `1*n` (row vector) or `n*1` (col vector) matrix `Vec = list[float]`

- Pivot: the pivot element is the first non-zero element of a row/Vec
  - important property of rowechelon form



### Special Matrices (helpful for tests)

- Identity: Diagonal with only ones (1)
- Elementary: A matrix which can be derived from Identity with only one gaussian operation (add, scale, swap)
- Diagonal: A square matrix (n==m), all non-diagonal entries (i != j) are zero
- Triangular: A square matrix (n==m)(Gauss algorithm should return a Matrix of this form)
  - Stufenmatrix in more general - non-square case


- row-echelon form: all 0-rows are at the bottom. 
- reduced row-echelon form: all pivots are 1. Only zeroes below the pivot

- rank
- kernel
- basis 


