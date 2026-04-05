Task 2: Linear vs Binary Search

import random
import time

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

for n in sizes:
    arr = sorted([random.randint(1, 10000) for _ in range(n)])
    x = arr[-1]  # worst case

    start = time.time()
    linear_search(arr, x)
    print("Linear:", n, time.time() - start)

    start = time.time()
    binary_search(arr, x)
    print("Binary:", n, time.time() - start)
