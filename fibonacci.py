def slow_fib(n):
    if n <= 1: return n
    return slow_fib(n - 1) + slow_fib(n - 2)

print(slow_fib(20))

def fast_fib(n):
    memo = {0: 0, 1: 1}

    def fib_helper(x):
        if x not in memo:
            memo[x] = fib_helper(x - 1) + fib_helper(x - 2)
        return memo[x]
    
    return fib_helper(n)
    
print(fast_fib(20))