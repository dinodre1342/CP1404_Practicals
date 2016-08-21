import string

UPPER = string.ascii_uppercase

def check(names):
    for each in names:
        if each in UPPER:
            return True


while True:
    names = input("Please input your name:")
    if not check(names):
        print("Invalid.")
    else:
        break


print(names)