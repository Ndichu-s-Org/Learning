import numpy as np

x = np.array([1.0, 2.0, 3.0])

y = np.array([4.0, 5.0, 6.0])

#Dot product - three eqquivalent ways

dot1 = np.dot(x, y)

dot2 = x @ y

dot3 = sum( x[i] * y[i] for i in range (len(x))) #manual

print (dot1, dot2, dot3) #all will give 32.0

#Geometric Interpretation

cos_theta = np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))

theta_deg = np.degrees(np.arccos(cos_theta))

print(f'Angle: {theta_deg:.2F} degrees')


#for unit vectors, dot product = cosine similarity directly

x_u = x / np.linalg.norm(x)

y_u = y / np.linalg.norm(y)

print(x_u @ y_u)

#orthogonal vectors: dot product = 0

a = np.array([1.0, 0.0, 0.0])

b = np.array([0.0, 1.0, 0.0])

print(a @ b)