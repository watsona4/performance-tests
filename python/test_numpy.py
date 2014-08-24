import sys
import random
import time
import numpy as np

# Set paramters

n = int(sys.argv[1])

# Construct random vector and matrix

start = time.time()

x = np.empty([n])

for i in xrange(n):
    x[i] = random.random()

a = np.empty([n,n])

for i in xrange(n):
    for j in xrange(n):
        a[i,j] = random.random()

end = time.time()

print '*** Numpy ***:  Construction = %.6f sec' % (end - start)

# Perform matrix-vector multiplication

start = time.time()

y = np.dot(a, x)

end = time.time()

print '*** Numpy ***:  Computation = %.6f sec' % (end - start)
