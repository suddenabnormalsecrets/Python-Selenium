from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures('setup')
class TestCase2:

    def test_time(self):
        sleep(1)
        self.driver.find_element(By.XPATH, '//span[text()="Time"]').click()
        self.driver.find_element(By.XPATH, '//input[@placeholder="Type for hints..."]').send_keys('Monkey D. Luffy')
        sleep(2)
        act = ActionChains(self.driver)
        act.key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
        sleep(1)
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        sleep(2)
        don = self.driver.find_element(By.XPATH, '//p[text()="No Timesheets Found"]')
        assert don.is_displayed(), 'It is Not Displayed'
        print('👍')
