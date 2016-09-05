import csv

my_file = open("data.csv", "r")
for row in my_file:
    print(row)
my_file.close()
#############################
"""
with open("data.csv", "r") as file_pointer:
    for each in file_pointer:
        print(each) """
###########################

csv_out = open("out.csv", "w")
csv_out_f = csv.writer(csv_out)

with open("data.csv", "r") as file_pointer:
    my_csv_reader = csv.reader(file_pointer)
    for row in my_csv_reader:
        print(row)
        if row[2] == "3":
            row.append("40")
        else:
            row.append("10")
    #['Fish fingers', '12.95', '2', 'r','10']
        csv_out_f.writerow(row)

csv_out.close()
# Activity
# Use "with" and "as" to open a csv file and display the data in list.
