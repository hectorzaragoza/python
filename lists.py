#data structures, tuple.
#we can't go into tuples as an array to change values, so we can make lists.

#name = [element,el2,el3,el4] #elements are separated by commas and ends with no comma
#lists will be a common way to store things

nameList = ["Hector", "Julia", "Kitty"]
print(nameList) #square parentheses tells you its a list, lists are ordered. So are tuples.

#nameList = nameList + ["Jo"]#this will overwrite nameList list to add Jo as part of the new list with 4 elements
#instead of doing line 10, you can shorthand it
nameList += ["Jo"]
print(nameList)

#to access element, use array syntax [0] first element and so on.

print(nameList[0]) #-1 would be the last element, -2 would be penultamite

print(nameList[1:3])
print(nameList[:])#shows everything
print(nameList[1:]) #shows all starting at 2nd element
print(nameList[::2])#goes through entire list, starts at 0 and goes in step of 2

print("Hector" in nameList) #if statement to check if value is in a list
print("Renato" in nameList)

for element in nameList:
    print(element)

print(len(nameList)) #checks number of elements in list

for index in range(len(nameList)):
    print(index, nameList[index]) #comma in print statement acts as a separator 

nameList.append("Bombastic") #appending adds value to back of list.
print(nameList)
