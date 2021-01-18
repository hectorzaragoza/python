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

#cleaned up lines 24-29
#y = 1
#x = 5
#for i in range(1,4):
#    z = i - y
#    print(" "*z + "O"*x)
#    x -= 2   

#Exercise 3
#Turn the program in exercise 2 into a function that takes the height of the pyramid as an input variable, and also the character
#to be used in the pyramid as another input value

#numberofLines = 3
#numberOfOs = 1
#for i in range(1,4):
#    whiteSpace = numberOfLines - i
#    print(" "*whiteSpace+"O"*numberOfOs+" "*whiteSpace)
#    numberOfOs += 2

#Skeleton of a function
#def VarName():
    #code
    #MoreCode

def createPyramid(numberOfLines,character):
    #numberofLines = 3
    numberOfChars = 1
    for i in range(1,numberOfLines + 1):
        whiteSpace = numberOfLines - i
        print(" "*whiteSpace+
            character*numberOfChars+
            " "*whiteSpace)
        numberOfChars += 2

createPyramid(4,str(4))

#Exercise 4 - Creating a file output of Ex. 3
#def createPyramid(numberOfLines,character,outName,Outlocation):
    #numberofLines = 3

#    out = open(outName,"w") #using this method, you have to remember to close the file. So, use with open()
    
#    numberOfChars = 1
    #creating a blank file
    #so that we can do with open in append mode later
    #out = open(outLocation+outName,"w")
    #out.close()

#   with open(Outlocation+outName,"w") as out:
#        pass #this just tells the program that we don't do anything here.

#    for i in range(1,numberOfLines + 1):
#        whiteSpace = numberOfLines - i
#        output = (" "*whiteSpace+
#            character*numberOfChars+
#            " "*whiteSpace)
#        
#        print(output)
#        with open(Outlocation+outName,"a") as out:
#            out.write(output)
#            out.write("\n")
#        numberOfChars += 2

#    out.close()

#createPyramid(30,"L","Output.txt","/Users\zarag\Desktop\helloworld\\") #location always ends with \\in windows or / in mac or linux 
#you have to make sure the folder you want to store file in exists.


#Exercise 5
