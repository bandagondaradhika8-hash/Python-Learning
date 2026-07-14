#        Day 10 – Functions


# P A R T 1
#A function is a block of code that performs a specific task.

#Instead of writing the same code many times, you write it once and call it whenever you need it.

def greet(): # DEFINING THE FUN HELLO
    print("Hello Radhika!")

greet()     #CALLING THE DEFINED FUN


#
def welcome():
    print("Welcome to Python!")

welcome()
welcome()
welcome()




# Part 2: Parameters

#parameter
#def greet(name): #name is called a parameter.

#To greet different types of people the parameter we use


def greet(name):  
    print("Hello", name)

greet("Radhika")
greet("Anu")
greet("Ravi")

#argument
#greet("Radhika") # radhika is an argument
def square(number):
    print(number * number)

square(5)
square(8)


#
def add(num):
    print(num + 10)

add(5)

#
def welcome(person):
    print("Welcome", person)

welcome("Anu")

#
def greet(name):     # ← Parameter
    print("Hello", name)

greet("Radhika")     # ← Argument

#
def multiply(number):
    print(number * 3)
multiply(4)
multiply(7)

#
def message(name):
    print("Good Morning", name)

message("Radhika")
message("Anu")







#Part 3: return

def add(a, b):
    return a + b

result = add(5, 3)

print(result)

#
def square(num):
    return num * num

print(square(4))

#
def add(a, b):
    return a + b

x = add(2, 5)

print(x)









# Part 4: Built-in vs User-defined Functions


#Built-in Functions

#These are functions that Python already gives us.

#We don't create them.

# example
#print()
#len()
#input()
#type()
#max()
#min()
#num()

numbers = [10, 20, 30]

print(len(numbers))






#User-defined Functions

#These are functions we create ourselves using def.

def greet():
    print("Hello Radhika!")

greet()



#
def add(a, b):
    return a + b

print(add(5, 4))