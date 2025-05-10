import pytest
from selenium import webdriver
from time import sleep
from selenium .webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class TestCase1:
    def test_admin(self):
        self.driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--active']").send_keys("admin")
        sleep(2)
        admin = self.driver.find_element(By.XPATH, "//span[text()='Admin']")
        sleep(2)
        assert admin.is_displayed(), "admin is not present"
        print("admin is present")

    def test_pim(self):
        pim = self.driver.find_element(By.XPATH, "//span[text()='PIM']")
        assert pim.is_displayed(),"PIM is not displayed"
        print("PIM is displayed")

