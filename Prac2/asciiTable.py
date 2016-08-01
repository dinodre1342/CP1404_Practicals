lower = 10
upper = 100
print("Enter a number (" + str(lower) + "-" + str(upper) + "):")

for i in range (10, 120, 11):
    print("{} {:>20}".format(i, chr(i)))

def getNum ():
    upper = int(input("Enter a number between (10-50):"))
    lower = int(input("Enter a number between (10-50):"))

    while True:
        if upper > lower:
            break
            print ("The Upper Value is too low.")
            upper = int(input("Enter a number between (10-50):"))

    for i in range (lower, upper, 11):
        print ("{}{:>20}".format(i, chr(i)).strip())

getNum()


