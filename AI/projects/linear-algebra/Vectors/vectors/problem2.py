#Generatee a random vector in 512 dimensions. normalize it. 
# verify that its norm is exactly 1.0 
# (use np.isclose with atol=1e-6 to check if the norm is close enough to 1.0).

import numpy as np

def normalize_v(v):
    norm = np.sqrt(np.sum(v**2))

    return v/norm



random_512d = np.random.randn(512)
normalized = normalize_v(random_512d)


#verify
computed_norm = np.sqrt(np.sqrt(np.sum(normalized**2)))

is_correct = np.isclose(computed_norm, 1.0, atol=1e-6)

print('vector dimension', {len(random_512d)})
print('norm after normalization', computed_norm)
print('within 1e-6 of 1.0?', {is_correct})
