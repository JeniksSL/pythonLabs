# Task 1 (11), 2 (3), 3 (11)
import random
from datetime import date, datetime
import pandas as pd


class Task1:
    pass

    def __init__(self, isrand=True):
        maxValue = random.uniform(-1000, 1000)
        if isrand:
            print("Numbers choosing randomly")

            for i in range(4):
                if i == 0 or i == 3:
                    rand = maxValue
                else:
                    rand = random.uniform(-1000, 1000)
                maxValue = rand if rand > maxValue else maxValue
                character = ord("a")
                print(chr(character + i) + " = " + str(rand))
        else:
            print("Not allowed))")


class Scholar:
    pass

    year =0
    ismale = 0
    height = 0
    weight = 0

    def __init__(self):
        self.year = random.uniform(2005, 2008)
        self.ismale = True if random.randint(0, 1) > 0 else False
        self.height = random.uniform(8, 10)*self.getAges()
        self.weight = random.uniform(2, 4)*self.getAges()
        print(self.toString())

    def getAges(self):
        return int(datetime.now().year)-self.year

    def toString(self):
        gender = "Boy" if self.ismale else "Girl"
        return "Ages: "+str(self.getAges())+", Gender: "+gender+", Height: " + str(self.height)+ ", Weight: "+ str(self.weight)

class Task3:
    pass

    def __init__(self):
        length=0
        while True:
            try:
                n = int(input("Input array size (less than 100): "))
                if n < 1 or n>100:
                    raise Exception()
                length=n
                break
            except Exception as e:
                print('Invalid format')
        initList=[]
        for i in range(length):
            initList.append(random.randint(0, 99))
        print("Initial list:" + str(initList))
        try:
            count = 0
            removed = 0
            while True:
                if initList[count] % 2 == 1:
                    print("Removed: " + str(initList.pop(count)))
                    removed += 1
                else:
                    count += 1
                if removed >= 5:
                    print("Result list:" + str(initList))
                    break

        except Exception as e:
            print('Array have not 5 odd numbers')










print("Task 1-(#11)")
Task1()
print("Task 2-(#3)")
print("Class:")
school = []
boys = 0
girls = 0
midyear= 0
higherBoy = 0
weightBoy = 1
lowestGirl=0
youngerGirl = 1
for i in range(10):
    school.append(Scholar())
    if school[i].ismale:
        boys += 1
        if not isinstance(higherBoy, Scholar):
            higherBoy = school[i]
            weightBoy=school[i]
        else:
            higherBoy =school[i] if school[i].height>higherBoy.height else higherBoy
            weightBoy = school[i] if school[i].weight > higherBoy.weight else higherBoy
    else:
        girls += 1
        if not isinstance(lowestGirl, Scholar):
            lowestGirl = school[i]
            youngerGirl = school[i]
        else:
            lowestGirl = school[i] if school[i].height < lowestGirl.height else lowestGirl
            youngerGirl = school[i] if school[i].getAges() < youngerGirl.getAges() else youngerGirl
    midyear = (midyear*i+school[i].getAges())/(i+1)

print("Average ages:" + str(midyear))
print("The highest: "+higherBoy.toString())
print("The weightiest: "+weightBoy.toString())
print("Is same: "+str(hash(higherBoy)==hash(weightBoy)))
print("The lowest: "+lowestGirl.toString())
print("The youngest: "+youngerGirl.toString())
print("Is same: "+str(hash(lowestGirl)==hash(youngerGirl)))

print("Task 3-(#11)")
Task3()


