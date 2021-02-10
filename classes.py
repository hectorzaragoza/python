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

testAnimal = Animal("Reptile","Nighttime") #creating an instance of this class.
testAnimalTwo = Animal("Amphibian","Daytime") #these values are returned to corresponding variables in def function, species and animaltype
print(testAnimal.species)
print(testAnimalTwo.species)
print(testAnimal.type)
print(testAnimalTwo.type)

testAnimal.species = "Reptile"
testAnimalTwo.setSpecies("Amphibian")
#same as testAnimalTwo.species = "Amphibian"

print(testAnimal.species)
print(testAnimalTwo.species)
print(testAnimal.type)
print(testAnimalTwo.getType())
#when you first initialize a class, all instances will have the variables associated with the class available
#even though these values for these properties can change for each.

#in a funciton, you need to declare global VarName in order to call it globally rather than only locally within the function.
# so, self. allows us to do that as well. 
print()
print(testAnimal.__doc__) #this will get you the documentation or help material written for that part of code
print(testAnimalTwo.__doc__)