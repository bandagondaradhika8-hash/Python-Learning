#####    D A Y 4     L O O P S   ############

            # P A R T 1 #


#  A while loop is used when you don't know in advance how many times the loop should run.
# 
i = 3
while i <= 5:
    print(i)
    i = i + 1
    # now to print 1 to 5
i = 1
while i <= 5:
    print(i)
    i = i + 1
########## to print 10 to 1
i = 10
while i >= 1:
    print(i)
    i = i - 1
############## to print even numbers using while ######
i = 2
while i <= 8:
    print(i)
    i = i + 2
########### to print odd numbers from 1 to 9 #######
i = 1
while i <= 9:
    print(i)
    i = i + 2
##########bonus challenge ###
i = 5

while i >= 1:
    print(i)
    i = i - 2

##### to print even numbers reverse from 10 to 2 ####
i = 10
while i >= 2:
    print(i)
    i = i - 2



###############
i = 2

while i <= 6:
    print(i * 2)
    i = i + 2







#  P A R T 2  BREAK,CONTINUE & PASS #

####### B R E A K #######"Stop the loop immediately!"#emergency exit
i = 1

while True:
    print(i)

    if i == 5:
        break

    i = i + 1
    ###############
i = 1

while True:
    print(i)

    if i == 3:
        break

    i = i + 1
    ###############

i = 10

while i >= 1:
    print(i)

    if i == 6:
        break

    i = i - 1
    
#####C O N T I N U E ######Skip only this iteration and continue with the next one. ⏭️
for i in range(1, 6):

    if i == 3:
        continue

    print(i)
####
for i in range(1, 6):

    if i == 4:
        continue

    print(i)
#########
i = 1

while i <= 5:

    if i == 3:
        i = i + 1
        continue

    print(i)
    i = i + 1
########   p a s s Nothing. 😄Yes, literally nothing.It's like telling Python:I'm not writing this part now. Just ignore it."
for i in range(1, 6):
    if i == 3:
        pass
    print(i)
##
for i in range(1, 4):
    if i == 2:
        pass
    print(i)






########### N E S T E D L O O P S :One loop inside another loop.
for i in range(2):

    for j in range(3):

        print("*")
##
for i in range(4):

    for j in range(2):

        print("Hi")

#####
for i in range(3):
    print("Outer")

    for j in range(2):
        print("Inner")
########
for i in range(2):
    print("❤️")

    for j in range(3):
        print("🐍")





########### P A R T 4 PATTERN PRINTING ######
for i in range(2):
    for j in range(3):
        print("#", end=" ")
    print()

#
for i in range(5):
    for j in range(2):
        print("*", end=" ")
    print()
###33
for i in range(3):
    for j in range(i + 1):
        print("*", end=" ")
    print()

## 
for i in range(4):
    for j in range(i + 1 ):
        print("*", end="")
    print()
#####above codes op should be reverse then this is the code 
for i in range(4):
    for j in range(4 - i ):
        print("*", end="")
    print()

#
for i in range(4):

    for j in range(4 - i - 1):
        print(" ", end="")

    for j in range(i + 1):
        print("*", end="")

    print()
#########
for i in range(4):

    for j in range(2 * i + 1):
        print("*", end="")

    print()


