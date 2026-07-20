#  Day 13  File Handling

#Topic 1: Creating and Writing a File
file = open("notes.txt", "w")

file.write("Hello Radhika!")

file.close()



#(Day 13 - Part 2)Part 2: Reading a File
file = open("notes.txt", "r")

content = file.read()

print(content)

file.close()
#
file = open("notes.txt", "r")

content = file.read()

print(content)

file.close()


#
# -------------------------------
# Day 13 - File Handling
# -------------------------------

# Step 1: Create a file and write data into it
file = open("notes.txt", "w")

file.write("My name is Radhika.\n")
file.write("I am learning Python.\n")
file.write("Today is Day 13 - File Handling.")

file.close()

print("File written successfully!\n")

# Step 2: Open the same file in read mode
file = open("notes.txt", "r")

content = file.read()

print("File Content:")
print(content)

file.close()




#Part 2: Append Mode ("a")

file = open("notes.txt", "a")

file.write("\nI love Python.")

file.close()

#
file = open("notes.txt", "a")

file.write("\nI will become an AI Engineer.")

file.close()

file = open("notes.txt", "r")

print(file.read())

file.close()


###############
#Program 1 - Write Mode ("w")

file = open("student.txt", "w")  
                                 
file.write("My name is Radhika.")

file.close()

print("File Created Successfully!")







#Program 2 - Read Mode ("r")

file = open("student.txt", "r")

content = file.read()

print(content)

file.close()






#Program 3 - Append Mode ("a")

file = open("student.txt", "a")

file.write("\nI am learning Python.")

file.close()

print("New text added successfully!")




#Program 4 - Read Again

file = open("student.txt", "r")

print(file.read())

file.close()






#Program 5 - readline()

file = open("student.txt", "r")

print(file.readline())

file.close()






#Program 6 - Multiple readline()
file = open("student.txt", "r")

print(file.readline())
print(file.readline())

file.close()







#Program 7 - readlines()

file = open("student.txt", "r")

content = file.readlines()

print(content)

file.close()






#Program 8 - Professional Method (with open())
with open("student.txt", "r") as file:
    print(file.read())





#
file = open("college.txt", "w")

file.write("Name : Radhika\n")
file.write("Branch : AIML\n")
file.write("Year : 3rd B.Tech")

file.close()

print("College file created successfully!")
#######continuation
file = open("college.txt", "r")

content = file.read()

print(content)

file.close()










#
# Create and Write
file = open("friends.txt", "w")

file.write("Friend1 : Anu\n")
file.write("Friend2 : Ravi\n")
file.write("Friend3 : Priya")

file.close()

print("Friends file created successfully!")

# Read the whole file
file = open("friends.txt", "r")

content = file.read()

print(content)

file.close()

# Append a new friend
file = open("friends.txt", "a")

file.write("\nFriend4 : Rahul")

file.close()

# Read the updated file again
file = open("friends.txt", "r")

content = file.read()

print("\nUpdated File:")
print(content)

file.close()










#with open()
with open("friends.txt", "r") as file:
    print(file.read())
#readlines
with open("friends.txt", "r") as file:
    content = file.readlines()

print(content)
#
with open("friends.txt", "r") as file:
    print(file.read())
