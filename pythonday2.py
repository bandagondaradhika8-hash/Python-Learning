#######DAY 2########### Day 2 - Input(), int(), Mini Calculator
# Date: 09-07-2026
###############################INPUT()########################
name = input("enter your name mam:")
print("hello",name)
##################numberrrrrrrrrrrrrr and typeeeeee#########
num = input("enter a number: ")
print(num)
print(type(num))
###########################int gives in number###########input gives in strings
a = int(input("enter your first number: "))
b = int(input("enter your second number: "))
print(a + b)
##############agee
age = int(input("Enter your age: "))
print("Your age is", age)
print(type(age))
########### sooooooooooooooo string + int ========== errrrrrrrrrorrrrrr
a = "10"
b = 20
################mini prooooooooject#########
num1 = int(input("enter your first number: "))
num2 = int(input("enter your second number: "))
addition = (num1 + num2)
subtraction = (num1 - num2)
multiplication = (num1 * num2)
division = (num1 / num2)
print("addition result:", addition)
print("subtraction result:", subtraction)
print("multiplication result:", multiplication)
print("division result:", division)
####################
print(str(50) + "10")




####################################### D A Y 2 PART 2 ###################if
#############    I F    #########
age = int(input("enter your age: "))
if age >= 18:
    print("you can vote.")

###############    I F  ......E L S E    ######################
if age >= 18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")


##############
##############  P O S I T I V E .......N E G A T I V E ########3
number = int(input("enter your number: "))
if number >0:
    print(" your number is positive")
else:
    print("number is negative: ")


    #############
    ################ e v e n o r o d d again#####
num = int(input("enter your number: "))
if num % 2 == 0:
        print(num, "is even")
else:
        print(num,"is odd")




################                        ###############
##################          e l i f         ###############
marks = int(input("enter your marks: "))
if marks >= 90:
     print("Grade A")
elif marks >= 75:
     print("Grage B")
elif marks >= 35:
     print("Grage C")
else:
     print("fail")

########  CHATGPT   C H A LL E N G E  #########
number = int(input("enter your number: "))
if number >= 0:
     print("number is positive")
elif number == 0:
     print("number is zero")
else:
     print("number is negative")


