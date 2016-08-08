import random

lines = int(input("how many quick picks?"))

for each in range(lines):
    lottery_numbers = []
    x = 0
    while x < 6:
        lottery_numbers.append(random.randint(1, 49))
        x += 1
    lottery_numbers.sort()
    random.sample(range(1, 49),6)
    print(lottery_numbers)