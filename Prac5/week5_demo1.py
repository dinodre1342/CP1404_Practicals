import random

lunch_list = ['chicken rice', 'fried rice', 'sandwich']
dinner_tuple = ('udon noodles', 'bbq chicken', 'beef wraps')

#print (lunch_list[1])
#print (dinner_tuple [-1])

lucky_no = random.randint(0, len(lunch_list)-1)
print("Today your lucky lunch is {}".format(lunch_list[lucky_no]))

lucky_no = random.randint(0, len(dinner_tuple)-1)
print ("Lucky dinner is {}".format(dinner_tuple[lucky_no]))

lunch_list.sort()
#dinner_tuple.sort () - Not Allowed