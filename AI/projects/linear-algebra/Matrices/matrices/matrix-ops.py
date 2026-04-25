import numpy as np

#create a matrix

A = np.array([[1, 2, 3],
              [4, 5, 6]
              ])

print(A.shape) #(2, 3) -- 2 rows, 3 columns

#Matrix-vector multiply

x = np.array([1.0, 2.0, 3.0])


y = A @ x

print(y) # [14. 32.]

# Manual: row 0 dot x = 1*1 + 2*2 + 3*3 = 1+4+9 = 14

B = np.array([[1, 0],
              [0, 1],
              [1, 1]
              ])

C = A @ B # (2x3) @ (3x2) -> (2x2)
print(C.shape) # (2, 2)


#Transpose
At = A.T
print(At.shape) #(3, 2)

M = np.array([[2.0, 1.0], [5.0, 3.0]])
I = np.eye(2) # 2x2 indentity
M_inv = np.linalg.inv(M)
print(np.allclose(M @ M_inv, I)) #True

# Shapes must be compatible for multiplication
# (3x4) @ (4x5) -> (3x5) OK
# (3x4) @ (3x5) -> ERROR: inner dims don't match


