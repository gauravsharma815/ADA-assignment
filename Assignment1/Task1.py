Task 1: Algorithm Growth Observation
Python Code :

import time
import math
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

times_const = []
times_linear = []
times_quad = []
times_log = []

for n in sizes:
    start = time.time()
    constant(n)
    times_const.append(time.time() - start)

    start = time.time()
    linear(n)
    times_linear.append(time.time() - start)

    start = time.time()
    quadratic(n)
    times_quad.append(time.time() - start)

    start = time.time()
    logarithmic(n)
    times_log.append(time.time() - start)

# Plot
plt.plot(sizes, times_const, label="O(1)")
plt.plot(sizes, times_linear, label="O(n)")
plt.plot(sizes, times_quad, label="O(n^2)")
plt.plot(sizes, times_log, label="O(log n)")
plt.legend()
plt.xlabel("Input Size")
plt.ylabel("Time")
plt.title("Growth of Algorithms")
plt.show()
