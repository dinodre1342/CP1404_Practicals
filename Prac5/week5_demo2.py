my_list = []

for each in range (1, 5):
    my_list.append(each)

print(my_list)

#List comprehension
my_list2 = [data for data in range (1, 5)]
print (my_list2)

my_list3 = [data*100 for data in range (1, 5)]
print (my_list3)

my_list4 = ["*"*n for n in range (1, 10)]
print (my_list4)