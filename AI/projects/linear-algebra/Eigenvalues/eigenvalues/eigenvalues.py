import numpy as np
# Simple 2x2 matrix
A = np.array([[4.0, 1.0],
[2.0, 3.0]])
# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print('Eigenvalues:', eigenvalues)
# [5. 2.]
print('Eigenvectors:')
# columns are eigenvectors
print(eigenvectors)
# Verify: A @ v = lambda * v for each eigenpair
for i in range(len(eigenvalues)):   
    v = eigenvectors[:, i]
# i-th column
lam = eigenvalues[i]
lhs = A @ v
rhs = lam * v
print(f'lambda={lam:.1f}: match = {np.allclose(lhs, rhs)}')
# For symmetric matrices, use eigh (more numerically stable)
S = A + A.T # make symmetric
lam_s, V_s = np.linalg.eigh(S)
# Verify eigendecomposition: S = V @ diag(lam) @ V^T
S_reconstructed = V_s @ np.diag(lam_s) @ V_s.T
print(np.allclose(S, S_reconstructed)) # True
# Covariance matrix example (used in PCA)
X = np.random.randn(100, 5) # 100 samples, 5 features
cov = X.T @ X / 100
# 5x5 covariance matrix
lam, V = np.linalg.eigh(cov)
print('Eigenvalues (variance explained):', lam[::-1].round(2))