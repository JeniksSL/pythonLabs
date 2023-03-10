# Task 1 (5)
from PyLab5.Shop import Shop
from PyLab5.Car import Car


for i in range(20):
    Shop.addCar(Car.getRandomCar())
Shop.getStatistics()
# List of cars Audi
for car in Shop.getCarListByBrand("Audi"):
    print(car.toString())
print()
# List of cars model TT older than 5 year
for car in Shop.getCarListByModel("TT", 5):
    print(car.toString())




