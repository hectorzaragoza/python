import pygame

#pygame.init() #inside of library pygame, theres a function/method called init which makes it ready to go

#Tuples Let's us bundle two values in a data structure.

#tupleName = (element1,element2,element3,...)
#tupleIndex = (0       ,1      ,2       ,...)
#for variables, we usually only store one value, e.g. int = 10, intTwo = 2 but we can group it using a tuple
#intTuples = (10,2)
#length = len(varName)

#screenSizeTuple = (900,700) #(width, height)
#print(screenSizeTuple[0:2])
#print(screenSizeTuple[0])
#print(screenSizeTuple[1])
#print(len(screenSizeTuple))

#You can create a tuple with only one element but have to include the ,
#testTuple = ("screen size",) + screenSizeTuple
#print(testTuple) #you can know what your tuple represents by concatenating your tuple with a string descriptor in slot 1
#print(testTuple[0])
#print(len(testTuple))

#Operations on Tuples
#We can check to see what is inside in Tuples

#print("screen size" in testTuple) #This results in true because the string is included in the Tuple.

#Testing to see a tuple inside a tuple
Size = (800,600) 
TestTwo = ("Screen Size",) + (Size,)
print(TestTwo)

print(TestTwo[0])
print(TestTwo[1])

print(Size in TestTwo)
print(TestTwo[1][0]) #This should give us 800 #printing the first value of the size tuple withing the TestTwo var
print(TestTwo[1][1]) #600

print(TestTwo[1][0])
#is the same as
print(Size[0])

for var in TestTwo:
    print(var)







