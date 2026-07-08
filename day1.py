########################day1 PART 1######################
#calling functions
def greet():
    print("hello radhika")

greet()
#add
def add(a,b):
    print(a+b)

add (10,20)
add (3,6)
#square
def square(num):
    print(num * num)
square(9)
square(24)
#even or odd
def even_odd (num):
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num,"is odd")
even_odd(99)
even_odd(33)
even_odd(53)
even_odd(22)

#largest of 2 digits
def largest(num1,num2):
    if num1 > num2 :
        print(num1,"is largest")
    else:
        print(num2,"is smallest")
largest(22,2)
largest(99,0)
largest(6,66)
#largest & smallest
def largest_smallest(num1,num2):
    if num1 > num2:
        print(num1,"is largest")
        print(num2,"is smallest")
    elif num2 > num1 :
        print(num2,"is largest")
        print(num1,"is smallest")
    else:
        print("both the numbers are same")
largest_smallest(67,68)
largest_smallest(99,100)
largest_smallest(100,100)


########################loops PART 2 ############################
for i in range (10,0,-1):
    print(i)
for i in range(2,21,2):
    print(i)
for i in range (1,6):
    print("*" * i)
for i in range (5,0,-1):
    print("*" *i)
for i in range (1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
for i in range (-1,5):
    print("*" *i)
for i in range (1,6):
    print(" " * (5 - i) + "*" * i)
for i in range (65, 70):
    for j in range(65, i + 1):
        print(chr(j), end="")
    print()
print(ord("A"))
print(ord("a"))
print(ord("0"))
print(ord(" "))
for i in range(1, 6):
    for j in range(5, 5 - i, -1):
        print(j, end="")
    print()
for i in range(10, 0, -2):
    print(i, end=" ")
 


    
