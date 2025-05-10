import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

@pytest.fixture
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    sleep(2)
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    sleep(2)
    request.cls.driver = driver
    yield
    driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
    sleep(2)
    driver.find_element(By.XPATH, "//a[text()='Logout']").click()
    driver.close()