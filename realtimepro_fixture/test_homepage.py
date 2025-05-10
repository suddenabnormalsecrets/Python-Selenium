# import pytest
# from selenium import webdriver
# from time import sleep
# from selenium .webdriver.common.by import By
#
# @pytest.fixture
# def setup():
#     global driver
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(15)
#     driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#     sleep(2)
#     driver.find_element(By.NAME, "username").send_keys("Admin")
#     driver.find_element(By.NAME, "password").send_keys("admin123")
#     driver.find_element(By.XPATH, "//button[@type='submit']").click()
#     sleep(2)
#     yield
#     driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
#     sleep(2)
#     driver.find_element(By.XPATH, "//a[text()='Logout']").click()
#     driver.close()
#
# def test_admin(setup):
#     driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--active']").send_keys("admin")
#     sleep(2)
#     admin = driver.find_element(By.XPATH, "//span[text()='Admin']")
#     sleep(2)
#     assert admin.is_displayed(), "admin is not present"
#     print("admin is present")
#
# def test_pim(setup):
#     pim = driver.find_element(By.XPATH, "//span[text()='PIM']")
#     assert pim.is_displayed(),"PIM is not displayed"
#     print("PIM is displayed")
#
