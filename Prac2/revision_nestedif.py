#import math
# radius = float(input("Enter the radius:"))
# area = 2 * math.pi * radius
# print ("The area is", area)

temperature = float(input("Enter the temperature today:"))

if temperature > 35:
    if temperature == 36:
        print("It is very hot!")
    else:
        print ("It is horrible!")
    print ("It is hot anyway!")
elif temperature > 33:
    print("Don't go outdoor.")
else
    print("It is not too bad")
print ("Always printed")