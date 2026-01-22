import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 8))
axs = fig.subplots(1, 1)


a = np.array([1, 2, 3])

print(type(a))
print(a.shape)
print(a.ndim)

b = np.array([[1, 2, 3], [3, 4, 5]])
print("=" * 20)
print(type(b))
print(b.shape)
print(b.ndim)
print("=" * 20)
print(b[1][0])
print(b[1, 1])
print("=" * 20)


c = np.array([[10 * j + i for i in range(10)] for j in range(16)])

print(c)

print("=" * 20)
cy, cx = c.shape
print(cy, cx)

print(c[2 : cy - 2, 2 : cx - 2])
print(c.dtype)
print(c.astype(np.float32))
print("=" * 20)

v1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
v2 = np.array([2, 2, 2, 2, 2, 2, 2, 2, 2, 2])

print(v1 * v2)
print(v1 * v2)

print(v1 + v2)
print(v1 + v2)

print(v1 - v2)
print(v1 - v2)


m1 = np.random.randint(1, 10, (5, 5))
m2 = np.random.randint(1, 10, (5, 5))

print(m1)
print(m2)
print("m1+m2")
print(m1 + m2)

print("m1*m2")
print(m1 * m2)

print("m1@m2")
print(m1 @ m2)

v3 = np.array([1, 2, 3, 4, 5])

print("m1 @ v3")
print(m1 @ v3)
