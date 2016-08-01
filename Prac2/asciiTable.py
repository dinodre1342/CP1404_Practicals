lower = 10
upper = 100
print("Enter a number (" + str(lower) + "-" + str(upper) + "):")

for i in range (10, 120, 11):
    print("{} {:>20}".format(i, chr(i)))

def get_number (lower, upper):
    print float(int(input("Please enter a number."))
except ValueError:
    print ("The number cannot be converted to int.")
