
from week8_demo1 import Person, Musician
from week8_demo1 import Student, IT_Student

john = Person("John", "20")
#john.print_person("aa", "bb")

#john.print_others(var1="cc", var2="dd")
print(john)

#Instantiate a new object
studentA = Student("Bob", 18)
print(studentA)
#print(studentA.__dict__)

studentB = Student("Bob", 17)
print(studentB)

#print("Student dict: ", Student.__dict__)
#print("Student B dict: ", studentB.__dict__)
#print(type(studentB))
print(studentA + studentB)
print(studentA == studentB)

studentC = Student("Ann", 20)

studentD = IT_Student("Ken", 10)
print(studentD)

#polymorphism
Person().speak()
Student().speak()
IT_Student().speak()

mozart = Musician()
