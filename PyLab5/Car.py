# class with 5 magic methods
import datetime
import random
import webcolors


class Car:
    __brands = {"Audi": ("TT", "A8"), "Lamborghini": ("Diablo", "Gallardo"), "Nissan": ("Skyline", "350Z"),
                "Mazda": ("RX-7", "RX-8"), "Mitsubishi": ("Lancer", "Eclipse"), "Ford": ("Focus", "Mustang")}
    __colors = ("Red", "Green", "Blue", "White", "Cyan", "Yellow", "Magenta", "Black")

    def __init__(self):
        self.id = "not specified"
        self.brand = "not specified"
        self.model = "not specified"
        self.year = "not specified"
        self.color = "not specified"
        self.price = "not specified"
        self.regNumber = "not specified"

    @staticmethod
    def getRandomCar():
        brand = list(Car.__brands.keys())
        brand = brand[(random.randint(0, len(brand) - 1))]
        model = Car.__brands[brand]
        model = model[(random.randint(0, len(model) - 1))]
        year = random.randint(2000, datetime.datetime.now().year)
        color = Car.__colors[(random.randint(0, len(Car.__colors) - 1))]
        price = 2000 * random.uniform(100, 500) / (datetime.datetime.now().year - year + 20)
        regNumber = chr(random.randint(ord("A"), ord("Z"))) + chr(
            random.randint(ord("A"), ord("Z"))) + f"{(random.randint(0, 9999)):00004d}"
        newCar = Car()
        newCar.setBaseParameters(brand, model, year, color)
        newCar.setShopParameters(price, regNumber)
        return newCar

    def setBaseParameters(self, brand, model, year, color):
        try:
            if brand not in self.__brands.keys():
                raise ValueError("brand exception")
            if model not in self.__brands[brand]:
                raise ValueError("model exception")
            if not isinstance(year, int) or year > datetime.datetime.now().year or year < 1900:
                raise ValueError("year exception")
            if color not in self.__colors:
                raise ValueError("color exception")
            self.brand = brand
            self.model = model
            self.year = year
            self.color = color
        except ValueError as e:
            print("Base parameters exception: " + str(e))
            return

    def setShopParameters(self, price, regNumber):
        try:
            if not isinstance(price, (int, float)) or price < 0:
                raise ValueError("price exception")
            self.price = price
            self.regNumber = regNumber
        except ValueError as e:
            print("Shop parameters exception: " + str(e))
            return

    def __str__(self):
        return "Car " + self.brand + " " + self.model + ", year: " + str(self.year) + ", color: " + self.color + \
            ", reg.: " + self.regNumber + ", price: " + f"{self.price:.2f}" + "USD"

    def __eq__(self, other):
        if isinstance(other, Car):
            if self.brand.__eq__(other.brand) and self.model.__eq__(other.model) and self.year == other.year and self.color.__eq__(other.color):
                return True
        return False

    def __getattr__(self, item):
        if item == "ages":
            return datetime.datetime.now().year - self.year
        elif item == "id":
            return self.id
        elif item == "brand":
            return self.brand
        elif item == "model":
            return self.model
        elif item == "year":
            return self.year
        elif item == "color":
            return self.color
        elif item == "price":
            return self.price
        elif item == "regNumber":
            return self.regNumber
        else:
            print(f"Attribute {item} is not exist")
            raise AttributeError

    def __index__(self):
        return int(webcolors.CSS3_NAMES_TO_HEX[self.color.lower()].replace("#", ""), 16)

    def __add__(self, other):
        return self.price + other.price


cars = []
for i in range(5):
    cars.append(Car.getRandomCar())
counter = 0
for car in cars:
    print("Number of a car" + str(counter))
    print("A car: " + str(car)) # Uses __str__
    print("A color: " + car.color)
    print("A color in hex: " + hex(car)) # Uses __index__
    print("Is car equals first car: " + str(car == (cars[0])) ) # Use __eq__
    print("Ages of a car: " + str(car.ages)) # Uses __getattr__
    print("Price: " + str(car.price))
    print("Car + first car: " + str(car+cars[0])) # Uses __add__





