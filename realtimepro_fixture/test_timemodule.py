import pytest
from selenium.webdriver import ActionChains, Keys
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class TestCase2:
    def test_time(self):
        self.driver.find_element(By.XPATH, "//span[text()='Time']").click()
        sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']").send_keys("peter")
        sleep(2)
        actions = ActionChains(self.driver)
        actions.key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
        sleep(2)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        sleep(2)
        expected_output = self.driver.find_element(By.XPATH, "//p[text()='No Timesheets Found']")
        assert expected_output.is_displayed(),"time sheet is present"
        print("i got the expected output")
