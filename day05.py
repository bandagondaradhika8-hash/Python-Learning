######### D A Y 5 ### L I S T S ######


                # P A R T 1 #
#A list is a collection of multiple values stored in a single variable.

# creating a list 
fruits = ["Apple", "Banana", "Mango"]

print(fruits)

##### Accessing list elements   INDEXINGG

fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])   #index value is 0
print(fruits[1])
#########
animals = ["Dog", "Cat", "Lion", "Tiger", "Elephant"]
print(animals[4])


######## NEGATIVE INDEXING ########## starts from right side with -1
animals = ["Dog", "Cat", "Lion", "Tiger", "Elephant"]
print(animals[-1])
print(animals[-2])
print(animals[-5])


#### updating list elements ....we can change an item a list by using inder number
fruits = ["Apple", "Banana", "Mango"]

fruits[1] = "Orange"

print(fruits)
cities = ["Hyderabad", "Delhi", "Mumbai", "Chennai"]

cities[0] = "Bangalore"

print(cities)

#
numbers = [10, 20, 30]

numbers[1] = 99

print(numbers)



######### F U N C T I O N LEN() len() tells us how many elements are in a list. 

fruits = ["Apple", "Banana", "Mango", "Orange"]

print(len(fruits))

#
names = ["muddivan", "PAVAN", "Radhika", "cheddivan", "RADHA"]

print(len(names))
print(names[4])

#####
numbers = [5, 10, 15, 20]

print(len(numbers))
print(numbers[-1])
print(numbers[0])



                            # P A R T 2 # APPEND,INSERT,REMOVE,POP,DEL

#### append() Adds an element at the end of the list 

fruits = ["Apple", "Banana"]

fruits.append("Mango")

print(fruits)





####### insert() adds an element at a specific index.

fruits = ["Apple", "Banana", "Mango"]

fruits.insert(1, "Orange")

print(fruits)
#
colors = ["Red", "Green", "Blue"]

colors.insert(2, "Yellow")

print(colors)






########### remove()  removes an item by its value

fruits = ["Apple", "Banana", "Mango"]

fruits.remove("Banana")

print(fruits)

#
names = ["Anu", "Ravi", "Sai", "Ram"]

names.remove("Sai")

print(names)
#
numbers = [10, 20, 30]
numbers.remove(20)
print(numbers)

#
numbers = [5, 10, 15, 20]

numbers.remove(15)

print(len(numbers))
print(numbers[2])





##### pop() removes an element using its index.

fruits = ["Apple", "Banana", "Mango"]

fruits.pop(1)

print(fruits)
#

fruits = ["Apple", "Banana", "Mango"]

x = fruits.pop(1)

print(x)
print(fruits)

# pop without an indedx it removes the last element

numbers = [10, 20, 30, 40]

numbers.pop()

print(numbers)
#
numbers = [100, 200, 300, 400]

x = numbers.pop(2)

print(x)
print(numbers)
