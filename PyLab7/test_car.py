import datetime

from PyLab4.Car import Car
import unittest


class CarTest(unittest.TestCase):
    def test__init__(self):
        self.assertEqual(Car().id, "not specified")
        self.assertEqual(Car().brand, "not specified")
        self.assertEqual(Car().model, "not specified")
        self.assertEqual(Car().year, "not specified")
        self.assertEqual(Car().color, "not specified")
        self.assertEqual(Car().price, "not specified")
        self.assertEqual(Car().regNumber, "not specified")

    def test_getRandomCar(self):
        car = Car().getRandomCar()
        self.assertEqual(car.getRandomCar().id, "not specified")
        self.assertIn(car.brand, car._Car__brands.keys())
        self.assertIn(car.model, car._Car__brands[car.brand])
        self.assertLessEqual(car.year, datetime.datetime.now().year)
        self.assertIn(car.color, car._Car__colors)
        self.assertTrue(isinstance(car.price, float))
        self.assertRegex(car.regNumber, r'(?:[A-Z0-9])')

    def test_setBaseParameters(self):
        base_car = Car().getRandomCar()
        car = Car()
        car.setBaseParameters(base_car.brand, base_car.model, base_car.year, base_car.color)
        self.assertIs(car.brand, base_car.brand)
        self.assertIs(car.model, base_car.model)
        self.assertIs(car.year, base_car.year)
        self.assertIs(car.color, base_car.color)

    def test_setShopParameters(self):
        base_car = Car().getRandomCar()
        car = Car()
        car.setShopParameters(base_car.price, base_car.regNumber)
        self.assertIs(car.price, base_car.price)
        self.assertIs(car.regNumber, base_car.regNumber)

    def test_toString(self):
        car = Car().getRandomCar()
        car_str = car.toString()
        self.assertIn(str(car.brand), car_str)
        self.assertIn(str(car.model), car_str)
        self.assertIn(str(car.year), car_str)
        self.assertIn(str(car.color), car_str)
        self.assertIn(f"{car.price:.2f}", car_str)
        self.assertIn(str(car.regNumber), car_str)


if __name__ == '__main__':
    unittest.main()