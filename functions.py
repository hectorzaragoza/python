#functions allow us to put something into it, does something to it, and gives a different output.
#We start with def to define the function, then we name it, VarName()

#def function(input1, input2, input3,...):
#   code 
#   more code
#   return value
#result = functionName(In1, In2, In3,...)
#result = value

def addOne(x): #this line of code simply gives your function a name and inside the parenthesis, the inputs
    y = x + 1 #this line of code determines the actual function/manipulation/calculation that you are trying to do.
    #Line 12 cont. i.e. what you want to do to your inputs and assign that to a new variable which will then be returned
    return y #this line of code returns the output of your function

def addTogether(in1, testin2):
    inter = in1 + testin2
    return inter

testValue = 2 #this is going to be the variable we put into our addOne function, whose result is assigned in result
result = addOne(testValue) #y = testValue + 1 -> 2+1 -> 3
print(result)

secondTwo = addTogether(testValue, result) #secondTwo is a variable that will store the result of inputting testValue
#and result into the addTogether function defined in line 16.
print(secondTwo)

print(addTogether("Hello"," World!"))

print(addTogether("Hello",str(1)))

#exercise
#Write a function that takes two inputs and returns their sum



def SumFunction(VarOne, Vartwo):
    varthree = VarOne + Vartwo
    return varthree

open = 1
close = 2

EndProduct = SumFunction(open, close)

print(EndProduct)

#Write a function that takes an input and checks how many times the input is divisible by 3 and by 5. It then returns
#those two values

def aFunction(InputA):
    DivByThree = int(InputA/3) #You can have multiple things done to an input within a single function and return 
    #multiple results for tall those things as in this example.
    DivByFive = int(InputA/5)
    return DivByThree, DivByFive

Divisible = aFunction(489)

print(Divisible)

print(163*3, 97*5) #testing result

