#       Day 14 – Exception Handling

#try and except
try:
    num = int(input("Enter a number: "))
    print(num + 10)

except:
    print("Please enter numbers only.")

#
try:
    age = int(input("Enter your age: "))
    print("Next year you will be", age + 1)

except:
    print("Please enter a valid number.")






#else
try:
    num = int(input("Enter a number: "))
    print(num)

except:
    print("Invalid Input")

else:
    print("Everything went successfully!")



#
try:
    marks = int(input("Enter your marks: "))
    print("Marks:", marks)

except:
    print("Please enter only numbers.")

else:
    print("Marks entered successfully!")







#finally
try:
    num = int(input("Enter a number: "))
    print(num)

except:
    print("Invalid Input")

else:
    print("Everything went well!")

finally:
    print("Program Finished.")



#
try:
    age = int(input("Enter your age: "))
    print("Age:", age)

except:
    print("Invalid age!")

else:
    print("Age accepted!")

finally:
    print("Thank you for using the program.")






#
try:
    num = int(input("Enter Number: "))
    print(100 / num)

except:
    print("Error!")

else:
    print("Division Successful!")

finally:
    print("Program Ended!")










#except
try:
    num = int(input("Enter a number: "))
    print(100 / num)

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

finally:
    print("Program Finished.")








# Project: Student Marks Validator

try:
    marks = int(input("Enter your marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks should be between 0 and 100.")

    if marks >= 90:
        print("Grade A")

    elif marks >= 75:
        print("Grade B")

    elif marks >= 50:
        print("Grade C")

    else:
        print("Fail")

except ValueError as e:
    print("Error:", e)

finally:
    print("Program Ended.")
