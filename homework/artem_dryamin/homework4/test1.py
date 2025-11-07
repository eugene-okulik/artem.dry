my_dict = {
    'tuple': (1, 52, 'test', 'my', 'who'),
    'list': [16, 17, 18, 15, 'denis'],
    'dict': {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5},
    'set': {'artem', 'yan', 4, 5, 7}
          }
print(my_dict['tuple'][-1])
my_dict['list'].append(26)
my_dict['list'].pop(1)
my_dict['dict']['six'] = 6
my_dict['dict'].pop('one')
my_dict['set'].add('galya')
my_dict['set'].pop()
print(my_dict)
