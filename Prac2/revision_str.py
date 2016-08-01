#my_str1 = 'this is first string'
#my_str2 = "this is second /n string"
#my_str3 = """this is my thirrd string"""

#print (my_str1)
#print (my_str2)
#print (my_str3)

#print ("""This is a timetable:
#1 x 2 = 2
#2 x 2 = 4""")

#print ("This is another timetable: ")

who = "John"
day = "Monday"
feeling = "Great"
new_string = "Hello " +who + ", Good " + day+"!"
print(new_string)
new_string2 = "Hello {}, Good {}!".format(who, day)
print(new_string2)

print("Hello {0}, Good {1}! What is your plan, {0}? Feeling {2}?".format(who, day, feeling))

short_string = "This"
print("Hello {}!!".format(short_string))
print("Hello {:20s}!!".format(short_string)) #String default is left aligned.
print("Hello {:>20s}!!".format(short_string)) #Align to right hand side
print("Hello {:^20s}!!".format(short_string)) #Align to centre

number1 = 512
print("This number is {:d}.".format(number1)) #d for integer variable
print("This number is {:10d}.".format(number1)) #number default to right aligned.
print("This number is {:<10d}.".format(number1)) #left aligned
print("The price is ${:.2f}.".format(number1)) #format with float and 2 decimal places.
print("The price is ${:010.2f}.".format(number1)) #format with float and 2 decimal places.