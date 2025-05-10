from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class TeseCase2:
    def test_admin(self):
        sleep(1)
        self.driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys('Admin')
        sleep(2)
        admin = self.driver.find_element(By.XPATH, '//span[text()="Admin"]')
        sleep(1)
        assert admin.is_displayed(), 'Admin is not present'
        print("Yeah, Admin's Here")

    def test_pim(self):
        sleep(2)
        pim = self.driver.find_element(By.XPATH, '//span[text()="PIM"]')
        assert pim.is_displayed(), 'PIM is not displayed'
        print('PIM is Displayed')
