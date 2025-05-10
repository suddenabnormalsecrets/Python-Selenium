from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def setup(request):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    sleep(3)

    driver.find_element(By.NAME, 'username').send_keys('Admin')
    driver.find_element(By.NAME, 'password').send_keys('admin123')
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    request.cls.driver = driver
    yield

    driver.find_element(By.XPATH, '//span[@class="oxd-userdropdown-tab"]').click()
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'Logout')
    sleep(3)
    # driver.quit()
