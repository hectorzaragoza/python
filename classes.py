#Classes are similar to functions using class instead of def

#class Name:
#    properties
#    attributes


#General form of an animal, working down to something more specific.
#creating a kind of template, with properties that every animal has...
class Animal:
    """A General Animal Template""" #documentation you can add with triple quotation 
    #standard starting values
    def __init__(self,species,animalType): #creating a function inside of a class. Double underscore before and after, it's something we can override
#init is just initialization
#self needs to be the first variable to be declared to be able to reference animal class
        self.species = species #self. assigns species as a variable of the class animal.
        self.type = animalType #daytime animal or nighttime animal.
    def setSpecies(self,species):
        self.species = species

    #getters
    def getType(self):
        return self.type
#we have the template now so now we have to call it.

#Class Inheritance - creating a class that inherits attributes/properties from another class.
#Template
#class Name(parentClassName,parentTwoName):

class Pet(Animal): #we want our pet class to inherit all the traits of the animal class, since we want our pet to have a species, a type, etc. plus whatever we add to it.
    def __init__(self, species, animalType, name, sound):
        Animal.__init__(self,species,animalType) #we need to initialize the animal because the pet IS an animal.
        self.name = name
        self.sound = sound
#def anotherMethod(self):
#   code
    def __str__(self):
        return "My name is: "+self.name

    #define setter
    def setSound(self, sound):
        self.sound = sound

    def getSound(self):
        return self.sound 

    def pet(self):
        print(self.name, "goes", self.sound)



testAnimal = Animal("Reptile","Nighttime") #creating an instance of this class.
#testAnimalTwo = Animal("Amphibian","Daytime") #these values are returned to corresponding variables in def function, species and animaltype
testPet = Pet("Mammal", "Day Time", "Messi", "Woof")
print(testAnimal.species)
#print(testAnimalTwo.species)
print(testAnimal.type)
#print(testAnimalTwo.type)
print(testPet.species)
print(testPet.getType())
print(testPet.name)
print(testPet.setSound("Wahooo!!"))
print(testPet.getSound())
print(testPet.sound)
print(testPet.pet())
print(testPet) #this used to print out the object location e.g. "<__main__.Animal object at 0x105572198>" but because of the new function
#we created in the the Pet Class, we defined an already existing function named str but the __ __ allows us to overwrite it. So now, the print(testPet)
#returns what we 
testPet.pet()

testAnimal.species = "Reptile"
#testAnimalTwo.setSpecies("Amphibian")
#same as testAnimalTwo.species = "Amphibian"

print(testAnimal.species)
#print(testAnimalTwo.species)
print(testAnimal.type)
#print(testAnimalTwo.getType())
#when you first initialize a class, all instances will have the variables associated with the class available
#even though these values for these properties can change for each.

#in a funciton, you need to declare global VarName in order to call it globally rather than only locally within the function.
# so, self. allows us to do that as well. 
#print() #prints a space
#print(testAnimal.__doc__) #this will get you the documentation or help material written for that part of code
#print()
#print(testAnimalTwo.__doc__)

