import datetime
import numpy as np
from matplotlib import pyplot as plt


class Shop:
    __id = 195151
    __carList = []

    def __int__(self):
        None

    @classmethod
    def getID(cls):
        cls.__id += 1
        return cls.__id

    @classmethod
    def addCar(cls, newCar):
        newCar.id = Shop.getID()
        cls.__carList.append(newCar)

    @classmethod
    def getCarListByBrand(cls, brand):
        carList = []
        for storedCar in cls.__carList:
            if storedCar.brand == brand:
                carList.append(storedCar)
        return carList

    @classmethod
    def getCarListByModel(cls, model, inOperation=-1):
        carList = []
        currentYear = datetime.datetime.now().year
        for storedCar in cls.__carList:
            if storedCar.model == model and currentYear-storedCar.year > inOperation:
                carList.append(storedCar)
        return carList

    @classmethod
    def getStatistics(cls):
        brands = {}
        years = []
        prices = []
        for storedCar in cls.__carList:
            prices.append(storedCar.price)
            years.append(storedCar.year)
            name = storedCar.brand + " " + storedCar.model
            if name in brands.keys():
                brands[name] += 1
            else:
                brands[name] = 1
        fig = plt.figure(figsize=(20,4))
        ax1 = fig.add_subplot(1, 4, 1)
        ax2 = fig.add_subplot(1, 4, 2)
        ax3 = fig.add_subplot(1, 4, 3)
        ax4 = fig.add_subplot(1, 4, 4)
        ax1.pie(brands.values(), labels=brands.keys(), autopct='%1.1f%%')
        ax2.hist(years)
        ax3.scatter(years, prices)
        npBrands = np.arange(len(brands.keys()))
        ax4.barh(npBrands, brands.values())
        ax4.set_yticks(npBrands, brands.keys())
        plt.subplots_adjust(left=0.1,
                            bottom=0.1,
                            right=0.90,
                            top=0.90,
                            wspace=0.6,
                            hspace=0.4)
        plt.show()