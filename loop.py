#loops, help us do things repeatedly
#For loop, in this condition, do this.



#for newVariableName in somethingToLoopOver:
#    code
#    moreCode
#Not inside loop anymore
#    indentedCode will result in error if not inside a funciton.

#range(start,stop,step) -->start, start+step, start + n steps < stop (The stop is up to but not including.)
#for number in range(0,10,1): #range only takes ints, but you can divide by 10 if you wanted to get decimals.
#    print(number) #new line is automatically produced with each print()

#for latex in range(10): #assumes start of 0 and step 1
#    print(latex)

#for latexTwo in range(0,20,1):
#    print(latexTwo)

#While Loops
#While a certain condition is true, continue to loop, until the condition is false

#while condition/booleanExpression:
#    Code
#    moreCode 
#no longer inside the loop

counter = 0

while counter < 10: #our while loop will keep going until counter is 10
    print(counter)
    counter = counter + 1 #is the same as counter += 1

#start of with 0, reach loop and check condition of loop, so True, print 0, enter loop, add 1 and rerun loop.
print(counter) #this prints 10 because that is the last value of counter that made the previous loop false

text = ""

while text != "AAA":
    print(text)
    text += "A" #text = text + "A"
    #"" + "A" -> "A"
    #"A" + "A" -> "AA"
    #"AA" + "A" -> but loop does not print because it equals "AAA"

#Indentation plays a role in python, it is not just whitespace. Indentation
#is used by the Python Interpreter to form groupings when special cases are create.
#It dictates which block of code belongs into which grouping, as well as when that grouping stops through no 
#longer using the indentation.