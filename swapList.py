def swapList(newList):

    size = len(newList)
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList

newList= [13, 50, 30, 40, 14]
print(swapList(newList))