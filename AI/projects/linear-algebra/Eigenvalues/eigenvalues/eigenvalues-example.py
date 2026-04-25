import numpy as np


np.random.seed(0)
# Create data with strong structure in one direction
n = 200
t = np.random.randn(n)
# 1D latent variable
X = np.column_stack([
3*t + 0.3*np.random.randn(n), # strongly correlated with t
1*t + 0.3*np.random.randn(n)
# less strongly correlated
])
# Compute covariance matrix
X_centered = X - X.mean(axis=0)
cov = X_centered.T @ X_centered / n
print('Covariance matrix:')
print(cov.round(2))
# Eigendecomposition
eigenvalues, eigenvectors = np.linalg.eigh(cov)
idx = np.argsort(eigenvalues)[::-1] # sort descending
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]
print('Eigenvalues:', eigenvalues.round(2))
print('Principal component 1:', eigenvectors[:,0].round(3))
# This vector points along the direction of most variance