name = str(input("Please Enter Your Name:"))

if len(name) == 0:
    print ("Your name can't be blank. ")
    name = str(input("Please Enter Your Name:"))

print ("Your name is {}".format(name))
print (name[1::2])
