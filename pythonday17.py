#    Day 17 – Method Overriding


#Method overriding in Python occurs when a child class 
# (subclass) defines a method with the exact same name and signature as a method in its parent class (superclass)

#Animal
#│
#├── Dog → Barks 🐶
#├── Cat → Meows 🐱
#└── Cow → Moos 🐄


#
class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


dog1 = Dog()

dog1.sound()



#
class Bird:

    def fly(self):
        print("Bird is flying")


class Eagle(Bird):

    def fly(self):
        print("Eagle flies very high")


bird1 = Eagle()

bird1.fly()


#
class Animal:
    def sound(self):
        print("Animal")

class Dog(Animal):
    def sound(self):
        print("Dog")

dog = Dog()
dog.sound()









# p O L Y M O R P H I S M : one method many forms


class Dog:

    def sound(self):
        print("Dog says Woof!")


class Cat:

    def sound(self):
        print("Cat says Meow!")


class Cow:

    def sound(self):
        print("Cow says Moo!")
animals = [Dog(), Cat(), Cow()]     #

for animal in animals:
    animal.sound()


#chall
#
class Mobile:

    def device(self):
        print("Using Mobile!")

class Laptop:

    def device(self):
        print("Using Laptop!")

devices = [Mobile(), Laptop()]

for device in devices:
    device.device()







# Encapsulation  : Protecting data from direct access.

class BankAccount:

    def __init__(self):
        self.__balance = 5000

    def show_balance(self):
        print("Balance: ₹", self.__balance)


account = BankAccount()

account.show_balance()






#ex
class Bike:

    def move(self):
        print("Bike is running")


class Car:

    def move(self):
        print("Car is driving")


class Plane:

    def move(self):
        print("Plane is flying")


vehicles = [Bike(), Car(), Plane()]

for vehicle in vehicles:
    vehicle.move()