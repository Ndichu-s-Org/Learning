import numpy as np

A = np.array([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [7.0, 8.0, 9.0]
])

Q, R = np.linalg.qr(A)

print('Q shape:', Q.shape) #(3, 3)
print('R shape:', R.shape) #(3, 3)

#verify Q is orthogonal
print(np.allclose(Q.T @ Q, np.eye(3))) #True

#verify reconstruction: A = Q @ R

print(np.allclose(A, Q @ R)) #True

d = 512
G = np.random.randn(d, d) #gaussian entries
Q, _ = np.linalg.qr(G) #only need Q

#verify it is truly orthogonal
print(np.allclose(Q.T @ Q, np.eye(d), atol=1e-5)) #true

print(np.allclose(Q @ Q.T, np.eye(d), atol=1e-5)) #true

#Rotate a unit vectoe and verify norm is preserved

x = np.random.randn(d)
x = x / np.linalg.norm(x)
y = Q @ x

print(f'||x|| = {np.linalg.norm(x):.6f}') #1.000000

print(f'||Qx|| = {np.linalg.norm(y):.6f}') #1.00000