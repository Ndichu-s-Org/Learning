import numpy as np


#create vectors

x = np.array([1.0, 2.0, 3.0])

y = np.array([4.0, 5.0, 6.0])


#vector addition
z = x + y
print (z)

#scalar multiplication
w = 2.5 * x

print (w) 

#L2 norm (Euclidean distance)
norm_x = np.linalg.norm(x)
print (norm_x)

#verify manually
manual_norm  = np.sqrt(x[0]**2 + x[1]**2 + x[2]**2)
print(np.isclose(norm_x, manual_norm))

#normalize to unit vector
x_unit = x / np.linalg.norm(x)
print(np.linalg.norm(x_unit))

#High dimensional vectors work identically
d = 1536
v = np.random.randn(d) # random 1536-dimensional vector
v_unit = v/np.linalg.norm(v)
print(np.linalg.norm(v_unit))
