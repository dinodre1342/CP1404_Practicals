score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")

elif score > 50:
    print("Passable")

elif score > 90:
    print("Excellent")

else:
    print("Bad")

print ("score")
