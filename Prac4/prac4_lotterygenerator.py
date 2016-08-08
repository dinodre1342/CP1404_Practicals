import random

num_of_picks = int(input("Enter number of picks:"))

for i in range (num_of_picks):
    num_list = []
    for j in range(0, 6):
        rand_num = random.randint(1, 46)
        while rand_num in num_list:
            rand_num = random.randint (1,46)
        num_list.append(rand_num)
    num_list.sort()
    print(num_list)