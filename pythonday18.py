# D A Y 18 SETS 
#Topic 1: Sets

#A set is a collection of values where duplicate values are automatically removed.

#Example:
numbers = {10, 20, 30, 40}

print(numbers)

#
numbers = {10, 20, 20, 30, 30, 40}

print(numbers)



#Topic 2: add()

#We can add a new value to a set using .add().
fruits = {"Apple", "Banana", "Mango"}

fruits.add("Orange")

print(fruits)

#
friends = {"Anu", "Priya", "Ravi"}

friends.add("Rahul")

print(friends)



#Topic 3: remove()

#remove() deletes a specific value from a set.
fruits = {"Apple", "Banana", "Mango", "Orange"}

fruits.remove("Banana")

print(fruits)




#Topic 4: discard()

#discard() also removes a value.
fruits = {"Apple", "Banana", "Mango"}

fruits.discard("Banana")

print(fruits)


#
numbers = {10, 20, 30, 40}

numbers.remove(20)
numbers.discard(50)

print(numbers)






#union()

#Now we're getting into the really useful part of sets.

#union() combines two sets and removes duplicates.

set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.union(set2)

print(result)


#ex
friends1 = {"Anu", "Priya", "Ravi"}
friends2 = {"Ravi", "Rahul", "Kiran"}

all_friends = friends1.union(friends2)

print(all_friends)






#intersection()

#This one is super easy.

#intersection() finds the values that are common in both sets.

#Example:
set1 = {"Anu", "Ravi", "Priya"}
set2 = {"Ravi", "Rahul", "Priya"}

common = set1.intersection(set2)

print(common)


#
class1 = {"Python", "Java", "HTML", "CSS"}
class2 = {"Python", "Java", "SQL", "C"}

common = class1.intersection(class2)

print(common)








#difference()

#This tells us what is in the first set but NOT in the second set.

set1 = {"Python", "Java", "HTML"}
set2 = {"Python", "Java", "SQL"}

result = set1.difference(set2)

print(result)


#
girls = {"Anu", "Priya", "Keerthi", "Radhika"}
boys = {"Ravi", "Rahul", "Anu"}

result = girls.difference(boys)

print(result)






#
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))