#           D A Y 7   S T R I N G S 


#    we use string in aiml, webdevelopment,apps,datascience,interviews



#       P A R T 1 STRINGS
# A string is a simple text 
name = "Radhika"
city = "Hyderabad"   'hyderabad'  #it is also a string
country = "India" #    all these are strings
print(name)

# 123 it is not a string 





#     Part 2: String Indexing

word = "Python"
print(word[0])  # here we will get the letter of the index valued letter
print(word[-1])

#
name = "radhika"
print(name[-3])
print(name)
print(name[0])






  #          Part 3: String Slicing

  #    word[start:end]


  # here  it will give the op as we need # to ## uses ration form 2:5 like this 2:5 are index values


word = "Python"

print(word[0:3]) # here it will op as pyt bcz we have index value 0 to 3 is pyt
print(word[3:6])


#
name = "RADHIKA"
print(name[0:7])
print(name[1:7])
print(name[2:7])
print(name[3:7])
print(name[4:7])
print(name[5:7])
print(name[6:7])
print(name[7:7])
print(name[5:9])

#
word = "Python"
print(word[3:6])
print(word[0:1])
print(word[2:4])
print(word[1:5])
print(word[:3])  # if we wont give start also it will take it from the index 0
print(word[2:]) # similarly if we dont give end index it gives op till end








#           Part 4: String Slicing Shortcuts

#shortcut 1     Start from the beginning
word = "Python"

print(word[:3])



#shortcut2   Go till the end
word = "radhika"
print(word[3:])




#shrotcut 3    Copy the whole string
name = "chinnari"
print(word[:])



#shortcut 4 ## negative slicing 
name = "bandagonda"
print(name[-2:])

#ex
word = "Elephant"
print(word[:4])
print(word[3:])
print(word[-2:])






##         Part 5   (String Methods)

#     upper()
 #    lower()
 #    replace()
#     find()
#     count()

# Method 1: upper()
#  
#It converts all letters to CAPITAL letters

name = "Radhika"
print(name.upper())

# Method 2: lower()
#It converts all letters to small letters.
name = "RADHIKA"
print(name.lower())


#Method 3: capitalize()
#It makes only the first letter capital.
name = "radhika"
print(name.capitalize())


# Method 4 : Replace()
#It replaces one word/letter with another.

word = "Python"
print(word.replace("P", "J"))
#
text = "I love Python"
print(text.replace("Python", "Java"))


# Method 5 : count()
#It counts how many times something appears.
word = "banana"
print(word.count("a"))
#
word = "Mississippi"
print(word.count("s"))

word = "banana"
print(word.replace("a", "o"))


# Method 6 : find()
#It tells you the index of the first occurrence of a character or word.

word = "Python"
print(word.find("t"))
#
word = "elephant"
print(word.find("p"))
print(word.find("z"))
print(word.find("a"))
