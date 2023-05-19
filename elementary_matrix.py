# identity matrix
def I(n) :
   return [ [(i, 1)] for i in range(n) ]

# r1 = r2, r2 = r1
def S(n, r1, r2) :
   s = I(n)
   s[r2], s[r1] = s[r1], s[r2]
   return s

# r1 = r1 * a
def M(n, r1, a) :
   m = I(n)
   m[r1] = [(r1, a)]
   return m

# r1 = r1 + r2 * a
def A(n, r1, r2, a) :
   a = I(n)
   a[r1].append((r2, a))
   return a
