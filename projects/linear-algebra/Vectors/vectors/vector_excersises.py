import numpy as np



x = np.array([2, 5, -3, 1])

print(x.shape)

print(x[3])

norm_x = np.linalg.norm(x)

print(norm_x)

#norm manually

manual_norm = np.sqrt(x[0]**2 + x[1]**2 + x[2]**2 + x[3]**2)
print(manual_norm)


def unit_vector_concise(v):
    """More concise version using list comprehension for the norm."""
    norm = (sum(x**2 for x in v))**0.5
    return [x/norm for x in v] if norm != 0 else v

# Test the concise version on one vector
print("\nTesting concise version on a sample vector:")
v_test = np.array([3, 4])
u_test = unit_vector_concise(v_test)
print(f"Original: {v_test}")
print(f"Unit vector: {u_test}")
print(f"Norm: {sum(x**2 for x in u_test)**0.5}")