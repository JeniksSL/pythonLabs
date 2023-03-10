#Task 1 (#4), 2 (#1)
import random
import numpy as np

print("Task 1-(#4)")
length = 0
while True:
    try:
        n = int(input("Input list size (less than 100): "))
        if n < 1 or n > 100:
            raise ValueError()
        length = n
        break
    except ValueError:
        print('Invalid format')
initList = [random.randint(-100, 100) for i in range(length)]
multiplication = 1

for i in range(length):
    if i % 2 != 0:
        multiplication *= initList[i]
print("Initial list: " + str(initList))
print("The product of the list elements is:" + str(multiplication))
maxElement = max(initList)
print("Max element of list is: " + str(maxElement))
initList.remove(maxElement)
print("List with removed max element : " + str(initList))

print("Task 2-(#1)")
width = 0
height = 0
while True:
    try:
        n = int(input("Input matrix width (less than 100): "))
        m = int(input("Input matrix height (less than 100): "))
        if n < 1 or n > 100 or m < 1 or m > 100:
            raise ValueError()
        width = n
        height = m
        break
    except ValueError:
        print('Invalid format')

print("Standard")
matrix = []
for i in range(height):
    row = [random.randint(-100, 100) for j in range(width)]
    matrix.append(row)
sumRows = []
for row in matrix:
    sumRows.append(sum(row))
maxValue = max(sumRows)
maxRow = sumRows.index(maxValue)
print("Initial matrix: " + str(matrix))
print("Index of row with max value of elements sum: "+str(maxRow))

print("Using numpy")
npMatrix = np.matrix(matrix)
sumRows = npMatrix.sum(1)
npArray = np.array(sumRows)
maxRow = npArray.argmax(0)
print("Index of row with max value of elements sum: "+str(maxRow))

