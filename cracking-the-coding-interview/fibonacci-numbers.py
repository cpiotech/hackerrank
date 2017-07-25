# Memoization
memo = {}
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    result = fibonacci(n - 1) + fibonacci(n - 2)
    memo[n] = result
    return result
n = int(raw_input())
print(fibonacci(n))
