f={0:1,2:3,4:7}
for i in f:
    print(i,end=" ")
    print(f[i])

##############################################################################################
#using keys of the library
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

##############################################################################################
# length of the library
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
}
print(len(thisdict))

##############################################################################################
#can input any dat type

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

##############################################################################################

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

##############################################################################################

#select a dat in the key model
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict.get("model"))

##############################################################################################
#get a list of keys
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

##############################################################################################
#get a list of values
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

##############################################################################################
#get a item list as dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
x = car.items()
print(x)

##############################################################################################
#check if a specific key present in the dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

##############################################################################################
#remove items in dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

##############################################################################################
#remove the last item in the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

##############################################################################################
#delete the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict

##############################################################################################
#clear all items in the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

##############################################################################################
#Nested libraries
child1 = {"name" : "Emil","year" : 2004}
child2 = {"name" : "Tobias","year" : 2007}
child3 = {"name" : "Linus","year" : 2011}
myfamily = {"child1" : child1,"child2" : child2,"child3" : child3}
print(myfamily)

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])