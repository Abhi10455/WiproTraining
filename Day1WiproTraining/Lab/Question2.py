data = [1, 2, 3, 4, 5, 6, 2, 4]
squareslist = [a**2 for a in data]
uniqueevenset = {a for a in data if a % 2 == 0}
cubedict = {a: a**3 for a in data}

print("Squares List:", squareslist)
print("Unique Even Set:", uniqueevenset)
print("Cube Dictionary:", cubedict)