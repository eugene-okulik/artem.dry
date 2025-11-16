def calc_decorator(func):
    def wrapper(a, b):
        if a < 0 or b < 0:
            return func(a, b, '*')
        elif a == b:
            return func(a, b, '+')
        elif a > b:
            return func(a, b, '-')
        else:
            return func(a, b, '/')
    return wrapper


@calc_decorator
def calc(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return "Деление на ноль!"
        return a / b


num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
result = calc(num1, num2)
print("Результат:", result)