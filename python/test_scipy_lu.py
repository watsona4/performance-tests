import sys
import random
import time
import numpy as np
import scipy.linalg as la

# Set paramters

n = int(sys.argv[1])
m = 20

# Construct random vector and matrix

start = time.time()

b = np.empty([m,n])

for i in xrange(m):
    for j in xrange(n):
        b[i,j] = i + j + 2

a = np.empty([n,n])

for i in xrange(n):
    for j in xrange(n):
        a[i,j] = 1.0/(i + j + 1.0)

end = time.time()

print '*** Python (SciPy) ***:  Construction = %.6f sec' % (end - start)

# Perform LU factorization

start = time.time()

(lu,piv) = la.lu_factor(a)

end = time.time()

print '*** Python (SciPy) ***:  Factorization = %.6f sec' % (end - start)

# Perform LU substitution

start = time.time()

x = np.empty([m,n])

for k in xrange(m):
    x[k] = la.lu_solve((lu,piv), b[k])

end = time.time()

print '*** Python (SciPy) ***:  Substitution = %.6f sec' % (end - start)
