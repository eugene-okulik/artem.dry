import sys

sys.set_int_max_str_digits(0)


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def nth_fib(n):
    gen = fibonacci()
    value = 0
    for i in range(n + 1):
        value = next(gen)
    return value


print(nth_fib(5))
print(nth_fib(200))
print(nth_fib(1000))
print(nth_fib(100000))
