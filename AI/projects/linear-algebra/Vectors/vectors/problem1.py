# write a function normalize (v) that returns the unit vector int he same direction as v.
# dont use np.linalg.norm, compute the norm manually. 
# test it on 5 random vectors and rectify each output is 1.0

import numpy as np

def unit_vector(v):

    norm = np.sqrt(sum(x**2 for x in v))

    print(norm)

    unit = []

    for x in v:
        unit.append(x/norm)
    
    return unit





test_v = np.array([2, 5])

u_test = unit_vector(test_v)

print(u_test)

#verify norm of unit vector is 1.0

verify_norm = np.sqrt(sum(x**2 for x in u_test))
print(verify_norm)