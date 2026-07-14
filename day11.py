#  Day 11 – Writing Your Own Functions


#Part 1 – Writing our First Function

#1
def say_hello():
    print("Hello Radhika!")

say_hello()
#
def say_hello():
    print("hello radha")
say_hello()

#2
def welcome():
    print("Welcome to Python!")

welcome()
welcome()
#
def how_are_you():
    print("man")
how_are_you()
how_are_you()


#3
def stars():
    print("*****")

stars()
stars()
stars()
#
def stars():
    print(";;;;;")
stars()






#Part 2: Functions with Parameters

#1
def greet(name):
    print("Hello", name)

greet("Radhika")
greet("radha")

#2
def multiply(number):
    print(number * 2)

multiply(5)
multiply(8)

#3
def country(place):
    print("I live in", place)

country("India")
country("UK")

####
def double(num):
    print(num * 2)

double(6)

#
def square(x):
    print(x * x)

square(9)

#
def love_python(language):
    print("I Love", language)
love_python("python")
#
def square(x):
    print(x * x)
square(6)
#
def add(num):  #used one parameter
    print(num + 20)
add(10)

#
def add(a, b):   #used two parameters
    print(a + b)

add(10, 20)

#
def subtract(a,b):
    print(a - b)
subtract(50,20)

#
def divide(a,b):
    print(a/b)
divide(20,40)

#
def multiply(a,b,c):
    print(a * b * c)
multiply(99,101,2000)
