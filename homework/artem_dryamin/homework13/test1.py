import os
import datetime


path = os.path.dirname(__file__)
base_path = os.path.dirname(os.path.dirname(path))
new_path = os.path.join(base_path, 'eugene_okulik', 'hw_13', 'data.txt')


def read_file():
    with open(new_path, 'r') as data_file:
        for line in data_file.readlines():
            yield line


lines = []


for data_line in read_file():
    lines.append(data_line[3:28])


a, b, c = lines


def datedate(l):
    l = datetime.datetime.strptime(l, "%Y-%m-%d %H:%M:%S.%f")
    return l


print(datedate(a) + datetime.timedelta(days=7))
print(datedate(b).strftime('%A'))
now = datetime.datetime.now()
new_date = now - datedate(c)
print(new_date.days)
