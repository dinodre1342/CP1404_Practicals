class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def print_person(self, *args): #*args means variable number of inputs
        print("Length: ", len(args))
        for each in args:
            print(each)

    def print_others(self, **kwargs):
        print("Length: ", len(kwargs))
        for each in kwargs:
            print(each, "-> ", kwargs[each])

    def __str__(self):
        return "Person class, name={}, age={}".format(self.name, self.age)

class Student(Person):
    next_id = 1 #Class variable / Global variable

    def __init__(self, name="", age=0):
        super().__init__(name, age) #call base class Person init()
        #student_id = instance attribute
        self.student_id = Student.next_id
        Student.next_id += 1

    def __str__(self):
        return "Student class, name={}, age={}, id={}".format(self.name, self.age,self.student_id)