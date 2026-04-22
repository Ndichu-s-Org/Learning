Here are 10 practice questions about dot products, ranging from basic to advanced:

## **Basic Calculation Questions**

**Question 1:** Compute the dot product of `[2, 3]` and `[4, -1]` by hand.

**Question 2:** Calculate the dot product of `[1, 2, 3]` and `[4, 5, 6]`.

**Question 3:** Find the dot product of `[0, 0, 0, 0]` with `[5, 10, 15, 20]`. What pattern do you notice?

## **Direction & Angle Questions**

**Question 4:** Two vectors have a dot product of 0. What does this tell you about their directions? Give an example.

**Question 5:** Vector `a = [3, 4]` and `b = [6, 8]`. Calculate their dot product. What does the result tell you about their directions?

**Question 6:** If the dot product of two unit vectors is -0.5, what is the angle between them? (Hint: cos(θ) = dot product when both are unit vectors)

## **Properties & Patterns Questions**

**Question 7:** Calculate `[1, 0] · [1, 0]`, `[1, 0] · [0, 1]`, and `[0, 1] · [0, 1]`. What pattern do you notice with standard basis vectors?

**Question 8:** Compute the dot product of `[2, -1, 3]` with itself. How does this relate to the vector's norm?

## **Application Questions**

**Question 9:** Write a function `are_perpendicular(x, y, tolerance=1e-6)` that returns `True` if two vectors are perpendicular (dot product close to 0). Test on:
- `[1, 0]` and `[0, 1]`
- `[2, 3]` and `[-6, 4]`
- `[1, 2, 3]` and `[4, -2, 0]`

**Question 10:** A rectangle has vertices at (0,0), (4,0), (4,3), and (0,3). Use dot products to verify that the corners are right angles (90°). (Hint: Find vectors along the edges from one corner)

## **Bonus Challenge Questions**

**Question 11:** Prove mathematically that `x · y = y · x` (commutative property) using the definition of dot product.

**Question 12:** If `x · y = 5` and `x · z = -3`, what is `x · (2y + 3z)`? (Use dot product properties without calculating individual components)

---

## **Answer Key (Try first, then check):**

<details>
<summary>Click for answers</summary>

**Q1:** (2×4) + (3×-1) = 8 - 3 = 5

**Q2:** (1×4) + (2×5) + (3×6) = 4 + 10 + 18 = 32

**Q3:** 0. Dot product with zero vector always equals 0.

**Q4:** They are perpendicular (90° angle). Example: `[1,0]` and `[0,1]` give dot product 0.

**Q5:** (3×6) + (4×8) = 18 + 32 = 50. Positive dot product means angle < 90° (actually b = 2a, so they point in exactly the same direction, angle = 0°).

**Q6:** cos(θ) = -0.5, so θ = arccos(-0.5) = 120° (or 2π/3 radians).

**Q7:** Results: 1, 0, 1. Standard basis vectors are perpendicular to each other and have norm 1.

**Q8:** (2×2) + (-1×-1) + (3×3) = 4 + 1 + 9 = 14. This equals the square of the norm: ||v||² = 14, so ||v|| = √14.

**Q9:** 
- `[1,0]` and `[0,1]`: dot = 0 → True
- `[2,3]` and `[-6,4]`: dot = (2×-6)+(3×4) = -12+12=0 → True
- `[1,2,3]` and `[4,-2,0]`: dot = (1×4)+(2×-2)+(3×0)=4-4+0=0 → True

**Q10:** From corner (0,0): edge1 = [4,0], edge2 = [0,3]. Dot = (4×0)+(0×3)=0 ✓. From corner (4,0): edge1 = [-4,0], edge2 = [0,3]. Dot = (-4×0)+(0×3)=0 ✓.

**Q11:** x·y = Σ(x_i × y_i) = Σ(y_i × x_i) = y·x (multiplication is commutative)

**Q12:** x·(2y+3z) = 2(x·y) + 3(x·z) = 2(5) + 3(-3) = 10 - 9 = 1

</details>

---

## **Quick Test Code for Questions 1-3:**

```python
import numpy as np

# Question 1
a = np.array([2, 3])
b = np.array([4, -1])
print(f"Q1: {np.dot(a, b)}")  # 5

# Question 2
c = np.array([1, 2, 3])
d = np.array([4, 5, 6])
print(f"Q2: {np.dot(c, d)}")  # 32

# Question 3
e = np.array([0, 0, 0, 0])
f = np.array([5, 10, 15, 20])
print(f"Q3: {np.dot(e, f)}")  # 0
```