import datetime

my_time = 'Jan 15, 2023 - 12:05:33'
python_time = datetime.datetime.strptime(my_time, '%b %d, %Y - %H:%M:%S')
print(python_time.strftime('%B'))
print(python_time.strftime('%d.%m.%Y, %H:%M'))
