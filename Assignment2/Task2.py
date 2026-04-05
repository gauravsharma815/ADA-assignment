Task : Search

import time
import random
import matplotlib.pyplot as plt

def linear_search(arr, x):
for i in range(len(arr)):
if arr[i] == x:
return i
return -1

def binary_search(arr, x):
l, r = 0, len(arr) - 1
while l <= r:
mid = (l + r) // 2
if arr[mid] == x:
return mid
elif arr[mid] < x:
l = mid + 1
else:
r = mid - 1
return -1

sizes = [100, 500, 1000]

linear_times = []
binary_times = []

for n in sizes:
arr = sorted([random.randint(1, 10000) for _ in range(n)])
x = arr[-1]

```
start = time.time()
linear_search(arr, x)
linear_times.append(time.time() - start)

start = time.time()
binary_search(arr, x)
binary_times.append(time.time() - start)
```

plt.plot(sizes, linear_times, label="Linear Search")
plt.plot(sizes, binary_times, label="Binary Search")

plt.xlabel("Input Size")
plt.ylabel("Execution Time")
plt.title("Search Comparison")
plt.legend()

plt.savefig("plots/search_comparison.png")
plt.show()
