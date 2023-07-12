import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PythonMainPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # закрытие браузера при окончании каждого теста
        self.driver.close()


    def test_list_sort(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(3)
        driver.find_element(By.ID, "login-button").click()
        items0 = driver.find_elements(By.CLASS_NAME, "inventory_item")
        select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
        select.select_by_value("za")
        time.sleep(3)
        items1 = driver.find_elements(By.CLASS_NAME, "inventory_item")
        items1.reverse()
        self.assertEqual(items0, items1)

    def test_sign_in(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        self.assertIn("Swag Labs", driver.title)
        password = driver.find_element(By.CLASS_NAME, "login_password")
        password = driver.execute_script('return arguments[0].lastChild.textContent;', password).strip()
        self.assertEqual(password, "secret_sauce")
        login = driver.find_element(By.ID, "login_credentials").get_attribute('innerHTML')
        login = login.split("</h4>")[1].split("<br>")[0].strip()
        self.assertEqual(login, "standard_user")
        driver.find_element(By.ID, "user-name").send_keys(login)
        driver.find_element(By.ID, "password").send_keys(password)
        time.sleep(3)
        driver.find_element(By.ID, "login-button").click()
        self.assertTrue(driver.find_element(By.CLASS_NAME, "footer_copy").
                        text.index("Sauce Labs. All Rights Reserved.") >= 0)

    def test_locked_user(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver = self.driver
        driver.get("https://www.saucedemo.com")
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(3)
        self.assertTrue(driver.find_element(By.CLASS_NAME, "error-message-container").
                        text.index("Epic sadface: Sorry, this user has been locked out.") >= 0)
        print(driver.current_url)
        self.assertTrue(driver.current_url == "https://www.saucedemo.com/")

    def test_problem_user(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com")
        driver.find_element(By.ID, "user-name").send_keys("problem_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(3)
        driver.find_element(By.ID, "login-button").click()
        items = driver.find_elements(By.XPATH, "//img[@class='inventory_item_img']")
        for item in items:
            self.assertEqual(item.get_attribute("src"), "https://www.saucedemo.com/static/media/sl-404.168b1cce.jpg")
        driver.execute_script('return arguments[0].parentElement;', items[0]).click()
        self.assertEqual(driver.current_url, "https://www.saucedemo.com/inventory-item.html?id=5")

    def test_buy_item(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(3)
        driver.find_element(By.ID, "login-button").click()
        items = driver.find_element(By.ID, "inventory_container").find_elements(By.CLASS_NAME, "inventory_item")
        for item in items:
            item.find_element(By.TAG_NAME, "button").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(3)
        driver.find_element(By.ID, "checkout").click()
        driver.find_element(By.ID, "first-name").send_keys("first-name")
        driver.find_element(By.ID, "last-name").send_keys("last-name")
        driver.find_element(By.ID, "postal-code").send_keys("postal-code")
        driver.find_element(By.ID, "continue").click()
        driver.find_element(By.ID, "finish").click()
        self.assertTrue(driver.find_element(By.CLASS_NAME, "complete-header").
                        text.index("Thank you for your order!") >= 0)


if __name__ == '__main__':
    unittest.main()



