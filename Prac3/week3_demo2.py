"""
write code to read a file like this and print each part seperately with the price formatted like currency
"""

file_reader = open("data2.txt", "r")
print(file_reader.read())

#print(file_reader.read())

for line in file_reader:
     #Fender Stratocaster, 2014, 765.40\n
    line = line.strip ()
    line = line.replace("\\n","")
    datum = line/split(",")
    print("Model: {:s}\nYear:{:s}\nPrice:${:s}".format(datum[0],datum[1],datum[2]))
    print ("************")
    print(line)

file_reader.close()





