#we already downloaded a module/library in pygame

#Standard Libraries
#syntax to import modules = import moduleName

#import random
#import random as r #if your module names get very long, you can rename them by using: import random as r
#now you can go into random library by using r.Method

#the dot lets us go into the library/module random; the second random calls the random method inside the first random library
#print(random.randint(0,10)) #a<=N<=b

#print(random.random())

#print(r.randint(0,10))

#if you dont want to import entire module
#from moduleName import methodName1, methodName2,...

from random import randint, random

print(randint(0,10))
print(random())
