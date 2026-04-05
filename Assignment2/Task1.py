Task 1: Growth

import time
import matplotlib.pyplot as plt

def constant(n):
return n + 1

def linear(n):
s = 0
for i in range(n):
s += i
return s

def quadratic(n):
s = 0
for i in range(n):
for j in range(n):
s += 1
return s

def logarithmic(n):
i = 1
while i < n:
i *= 2

sizes = [10, 100, 500, 1000]

t1, t2, t3, t4 = [], [], [], []

for n in sizes:
start = time.time()
constant(n)
t1.append(time.time() - start)

```
start = time.time()
linear(n)
t2.append(time.time() - start)

start = time.time()
quadratic(n)
t3.append(time.time() - start)

start = time.time()
logarithmic(n)
t4.append(time.time() - start)
```

plt.plot(sizes, t1, label="O(1)")
plt.plot(sizes, t2, label="O(n)")
plt.plot(sizes, t3, label="O(n^2)")
plt.plot(sizes, t4, label="O(log n)")

plt.xlabel("Input Size")
plt.ylabel("Execution Time")
plt.title("Algorithm Growth")
plt.legend()

plt.savefig("plots/growth_graph.png")
plt.show()
