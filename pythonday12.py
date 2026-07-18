# Part 1 – return Revision

def add(a, b):
    return a + b

answer = add(10, 20)

print(answer)
#
def square(x):
    return x * x

print(square(5))

#
def multiply(a, b):
    return a * b

result = multiply(4, 5)

print(result + 10)

#
def add(a,b):
    return a+b

print(add(5,5))
#


def square(x):
    return x*x

num = square(4)

print(num)








# Part 2: Even or Odd Function

def even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_odd(8)
even_odd(5)

#




#
def check_number(number):
    if number > 0:
        print("Positive")
    elif number == 0:
        print("Zero")
    else:
        print("Negative")

check_number(15)
check_number(0)
check_number(-8)




#
def vote_check(number):
    if number > 18:
        print("Eligible to Vote")
    else:
        print("not eligible")
vote_check(16)
vote_check(24)



#
def grade_check(mark):
    if mark >= 90:
        print("grade A")
    elif mark >= 75:
        print("grade B")
    elif mark >= 50:
        print("grade c")
    else:
        print("fail")
grade_check(99)
grade_check(0)




#🏦 ATM Balance Checker
def check_balance(balance):
    if balance >= 1000:
        print("You can withdraw money")
    else:
        print("Insufficient Balance")
check_balance(0)


#Password Checker

def check_password(password):
    if password == "python123":
        print("Access Granted")
    else:
        print("Wrong Password")
check_password("python123")

#
def check_password(password):
    if password == ("python123"):
        print("access granted")
    else:
        print("wrong password")
check_password("python")




#
def login(username, password):
    if username == "Radhika" and password == "python123":
        print("Login Successful")
login("Radhika", "python123")