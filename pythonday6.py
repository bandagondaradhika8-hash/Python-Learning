#             D A Y 6          #

#         Part 1 - Looping Through a List


fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)


animals = ["Dog", "Cat", "Lion"]

for x in animals:
    print(x)




#Part 2                Looping using range(len(list))

fruits = ["Apple", "Banana", "Mango"]

for i in range(len(fruits)):
    print(i, fruits[i])

# use this when we need only the values
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:    # here we wont use any len and in print wont print
    print(fruit)






#Part 3:   in Operator  :::  The in operator checks whether an item exists in a lis

  ######## TRUE OR FALSE         IN OP


fruits = ["Apple", "Banana", "Mango"]

print("Banana" in fruits)  

#
fruits = ["Apple", "Banana", "Mango"]

print("Orange" in fruits) 




#   not in {not in is the opposite of in.}

#########   if the item is not present, it returns True.

fruits = ["Apple", "Banana", "Mango"]

print("Orange" not in fruits)
#
fruits = ["Apple", "Banana", "Mango"]

print("Banana" not in fruits)

#
fruits = ["Apple", "Banana"]

print("Apple" in fruits)
print("Apple" not in fruits)
print("Mango" in fruits)
print("Mango" not in fruits)








# Part 4  lists + loops + if conditions.


animals = ["Dog", "Cat", "Lion"]

for animal in animals:
    if animal == "Cat":
        print("Found Cat")

#
fruits = ["Apple", "Banana", "Banana", "Mango"]

for fruit in fruits:
    if fruit == "Banana":
        print("Found Banana")

#
numbers = [5, 10, 15, 20, 15]

for num in numbers:
    if num == 15:
        print(num)

#
numbers = [5, 10, 15, 20]

for num in numbers:
    if num > 10:
        print(num)


#
numbers = [5, 10, 15, 20]

for num in numbers:
    if num >= 10:
        print(num)


#
numbers = [2, 5, 8, 11, 14]

for num in numbers:
    if num % 2 == 0:
        print(num)






        # Part 5    B R E A K  
        #It immediately stops the loop.

fruits = ["Apple", "Banana", "Mango", "Orange"]

for fruit in fruits:
    if fruit == "Mango":
        print("Found Mango!")
        break

#
numbers = [2, 4, 6, 8]

for num in numbers:
    print(num)
    break

#
numbers = [3, 6, 9, 12]

for num in numbers:
    if num == 9:
        break
    print(num)

#
numbers = [2, 4, 6, 8]

for num in numbers:
    print(num)
    if num == 6:
        break

