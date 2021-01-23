#global Variables

def addOne():
    global y,x #this will make the y variable a global variable
    y = x + 1 #y inside this function is a local variable
    return y #a variable inside a function is only defined for that function.

x = 3
test = addOne()
print(test)

print(y)#causes error because y is not defined globally, only locally within a function.