Absolutely! Here are 10 practice questions on vectors, ranging from basic to more advanced, based on what you've been learning:

## **Basic Questions**

**Question 1:** Create a vector `a = [3, 7, 2, 8]`. Calculate its norm manually (without NumPy's built-in norm function).

**Question 2:** For vector `b = [10, 0, -10, 5]`, what is its norm? Which component contributes the most to the norm?

**Question 3:** Create two vectors `p = [1, 2, 3]` and `q = [4, 5, 6]`. Compute the vector sum `p + q` and then find the norm of the result.

## **Unit Vector Questions**

**Question 4:** Vector `v = [0.6, 0.8]` is claimed to be a unit vector. Verify this without using code (just on paper). Is it actually a unit vector?

**Question 5:** Given `w = [4, 3]`, find its unit vector by hand (fraction form is fine). Then verify the unit vector's norm equals 1.

**Question 6:** If you have a zero vector `z = [0, 0, 0, 0]` and try to normalize it, what problem occurs? How should you handle this in code?

## **Dimension & Properties Questions**

**Question 7:** What's the difference between a 3D vector `[1, 2, 3]` and a 4D vector `[1, 2, 3, 0]`? Are they the same? Why or why not?

**Question 8:** Create a random 10-dimensional vector. Normalize it. Prove that multiplying the normalized vector by its original norm gives back the original vector.

## **Application Questions**

**Question 9:** In machine learning, two vectors representing images have norms of 5.2 and 3.7 respectively. If you normalize both vectors, what will their new norms be? Why?

**Question 10:** Write a function that takes a list of vectors (of any dimensions) and returns only those that are already unit vectors (within tolerance of 1e-5). Test it with: `[[1,0,0], [0.5,0.5,0.5], [0.6,0.8], [3,4], [1,1,1,1]]`

---

## **Bonus Challenge Question:**

**Question 11:** Prove mathematically that for any non-zero vector `v`, the vector `u = v / ||v||` always has a norm of exactly 1. (Hint: Use the properties of norms and scaling)

---

## **Answer Key (Try first, then check):**

<details>
<summary>Click for answers</summary>

**Q1:** `||a|| = √(9 + 49 + 4 + 64) = √126 ≈ 11.225`

**Q2:** `||b|| = √(100 + 0 + 100 + 25) = √225 = 15`. The components 10 and -10 contribute equally (100 each).

**Q3:** `p+q = [5, 7, 9]`, `||p+q|| = √(25 + 49 + 81) = √155 ≈ 12.45`

**Q4:** `0.6² + 0.8² = 0.36 + 0.64 = 1.0` ✓ Yes, it's a unit vector!

**Q5:** Norm = √(16 + 9) = √25 = 5. Unit vector = `[4/5, 3/5] = [0.8, 0.6]`. Check: `0.64 + 0.36 = 1.0` ✓

**Q6:** Division by zero! In code, check `if norm == 0: return v` or raise an error.

**Q7:** Not the same. The 4D vector has an extra dimension with value 0. They represent points in different dimensional spaces.

**Q8:** If `u = v/||v||`, then `u * ||v|| = (v/||v||) * ||v|| = v` ✓

**Q9:** Both will have norm = 1. Normalization always scales any non-zero vector to length 1, regardless of original length.

**Q10:** Only `[1,0,0]` and `[0.6,0.8]` are unit vectors. `[0.5,0.5,0.5]` has norm ≈ 0.866, `[3,4]` has norm 5, `[1,1,1,1]` has norm 2.

**Q11:** `||u|| = ||v/||v|| || = (1/||v||) * ||v|| = 1` (using the property that scaling a vector scales its norm by the same factor)

</details>

Want me to create more questions on a specific topic (like dot products, vector projection, or cosine similarity)?
