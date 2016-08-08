"""
Ask the user for their name
Tell them how many vowels are in their name
Example output

Name: Bobby McAardvark
Out of 16 letters, Bobby McAardvark has 4 vowel

Use the string.format() method for the last print.
"""
#num = 100
#name = "John"
#print ("testing {} , {} ".format(num, name))

vowels = "aeiouAEIOU"
counter = 0
user_input = Str(input("Enter your name!"))
user_input2 = user_input.lower()

for each in user_input2:
    if each in vowels:
        counter += 1

print ("Out of {} letters, {} has {} vowels".format(len(user_input), user_input, counter)



