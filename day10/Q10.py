#Q10. Fibonacci, slow and fast. Write the plain recursive fib(n) (fib(n) = fib(n-1) + fib(n-2), with fib(0) = 0 and fib(1) = 1). Time it for n = 30 using the time module. Then write a second version that stores answers in a dictionary (memoization) and time it again. In a comment, explain why the first version is so slow.
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
n = 30
import time

start_time = time.time()
result = fib(n)
end_time = time.time()

print(f"Fibonacci({n}) = {result}")
print(f"Time taken (slow version): {end_time - start_time:.6f} seconds")

# Fast version with memoization
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
        return memo[n]

start_time = time.time()
result = fib_memo(n)
end_time = time.time()

print(f"Fibonacci({n}) = {result}")
print(f"Time taken (fast version): {end_time - start_time:.6f} seconds")


