# Creating a dictionary
# myDict = dict()
# print(myDict)

# secDict = {}
# print(secDict)

# engToEsp = {"one":"uno", "two":"dos", "three":"tres"}
# print(engToEsp['three'])

myDict = {'name': 'Sumon', 'age': 29}

# updating a value
# myDict['age'] = 30

# inserting/adding a value in dictionary
myDict['height'] = 170
# print(myDict)

# Travese through a dictionary
def traverseDict(dict):
    for key in dict:
        print(key, dict[key])
    
traverseDict(myDict)