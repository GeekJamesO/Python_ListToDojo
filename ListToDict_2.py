def make_dict(arr1, arr2):
    new_dict = {}
    if len(arr1) < len(arr2):
        temp = arr1
        arr1 = arr2
        arr2 = temp
    for i in range(0, len(arr1)):
        if (len(arr2) > i):
            new_dict[arr1[i]] = arr2[i]
        else:
            new_dict[arr1[i]] = None
    return new_dict


name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def showInputsAndOutputs(arr1, arr2):
    print "Array 1 ( length",  len(arr1),")  :  ", arr1
    print "Array 2 ( length",  len(arr2),")  :  ", arr2
    result = make_dict(arr1, arr2)
    print "Result: ", result
    return result

print "Assignment: Making Dictionaries"
print "Create a function that takes in two lists and creates a single dictionary where the first list "
print "contains keys and the second values. Assume the lists will be of equal length."
print " "
showInputsAndOutputs(name, favorite_animal)

print "Hacker Challenge:"
print "If the lists are of unequal length, the longer list should be used for the keys, the shorter for the values."
print " "

print "Adding a Wilson to the end of the name list..   "
name.append('Wilson')
print " "
showInputsAndOutputs(name, favorite_animal)
print " "

print "Adding a Yak and Zebra to the end of the animal list..   "
favorite_animal.append('Yak')
favorite_animal.append('Zebra')
print " "
showInputsAndOutputs(name, favorite_animal)
