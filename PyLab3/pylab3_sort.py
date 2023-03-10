# sort
from datetime import datetime
import random

import prettytable as prettytable
from matplotlib import pyplot as plt


def bubbleSort(A):
    for i in range(len(A)):
        for j in range(len(A)-1-i):
            if A[j] > A[j+1]:
                a = A[j]
                A[j] = A[j+1]
                A[j+1] = a


def selectSort(A):
    for i in range(len(A)-1):
        m = i
        for j in range(i, len(A)):
            if A[j] < A[m]:
                m = j
            A[m], A[i] = A[i], A[m]


def insertSort(A):
    for i in range(1, len(A)):
        t = A[i]
        j = i
        for j in range(j, 0, -1):
            if A[j-1] > t:
                A[j] = A[j-1]
            else:
                A[j] = t
                break


table = prettytable.PrettyTable(["Размер списка", "Время пузырька", "Время быстрой", "Время вставкой", "Время выбором"])
x = []
y1 = []
y2 = []
y3 = []
y4 = []

for N in range(1000, 5001, 1000):
    x.append(N)
    min = 1
    max = N
    A = []
    for i in range(N):
        A.append(int(round(random.random() * (max - min) + min)))

    print("\nИсходный список А:")
    print(A)

    B = A.copy()
    C = A.copy()
    D = A.copy()
    # print(B)

    # BubbleSort(A)
    print("---")
    # print(A)

    # QuickSort(B, 0, len(B)-1)
    # print("---")
    # print(B)

    # InsertSort(C)
    # print("---")
    # print(C)

    t1 = datetime.now()
    bubbleSort(A)
    t2 = datetime.now()
    y1.append((t2 - t1).total_seconds())


    t3 = datetime.now()
    C.sort()
    t4 = datetime.now()
    y2.append((t4 - t3).total_seconds())


    t5 = datetime.now()
    insertSort(C)
    t6 = datetime.now()
    y3.append((t6 - t5).total_seconds())


    t7 = datetime.now()
    selectSort(D)
    t8 = datetime.now()
    y4.append((t8 - t7).total_seconds())

    table.add_row(
        [str(N), str((t2 - t1).total_seconds()), str((t4 - t3).total_seconds()), str((t6 - t5).total_seconds()),
         str((t8 - t7).total_seconds())])
print(table)

plt.plot(x, y1, "C0")
plt.plot(x, y2, "C1")
plt.plot(x, y3, "C2")
plt.plot(x, y4, "C3")
plt.show()