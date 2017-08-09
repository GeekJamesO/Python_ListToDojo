def make_dict(arr1, arr2):
    new_dict = {}

    Keys = []
    Values = []
    if len(arr1) >= len(arr2):
        Keys = arr1
        Values = arr2
    else:
        Keys = arr2
        Values = arr1
    KeysLength   = len(Keys)
    ValuesLength = len(Values)

    for i in range(0, KeysLength ):
        if i < ValuesLength:
            new_dict[ Keys[i] ] =  Values[i]
        else:
            new_dict[ Keys[i] ] =  None
    return new_dict

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

print make_dict(name, favorite_animal)
