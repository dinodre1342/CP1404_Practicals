"""
Exception
1. Try: try to run some risky method(s)
2. Except: When error/exception occures, here will try to find the matching except

Scenario:
1. When no exeption occurs, the code excute the try until the error, then move to matching except and execute.
2. When no exeption occurs, the try will execute finish and skip the except part.
"""

try:
    input_file = open("unknown.txt", "r")
    input_file.readline()
    input_file.close()
except FileNotFoundError:
    print("Error Occurs")
except:
    print ("Generic execption")
"""-------------------------------"""
try:
    number = int(input("Enter a number:"))
    print(10/number)
except ValueError:
    print("The number cannot be converted to int.")
except ZeroDivisionError:
    print("The number cannot be zero.")