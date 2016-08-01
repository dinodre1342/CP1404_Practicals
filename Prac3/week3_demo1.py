#Open afile for reading,
#open () returns afile pointer and store in file_reader object
#open() takes in 2 parameters, first is the filename or full path, second is mode:r/w/a
file_reader = open ("data.txt", "r")
#create anew file object for file writing
file_writer = open ("output.txt", "w")
file_writer2 = open("output2.txt", "w")

print(file_reader.read())
""""""

for each_line in file_reader:
    #splitting the data by comma
    datum = each_line.split (",") #datum[0]=john, datum[1]= 20
    print("{:s}/\t:{:s}".format(datum[0],datum[1]))
    #print the formateed data to the file which is pointed by file_writer
    print("{:s}\t:{:s}".format(datum[0],datum[1]))

    #Second way of writing text to file
    file_writer2.write("{:s\t:{:s}".format(datum[0],datum[1]))
    #print(each_line)


file_reader.close()
file_writer.close()