#Write a program that, using loops, writes out a triangle of O’s, with the size of the bottom of
#the triangle being 5 O’s long.
#For example, this should look like the following:

#Exercise 1.1
#Letter = "O"

#while Letter != "OOOOOO":
#    print(Letter)
#    Letter += "O"
    
#Exercise 1.2
#Write a program that writes out a pyramid of O’s, with the height of the pyramid being 3 lines
#high.
#Make sure that the O is in the center of the pyramid, not on the left hand side like we did
#above for the triangle
#For example, this should look like the following:
#O
#OOO
#OOOOO
#Hint: You can shift the position of the O’s around by adding in spaces to the left and right of
#them.

#numberofLines=3
#numberofOs = 1
#for i in range(1,4):
#    whiteSpace = numberofLines - i
#    print(" "*whiteSpace+"O"*numberofOs)
#    numberofOs += 2

y = 1
x = 5
for i in range(1,4):
    z = i - y
    print(" "*z + "O"*x)
    x -= 2   
