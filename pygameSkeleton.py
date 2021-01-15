import pygame

pygame.init()

width = 900
height = 700
screenDimension = (width, height)

#create the pygame display

#screen = pygame.display.set_mode((width,height))
#call pygame then get inside using . , then call display class, and function set_mode

#screen = pygame.display.set_mode(screenDimension)
#finished = False #variable to tell us when the game is over. False because game just started.

#while finished != True:
    #processing all the events
    #for event in pygame.event.get(): #event1,event2,... #you dont want build up of event in your memory
        #event will happen, processed, and memory is freed up.
        #do appropriate things with events
        
    #pygame.display.flip() #Update method/load next frame
    
#pygame, there is a series of events, list of things that happen inside of the computer and pygame
#tracks of everything that is happening.

#IF STATEMENTS - allow us to check for certain conditions

#Syntax form
#if condition:
    #doAppropriateAction
#if differentCondition:
    #doMoreStuff
#These two are not related, but you can make them dependent by using elif, shorthand for else if

#if condition:
#    doAppropriateThing
#elif differentThing:
#    doMoreThings
#elif conditionThree:
#    doEvenMoreStuff
#else: 
#    doThis

genVariable = 7
if genVariable == 7:
    print("This number is 7.")
elif type(genVariable) == type(int): #if you enter elif, you don't go into else case
    print("Type is integer.")
else:
    print("Nope!")

for number in range(10):
    print(number)
    if number%3 == 0: #is our number divisible by three
        print("Divisible by 3")
    elif number%2 == 0:
        print("Divisible by 2")
    else:
        print("This number is not divisible by 2 or 3.") #when an if statement is satisfied, it will not check other conditions...

#you can use 'in' and 'not in' to create Boolean conditions.

greeting = "Hello, World!"
checkWord = "Hello"
checkLess = "Goodbye"
if checkWord in greeting:
    print("This is a greeting.")
else:
    print("Probably not a greeting.")

if checkLess not in greeting:
    print("This is probably anything but a goodbye.")

#exercise
word = "First"
if word == "First":
    print("Word is First!")
elif word == "Second":
    print("Word is Second!")
    print("Neither if checked worked, moving on to else")
else:
    print("Reached the else case")