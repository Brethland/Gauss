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


### Properties

- rank
- kernel
- basis
- span: 
  - the span of two vectors is the set of all their linear combinations
  - the span of a matrix is based on what? on the basis vectors?
  - the cnocept of span takes into account, linear dependent vectors inside the matrix,
  describing the space of the "useful" vectors only, disregarding redundant vectors, so to speak.
  ich linearly independent vector (to all others in a matrix) adds a new dimension to be reached through linear combination of this vector together with the others.


### Other stuff

_linear_ transformations have two properties: 
- all lines must remain lines
- origin must be fixed in place

- this keeps all parallel parallel
- grid lines stay parallel and evenly spaced


