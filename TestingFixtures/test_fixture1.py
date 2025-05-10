import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_search(setup):
    dr = setup
    wait = WebDriverWait(dr, 10)
    search_input = wait.until(ec.presence_of_element_located((By.XPATH, '//input[@placeholder="Search"]')))
    search_input.send_keys('Sam')

    a = ActionChains(dr)
    a.key_down(Keys.ENTER).perform()
