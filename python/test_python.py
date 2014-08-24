import sys
import random
import time

# Set paramters

n = int(sys.argv[1])

# Construct random vector and matrix

start = time.time()

x = [random.random() for i in xrange(n)]

a = [[random.random() for i in xrange(n)] for j in xrange(n)]

y = [0.0 for i in xrange(n)]

end = time.time()

print '*** Python ***:  Construction = %.6f sec' % (end - start)

# Perform matrix-vector multiplication

start = time.time()

for i in xrange(n):
    for j in xrange(n):
        y[i] += a[i][j]*x[j]

end = time.time()

print '*** Python ***:  Computation = %.6f sec' % (end - start)
