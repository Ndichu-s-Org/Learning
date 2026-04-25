#this implements the core rotation from Algorithm 1 of the TurboQuant paper and verifies its key properties

import numpy as np

np.random.seed(42)

d = 256

#step 1: generate the random rotation matrix
G = np.random.randn(d, d)
Pi, _ = np.linalg.qr(G)

#Step 2: Create a worst case input vector (adverseraial: all mass on one coord)

x = np.zeros(d)
x[0] = 1.0 #all mass in one coordinate


#step 3: rotate
y = Pi @ x

# Before rotation: x[0]=1.0, all others=0
print('Before: max coord =', x.max(), ', min =', x.min())

# After rotation: coordinates spread out evenly
print('After: max coord =', y.max().round(4), ', std =', y.std().round(4))

# The std after rotation should be approx 1/sqrt(d) = 1/sqrt(256) = 0.0625
print('Expected std:', 1/np.sqrt(d))

# Key: the norm is unchanged
print('||x|| =', np.linalg.norm(x))
print('||y|| =', np.linalg.norm(y))
