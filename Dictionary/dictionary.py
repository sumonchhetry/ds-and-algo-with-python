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

# myDict = {0: True, 1: False, 2: True, 3: True}
# print(all(myDict))
# print(any(myDict))

# len() method
# myDict = {'name': 'Sumon', 'age': 29, 'height': 170, 'profession': 'Developer'}
# print(len(myDict))

# sorted() method
# myDict = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}

# sorts the keys of any given dict
# print(sorted(myDict))
# print((myDict))

# my_dict = {}
# my_dict[1] = 1
# my_dict['1'] = 2
# my_dict[1.0] = 4
 
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
    
# print (sum)

# rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
# id1 = id(rec)
# del rec
# rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
# id2 = id(rec)
# print(id1 == id2)

# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
 
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
 
# print(sum)
# print(my_dict)

# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
        
# addone('Apple')
# addone('Banana')
# addone('apple')
# print (len(fruit))

# rec = {"Name" : "Python", "Age":"20"}
# r = rec.copy()
# print(id(r) == id(rec))

# arr = {}
# arr[1] = 1
# arr['1'] = 2
# arr[1] += 1
 
# sum = 0
# for k in arr:
#     sum += arr[k]
 
# print(sum)

# dict = {'c': 97, 'a': 96, 'b': 98}
 
# for _ in sorted(dict):
#     print (dict[_])

box = {}
jars = {}
crates = {}
box['biscuit'] = 1
box['cake'] = 3
jars['jam'] = 4
crates['box'] = box
crates['jars'] = jars
print(len(crates[box]))