#                Day 9 – Dictionaries


#  Part 1 – What is a Dictionary?

# A dictionary cannot have duplicate keys.

# A dictionary stores data in key : value pairs.

#The left side is called the key.

#The right side is called the value.


student = {
    "name": "Radhika",
    "age": 21,
    "branch": "AIML"
}

print(student)

#
car = {
    "brand": "Hyundai",
    "color": "White",
    "price": 800000
}

print(car)








#Part 2: Accessing Values

#dictionaries don't use index values

student = {
    "name": "Radhika",
    "age": 21,
    "branch": "AIML"
}

print(student["name"])
print(student["age"])
print(student["branch"])

#
car = {
    "brand": "Hyundai",
    "color": "White",
    "price": 800000
}

#
car = {
    "brand": "Hyundai",
    "color": "White",
    "price": 800000
}
#
car = {
    "brand": "Hyundai",
    "color": "White",
    "price": 800000
}

print(car["brand"])
print(car["color"])

#
book = {
    "title": "Python",
    "author": "Radhika",
    "pages": 250
}
print(book["title"])
print(book["author"])
print(book["pages"])










#    Part 3: Adding & Updating Dictionary Values

#Just like we added items to lists with append(), we can add or update items in a dictionary.


#adding
student = {
    "name": "Radhika",
    "age": 21
}

student["branch"] = "AIML"

print(student)

#
student = {
    "name": "Radhika",
    "age": 21
}
student["branch"] = "AIML"
student["age"] = 22



#updating
student = {
    "name": "Radhika",
    "age": 21
}

student["age"] = 22

print(student)

#dictionary keys must be unique 
#dictionary values can be repeated 
student = {
    "student1": "Radhika",
    "student2": "Radhika",
    "student3": "Anu"
}

print(student)








#Part 4: Dictionary Methods

#Unlike lists, dictionaries have different methods.

# keys()
# values()
# items()
# get()

#These are used everywhere in Python, Django, Flask, AI, and APIs.


# Method 1: keys()
#returns all the keys

student = {
    "name": "Radhika",
    "age": 21,
    "branch": "AIML"
}

print(student.keys())


#Method 2: values()
#Returns all the values.

student = {
    "name": "Radhika",
    "age": 21,
    "branch": "AIML"
}

print(student.values())


#Method 3: items()
#Returns both keys and values together.
student = {
    "name": "Radhika",
    "age": 21
}

print(student.items())




#Method 4: get()
#method is safer if the key might not exist
student = {
    "name": "Radhika",
    "age": 21
}

print(student.get("name"))





#pract
student = {
    "name": "Radhika",
    "age": 21
}
print(student["name"])
#
student = {
    "name": "Radhika",
    "age": 21
}
student["branch"] = "AIML"
print(student)

#
student = {
    "name": "Radhika",
    "age": 21,
    "branch": "AIML"
}

print(student.keys())

#
student = {
    "name": "Radhika"
}

print(student.get("marks"))

#
student = {
    "name": "Radhika",
    "age": 21
}

student["age"] = 22

print(student["age"])