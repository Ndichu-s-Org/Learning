import numpy as np

#create a simple 2D rotation matrix

theta = np.pi / 4 #45 degrees

Q = np.array([[np.cos(theta), -np.sin(theta)]
              [np.sin(theta), np.cos(theta)]
              ])

print(np.allclose(Q.T @ Q, np.eye(2))) #True


#verifyy norm preservation
x = np.array([3.0, 4.0])
y = Q @ x
print(np.linalg.norm(x)) #5.0
print(np.linalg.norm(y)) #5.0 

#verify dot product preservation

a = np.array([1.0, 0.0])

b = np.array([0.0, 1.0])

Qa = Q @ a 

Qb = Q @ b

print(a @ b) #0.0

print(Qa @ Qb)  #0.0 (preserved)


#verify inverse = transpose
print(np.allclose(np.linalg.inv(Q), Q.T)) #True