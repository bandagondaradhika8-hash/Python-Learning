## Day 15: Modules & Packages 

#topic 1
#mymath.py

#topic 2
#main.py





#Next Topic 3: from ... import ...
from mymath import add, multiply

print(add(100, 200))
print(multiply(10, 10))



#
import mymath as mm

print(mm.add(40, 60))
print(mm.subtract(100, 25))
print(mm.multiply(8, 9))
print(mm.divide(81, 9))






#Topic 4: Built-in Modules (math)
#creating  a new file mathpractice.py



#Topic 5: random Module

#Example 1 random variable
import random

print(random.randint(1, 10))


#Example 2: Random Choice
import random

fruits = ["Apple", "Banana", "Mango", "Orange"]

print(random.choice(fruits))




####
import random

print("Rolling Dice...")

dice = random.randint(1, 6)

print("You got:", dice)







#####guessing num challenge

import random

secret_number = random.randint(1, 10)

guess = int(input("Guess a number (1-10): "))

if guess == secret_number:
    print("🎉 Congratulations! You guessed it correctly.")

else:
    print("❌ Wrong Guess!")
    print("The correct number was:", secret_number)









#Topic 6: More random Module Functions


#1random.choice()  
#  #it picks one random item from a list
import random

fruits = ["Apple", "Mango", "Orange", "Banana"]

fruit = random.choice(fruits)

print("Today's fruit is:", fruit)




#2 random.shuffle()
#It mixes the items in a list.

import random

cards = ["A", "K", "Q", "J"]

random.shuffle(cards)

print(cards)








#
import random

friends = ["Anu", "Ravi", "Priya", "Rahul"]

print(random.choice(friends))

#
import random

numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)

print(numbers)






#Mini Project: Lucky Winner Picker


import random

students = ["Radhika", "Anu", "Ravi", "Priya", "Rahul"]

winner = random.choice(students)

print("🎉 Lucky Winner is:", winner)






#Packages
# A package is simply a folder that contains multiple python modules

#calculator.py
def add(a, b):
    return a + b
#greetings.py
def hello(name):
    print("Hello", name)
#main.py
    from utilities.calculator import add
    from utilities.greetings import hello

print(add(20, 30))
hello("Radhika") 