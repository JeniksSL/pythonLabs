import unittest

from PyLab4.Shop import Shop
from PyLab4.Car import Car
import pytest


@pytest.fixture
def carColors():
    car = Car()
    return car._Car__colors


def test__init__():
    shop = Shop()
    assert shop._Shop__id == 195151


def test_getID():
    shop = Shop()
    assert shop._Shop__id < Shop.getID()


def test_addCar(carColors):
    base_shop = Shop()
    for i in range(5):
        base_shop.addCar(Car.getRandomCar())
    assert all(carColors.__contains__(car.color) for car in base_shop._Shop__carList)



