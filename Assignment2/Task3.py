Task : Recursion

import time

call_count = 0

def factorial(n):
global call_count
call_count += 1
if n == 0:
return 1
return n * factorial(n - 1)

def fib_recursive(n):
global call_count
call_count += 1
if n <= 1:
return n
return fib_recursive(n-1) + fib_recursive(n-2)

def fib_dp(n):
dp = [0]*(n+1)
if n > 0:
dp[1] = 1
for i in range(2, n+1):
dp[i] = dp[i-1] + dp[i-2]
return dp[n]

n = 10

call_count = 0
start = time.time()
factorial(n)
print("Factorial Calls:", call_count, "Time:", time.time()-start)

call_count = 0
start = time.time()
fib_recursive(n)
print("Recursive Fibonacci Calls:", call_count, "Time:", time.time()-start)

start = time.time()
fib_dp(n)
print("DP Fibonacci Time:", time.time()-start)
