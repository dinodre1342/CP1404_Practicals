from week8_demo1 import Person
from week8_demo1 import Student

john = Person("John", "20")
#john.print_person("aa", "bb")

#john.print_others(var1="cc", var2="dd")
print(john)

#Instantiate a new object
studentA = Student("Amy", 18)
print(studentA)
#print(studentA.__dict__)

studentB = Student("Bob", 21)
print(studentB)

print("Student dict: ", Student.__dict__)
print("Student B dict: ", studentB.__dict__)