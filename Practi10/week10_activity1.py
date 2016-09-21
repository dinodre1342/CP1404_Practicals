"""
Write a function that takes an integer and prints the numbers from that down to 0.
The function will be called like this:
 print_down(10)
"""

def print_down(x):
    while x >= 0:
        print(x)
        x -= 1

def print_down_for(x):
    for each in range(x, -1, -1):
        print(each)

def print_down_recursion(x):
    print(x)
    # ending condition
    if x == 0:
        return
    else:
        x -= 1
        print_down_recursion(x)

print_down_recursion(10)

# fibonacci numbers = 0, 1, 1, 2, 3, 5, 8, 13, 21, 44, 65