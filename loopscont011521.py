#how can we manipulate our loop control flow
#lets create an infinite loop

#startVariable = 0
#while True:
#    startVariable += 1
#    if startVariable>10:
#        break #breaks out of the most inner loop, in this case its the while loop. If While Loop B is insied While
# Loop A, the break would break out of While Loop B.
#    print("after if")

#If we want to nest loops

#while startVariable < 20:
#    while True:
#        startVariable += 1
        #print(startVariable)
#        if startVariable > 10:
#            break
        #print("after if")

#testLists = [1,5,7]

#for element in testLists:
#    if element == 5:
#        continue #this causes our loop to continue past 5 when if statement is True.
    #print(element)

#Exercises
#for i in range(5):
#    if i == 3:
#        continue
    #print(i)

x = 0
while x < 4:
    x += 1
    print(x)
    