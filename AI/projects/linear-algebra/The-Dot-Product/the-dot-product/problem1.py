# write a function dot_product(x, y) that computes 
# the dot product using only a loop and addition
# no np.dot or @. test it against op.dot on random vectors

import numpy as np

#first solution - generator style

def dot_product(x, y):

    if len(x) != len(y):
        raise ValueError("vectors must be of the same length")
    
    dot = sum(x[i] * y[i] for i in range (len(x)))
     
    return dot


#second solution

def dot_product_2(x, y):
    
    if len(x) != len(y):
        raise ValueError("Vectors must be of the same length")
    
    dot = 0

    for i in range(len(x)):

        dot = dot + (x[i] * y[i])

    return dot

test_x = np.array([1, 2, 3])

test_y = np.array([4, 5, 6])

my_result = dot_product_2(test_x, test_y)

print(my_result)

np_result = np.dot(test_x, test_y)

print(np_result)


#Test on 5 random pairs of vectors
for test_num in range(5):
 
    dim = np.random.randint(3, 8)
    x = np.random.randn(dim) * 10
    y = np.random.randn(dim) * 10
    
    my_result = dot_product_2(x, y)
    np_result = np.dot(x, y)
    
    print(f"Test {test_num + 1} (dimension {dim}):")
    print(f"  My result: {my_result}")
    print(f"  np.dot: {np_result}")
    print(f"  Match? {np.isclose(my_result, np_result)}")
    print("-" * 40)



