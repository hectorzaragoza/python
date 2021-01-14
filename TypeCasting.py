#TypeCasting allows us to transform one variable type to another.

#String, Int, Float, Boolean
print(type(1))
print(type(1.0))
print(type("Hello"))
print(type(True))

#print("Hello" + 1.0) #This produces a Type Error because you can't concatenate or add a string to a float. So, Type Casting is helpful.

#Starting type --> (Different) ending type

#print("hello" + 1.0) #--> if we want "hello1.0" then we want a string not a float
print("hello" + str(1.0))

#we put the type of variable we wanted in front of the value we wanted to type cast as another type than its original
#str(1.0) --> "1.0"

print(float("1.3") + 4)
print(int("1") + 4)
print("1" + str(4)) #string version of 14
print(int(1.4) + 4) #results in 5, it's not rounding but cutting off the decimal and everything after that

print(bool("True") == True)
print(bool("True") == False)
print(bool("True") != True)

