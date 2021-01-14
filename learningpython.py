#print("Hello, World!")

#first Commit

#The first day of learning python consisted of learning about the print function, concatenating values using the + sign
# and doubling values using the * sign. STRING SLICING We also can print characters from a string using the syntax varvalue [Starting Value:Ending Value: Step Value]
#You can use negative values to go in reverse order.

#Review of Day 1
#print("Hello, Hector")

#FirstNameVariable = ("Hector")
#LastNameVariable = (" Zaragoza")

#ConcatStr = FirstNameVariable + LastNameVariable
#DoubleVarValue = FirstNameVariable * 2

#print(DoubleVarValue)

#print(ConcatStr)

#print(ConcatStr [7::2]) #start at character 7, print, go two steps, print, until end.

#exercise 1: 
#tooManySpaces =("Spaceman "[:8:])*2  
#tooManySpacesB =tooManySpaces[0:-1]
#print(tooManySpaces)

#Ints and Floats

#integerNumber = 1
#intNum2 = 2
#floatNumber = 1.2
#print(integerNumber)
#print(intNum2)
#print(integerNumber + intNum2 + floatNumber)

#you can check the type of an int using type
#print(type(5))
#print(type("Hello"))
#print(type(2.0))
#print(type(intNum2))

#Operations on INts and Floats

#print(1+2)
#varOne = 1
#varTwo = 2
#print(varOne+varTwo)
#theResults = 1 + 2
#print(theResults)

#multiply = (2*9)/3.5
#print(multiply)
#print(type(multiply))

#power is **

#PowerVar = 2**2
#print(PowerVar)

#Modulus Operator = the remainder of a division...there are cycles in modulus operators.
#you can use the following operators -,+,*,**,/,%
#ModulusOp = 4%4
#print(ModulusOp)

#ModTwo = 3%1.5
#print(ModTwo)
#ModThree = 5%1
#print(ModThree)

#manipulating strings via arithmetic: Multiplication but can't add a string, can't multiply by float...
#VarStr = ("Hello, World! ")
#print(VarStr*3)


#Booleans - True or False, 1 or 0. "True" is not True. The first is the word true while the latter is the boolean True.

trueBool = True
falseBool = False

print(trueBool)
print(falseBool)

print(type(trueBool))
print(type(falseBool))

#Boolean Operations
#Checking if equal by using ==, this checks for equivalnce while the single = is an assignment operator

print(trueBool == falseBool) #this is false because True is not == False
print(trueBool != falseBool) #this is true because they are not ==

TestOne = 2
TestTwo = 4
TestThree = 1
TestFour = 1.0

print(TestOne == TestTwo) #false
print(TestOne != TestTwo)/n #True
print(TestThree == TestFour)
print(type(TestThree) == type(TestFour))