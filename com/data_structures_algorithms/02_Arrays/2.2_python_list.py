pyList = [4, 12, 2, 34, 17]

print(len(pyList))


# appending
pyList.append([50, 8, 10])
print(pyList)


# Extending
listB = [7, 8, 10]

pyList.extend(listB)
print(pyList)

pyList.insert(4, 100)
print(pyList)

pyList.pop(-1)
print(pyList)

pyList[2:5]
print(pyList)