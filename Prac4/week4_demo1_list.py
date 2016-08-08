numbers = []

for i in range (5):
    user_number = int(input("Enter number {}:".format(i+1)))
    numbers.append(user_number)

print ("The list output:", numbers)

names = ["John", "Jenny", "Joshua"]
print ("The names are:", names)
print ("The first name is :", names[0])
print("The length of name list: ", len(names))

numbers = [10, 70, 1, 100, 29]
print ("The max is :", max(numbers))
print ("The average is:", sum(numbers)/len(numbers))

mega_list = names.extend (numbers)
print ("Mega list: ", names)

random_list = ["abc", 123, 7.0]
print ("random list:", random_list)

for each_data in names: #using for loop to navigate list
    print(each_data, end="\t")

names[0] = "New name" #list is mutable
print ("\n", names)

#my_str = "abcde" # string is immutable
#my_str[0] = "z"

print("the raw numbers :", numbers)
numbers.sort()
print("the sorted numbers :", numbers)
numbers.reverse()
print("the reverse numbers :", numbers)

names = ["aaa", "zzz", "eee"]
print ("the original list:", names)
names.sort()
print ("the sorted list:", names)
print(names[-1])
print(names.sort())

test_string ="abcde"
print(test_string[::-1])

data1 = [10, 1, 100]
data2 = [10, 1, 100]
print(data1 == data2)
print(data1 is data2)

print (data1 == data3)
print (data1 is data3)

print ("a" in "abcd")
print ("ab" in "abcd")
print ("a" in ['a', 'b', 'c', 'd'])
print ("ab" in ['a', 'b', 'c', 'd'])