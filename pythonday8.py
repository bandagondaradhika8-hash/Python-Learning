 #             D A Y 8 

#      P A R T 1  T U P L E S        List → []
#                                      Tuple → ()

# A tuple is a collection of items, just like a list.
# a tuple is immutable cant change and list is oppo
# Creating a tuple

fruits = ("Apple", "Banana", "Mango")

print(fruits)


3
# List can be changed

numbers_list = [10, 20, 30]
numbers_list[0] = 100

print(numbers_list)

# Tuple cannot be changed

numbers_tuple = (10, 20, 30)

# numbers_tuple[0] = 100   # This will give an error

print(numbers_tuple)











# P A R T 2 tuple indexing
fruits = ("Apple", "Banana", "Mango")

print(fruits[0])

# 
animals = ("cat","dog","monk")
print(animals[2])

# NEGATIVE INDEXING 
fruits = ("Apple", "Banana", "Mango")

print(fruits[-1])
#
animals = ("cat","dog","monk")
print(animals[-2])
#
marks = (85, 90, 95, 100)
print(marks[1])
print(marks[-1])
colors = ("Red", "Green", "Blue")






#Part 3: Tuple Slicing
#tuple slicing is also the same as list and string slicing!
fruits = ("Apple", "Banana", "Mango", "Orange")

print(fruits[1:3])

# NEGATIVE SLICING
languages = ("python","java","ml","sql")
print(languages[1:-2])



# P A R T 4   TUPLE METHODS

#count()
# index()

#method1 count()
numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))

fruits = ("Apple", "Banana", "Apple", "Mango")

print(fruits.count("Apple"))

#method2 index()
fruits = ("Apple", "Banana", "Mango", "Orange")

print(fruits.index("Mango"))

numbers = (5, 10, 15, 10)

print(numbers.index(10))

animals = ("Cat", "Dog", "Lion")

print(animals.count("Tiger"))








#    Part 5: List 🆚 Tuple


#Difference 1: Brackets
#list
fruits = ["Apple", "Banana", "Mango"] # used []
print(fruits)   

#tuple
fruits = ("Apple", "Banana", "Mango") #used ()
print(fruits)




#  Difference 2: Can we change it?

#list
numbers = [10, 20, 30]

numbers[0] = 100

print(numbers)


#tuple
#it cant change it will give us an error







#  Difference 3: Methods

# list has many methods like #

#  append()
# insert()
# remove()
# pop()
# clear()


# tuple has only two methods #

# 1.count()
# 2.index()



#Difference 4: When do we use them?


#Use a List when:

#You need to add items.
#You need to remove items.
#Data changes often.
shopping = ["Rice", "Milk"]
shopping.append("Eggs")
print(shopping)


#tuple
#Use a Tuple when:
#The data should never change.
days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)
print(days)