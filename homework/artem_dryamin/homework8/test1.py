import random

bonus = [True, False]


def sale():
    salary = int(input('what salary?'))
    rand_bonus = random.choice(bonus)
    if rand_bonus == True:
        total = salary + random.randint(100, 10000)
        print(f'{salary}, {rand_bonus} - ${total}')
    else:
        print(f'{salary}, {rand_bonus} - ${salary}')


sale()
