try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    #fraction = numerator / denominator

except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")


finished = False
result = 0
while not finished:
    try:
        result = int(input("Enter a valid integer:"))
        finished = true
    except ValueError:
        print("Valid result is:", result)
print("Please enter a valid integer.")