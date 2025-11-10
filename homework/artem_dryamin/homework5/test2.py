a = 'результат работы программы: 9'
bbbb = a.index(':')
number = int(a[bbbb + 1:].strip())
print(number + 10)
