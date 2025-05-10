import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_admin(setup):
    dr = setup
    wait = WebDriverWait(dr, 10)
    admin_tab = wait.until(ec.element_to_be_clickable((By.XPATH, '//span[text() = "Admin"]')))
    admin_tab.click()
