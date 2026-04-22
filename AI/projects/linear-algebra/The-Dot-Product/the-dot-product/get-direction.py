import numpy as np

def angle_between(x, y):
    dot = np.dot(x, y)
    norm_x = np.sqrt(np.sum(x**2))
    norm_y = np.sqrt(np.sum(y**2))
    cos_angle = dot / (norm_x * norm_y)
    angle_rad = np.arccos(cos_angle)
    angle_deg = angle_rad * 180 / np.pi
    return angle_deg

# Test with your vectors
x = np.random.randn(3) * 10
y = np.random.randn(3) * 10

dot_result = np.dot(x, y)
angle = angle_between(x, y)

print(f"Vectors: {x}, {y}")
print(f"Dot product: {dot_result}")
print(f"Angle between them: {angle:.1f} degrees")

if dot_result > 0:
    print("→ Same general direction")
elif dot_result == 0:
    print("→ Perpendicular")
else:
    print("→ Opposite directions")