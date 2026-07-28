# Day 16 – Object-Oriented Programming (OOP)

#What is a Class?
# What is an Object?
# Creating your first class
# Creating objects
# Calling methods


#1. c l a s s
#The design or blueprint used to make all these phones is called a Class.

#The actual phone in your hand is called an Object.

#syntax
#class Student:
#      pass                        class → Keyword to create a class.
#                                  Student → Name of the class.




#class → Keyword to create a class.

class Student:
    pass

student1 = Student()
#
class Student:
    pass

student1 = Student()

print(student1)




# Attributes:
#An attribute is simply information about an object
#real class 

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Radhika", 21)

print(student1.name)
print(student1.age)

#
student2 = Student("Anu", 20)

print(student2.name)
print(student2.age)
#
student3 = Student("Rahul", 22)
print(student3.name)
print(student3.age)






#methods              A method is simply a function inside a class.
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hello! My name is", self.name)
        print("I am", self.age, "years old.")

student1 = Student("Radhika", 21)

student1.introduce()


#Multiple Objects
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hello! My name is", self.name)
        print("I am", self.age, "years old.")
        print("-------------------")

student1 = Student("Radhika", 21)
student2 = Student("Anu", 20)
student3 = Student("Rahul", 22)

student1.introduce()
student2.introduce()
student3.introduce()


#challenge
class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("------------------")


car1 = Car("Toyota", "Fortuner")
car2 = Car("Hyundai", "Creta")

car1.show_details()
car2.show_details()





#Class         
#   ↓
#Constructor (__init__)
 #  ↓
#Attributes (self.name, self.age...)
 #  ↓
#Methods
 #  ↓
#Objects
 #  ↓
#Call Methods



# s e l f         the current object

class Student:

    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hello", self.name)

student1 = Student("Radhika")
student2 = Student("Anu")

student1.hello()
student2.hello()


#
class Dog:

    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name, "says Woof!")

dog1 = Dog("Tommy")
dog2 = Dog("Bruno")

dog1.bark()
dog2.bark()


#
class Student:

    def __init__(self, name):
        self.name = name
        print("Student object created!")

student1 = Student("Radhika")
student2 = Student("Anu")
student3 = Student("Rahul")


#
class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def details(self):
        print("Title :", self.title)
        print("Author:", self.author)
        print("---------------------")


book1 = Book("Python Basics", "Radhika")
book2 = Book("AI with Python", "Anu")

book1.details()
book2.details()











# I N H E R I T A N C E

class Person:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello! My name is", self.name)


class Student(Person):

    def study(self):
        print(self.name, "is studying Python.")


student1 = Student("Radhika")

student1.introduce()
student1.study()

#
class Teacher:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello! My name is", self.name)


class Student(Teacher):

    def study(self):
        print(self.name, "is studying Python.")


student1 = Student("Anu")

student1.introduce()
student1.study()

#chall
class Person:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello! My name is", self.name)


class Teacher(Person):

    def teach(self):
        print(self.name, "is teaching Python.")


teacher1 = Teacher("Anu")

teacher1.introduce()
teacher1.teach()









#The Magic of super()

class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

    def details(self):
        print("Name :", self.name)
        print("Roll No :", self.roll_no)


student1 = Student("Radhika", 101)

student1.details()
