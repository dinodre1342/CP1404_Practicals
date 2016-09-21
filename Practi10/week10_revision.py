"""
Define a function that takes in 2 parameters.
The first parameter is an integer number, the second
parameter is a list of numbers.
The function check if the list of numbers are divisible by
the first input parameter or not.
eg of calling:
>>> get_divisor(2, [1, 2, 3, 4])
[2, 4]
"""

def get_divisor(num, num_list):
   # result = [1, 2, 3] # mutable list
   # result1 = (1, 2, 3) #immutable tuple
    result = []
    for each in num_list:
        if each % num == 0:
            result.append(each)
    return result

#print(get_divisor(5, [1, 2, 3, 4]))

"""
subjects = {"CP1401": (60, 70, 80),
            "CP1404": (70, 80, 90),
            "CP1406": (66, 77, 88)}
Print the above data with proper string formatting
eg.
     CP1401     60%     70%     80.00%
"""

def print_marks(subjects):
    for key, value in subjects.items():
        print("{:^16}{:>6d}%{:>6d}%{:>8.2f}%".format(key, value[0], value[1], value[2]))

subjects = {"CP1401": (60, 70, 80),
            "CP1404": (70, 80, 90),
            "CP1406": (66, 77, 88)}
#print_marks(subjects)

class Computer:
    def __init__(self, name ="", processor="i5"):
        self.name = name #instance variable
        self.processor = processor
    def __str__(self):
        return "The name is {}, processor {}".format(self.name, self.processor)

mba = Computer("Macbook Air", "i7") #instance / object
print(mba)
asus = Computer("Asus")
print(asus)