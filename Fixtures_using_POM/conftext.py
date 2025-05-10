import pytest
from selenium import webdriver
from time import sleep
from Fixtures_using_POM.Login_page import Login
from Fixtures_using_POM.Home_page import Home

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    sleep(2)
    log = Login(driver)
    home = Home(driver)
    log.send_username("Admin")
    log.send_password("admin123")
    log.login_click()
    sleep(2)
    # request.cls.driver = driver
    yield
    home.user_log()
    sleep(2)
    home.log_out()
    driver.close()