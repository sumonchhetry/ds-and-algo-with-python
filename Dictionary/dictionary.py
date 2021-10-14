# Creating a dictionary
# myDict = dict()
# print(myDict)

# secDict = {}
# print(secDict)

# engToEsp = {"one":"uno", "two":"dos", "three":"tres"}
# print(engToEsp['three'])

# myDict = {'name': 'Sumon', 'age': 29}

# updating a value
# myDict['age'] = 30

# inserting/adding a value in dictionary
# myDict['height'] = 170
# print(myDict)

# Travese through a dictionary
# def traverseDict(dict):
#     for key in dict:
#         print(key, dict[key])
    
# traverseDict(myDict)

# Searching through a dictionary
# def searchDict(dict, value):
#     for key in dict:
#         if dict[key] == value:
#             return key, value
#     return "The value doesn's exist in the dict"

# print(searchDict(myDict, 29))

# Delete/remove an element from dictionary
# myDict = {'name': 'Sumon', 'age': 29, 'height': 170, 'profession': 'Developer', 'Address': 'Kolkata'}

# popitem() method
# print(myDict.popitem())
# print(myDict)

# clear() method
# myDict.clear()
# print(myDict)

# del() method
# del myDict['age']
# print(myDict)

# Dictionary method

# myDict = {'name': 'Sumon', 'age': 29, 'height': 170, 'profession': 'Developer', 'Address': 'Kolkata, India'}

# dict = myDict.copy()
# print(myDict)
# print(dict)

# To create a new dictionary with new keys and new values
# newDict = {}.fromkeys([1, 2, 3], 0)
# print(newDict)

# get() method to get a key which alreay exists in the dictionary or else the method will add it
# myDict.get('address')
# print(myDict)

# items() method
# myDict = {'name': 'Sumon', 'age': 29, 'height': 170, 'profession': 'Developer'}

# items help you to print items in pair
# print(myDict.items())

# keys() method helps us to get all the keys from any given dict
# print(myDict.keys())

# popitem() method remove the last item from the dict
# print(myDict.popitem())
# print(myDict)

# setDefault() method update the value of a key if it's present in the dict or it will add a new key and vaalue in the dict
# print(myDict.setdefault('name', 'Added'))
# print(myDict)

# print all the values in a given dictionary
# print(myDict.values())

# update() method add keys and values in an existing dict
# newDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# myDict.update(newDict)

# print(myDict)

# Dict methods
# myDict = {'name': 'Sumon', 'age': 29, 'height': 170, 'profession': 'Developer'}

# in operator check if the operator exist in the dict as keys or values
# print('Sumon' in myDict)

# when we use .values() in dict with in operator itchecks only for the values
# myDict = {1: True, 2: False}
# print(all(myDict))

myDict = {'One': 'Ak', 'Two': 'Dui', 'Three': 'Tin', 'Four': 'Char'}

print('one' in myDict)
