#dictionary structure - one element is known as a key value pair, a key and its corresponding value
#a key and a value are together known as an item
#varName = {key:value1,key2:value2,key3:value3} #key names need to be distinct, values dont need to be.

schoolDistricts = {"district1":"High School","district2":"middle School","district3":"high school"}
print(schoolDistricts)
#print(schoolDistricts[0]) #doesn't work because they are unordered unlike a list, so you cant access them like arrays.

#access elements in dictionaries by using the key, to display the value
print(schoolDistricts["district1"]) 

schoolDistricts["district5"] = "test" #you cant append because there is no order so just add new key (variable) and assign it its value
print(schoolDistricts)

print(schoolDistricts.keys()) #displays the keys

for key in schoolDistricts:
    print(key,schoolDistricts[key])

#why use a dictionary? your go to will usually be lists but you'll know when to use tuple or dicitonary or list

listofTranslations = ["Hello","Goodbye"]
listofgerman = {"wie gehts" :"Hello","tschuss":"Goodbye"}



