import sys
import random
import time
import numpy as np

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

print '*** Python (NumPy) ***:  Construction = %.6f sec' % (end - start)

# Perform LU factorization

start = time.time()

for k in xrange(n-1):
    for i in xrange(k+1,n):
        a[i,k] /= a[k,k]
        for j in xrange(k+1,n):
            a[i,j] -= a[i,k]*a[k,j]

end = time.time()

print '*** Python (NumPy) ***:  Factorization = %.6f sec' % (end - start)

# Perform LU substitution

start = time.time()

x = np.empty([m,n])

for k in xrange(m):

    x[k,0] = b[k,0]
    for i in xrange(1,n):
        s = 0
        for j in xrange(i-1):
            s += a[i,j]*x[k,j]
        x[k,i] = b[k,i] - s

    x[k,n-1] /= a[n-1,n-1]
    for i in xrange(n-2,-1,-1):
        s = 0
        for j in xrange(i+1,n):
            s += a[i,j]*x[k,j]
        x[k,i] = (x[k,i] - s)/a[i,i]

end = time.time()

print '*** Python (NumPy) ***:  Substitution = %.6f sec' % (end - start)
