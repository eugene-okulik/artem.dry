def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def nth_fib(n):
    gen = fibonacci()
    for _ in range(n):
        next(gen)
    return next(gen)


print(nth_fib(5))
print(nth_fib(200))
print(nth_fib(1000))
print(nth_fib(100000))
