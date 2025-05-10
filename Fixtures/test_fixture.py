# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
#
#
# @pytest.fixture()
# def setup():
#     dr = webdriver.Chrome()
#     dr.maximize_window()
#     dr.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
#
#     wait = WebDriverWait(dr, 10)
#
#     wait.until(ec.presence_of_element_located((By.NAME, 'username'))).send_keys('Admin')
#     wait.until(ec.presence_of_element_located((By.NAME, 'password'))).send_keys('admin123')
#     wait.until(ec.element_to_be_clickable((By.XPATH, '//button[text() = " Login "]'))).click()
#
#     yield dr
#
#     wait.until(ec.element_to_be_clickable((By.XPATH, '//span[@class="oxd-userdropdown-tab"]'))).click()
#     wait.until(ec.element_to_be_clickable((By.LINK_TEXT, 'Logout'))).click()
#     dr.quit()
#
#
# def test_search(setup):
#     dr = setup
#     wait = WebDriverWait(dr, 10)
#     search_input = wait.until(ec.presence_of_element_located((By.XPATH, '//input[@placeholder="Search"]')))
#     search_input.send_keys('Sam')
#
#     a = ActionChains(dr)
#     a.key_down(Keys.ENTER).perform()
#
#
# def test_admin(setup):
#     dr = setup
#     wait = WebDriverWait(dr, 10)
#     admin_tab = wait.until(ec.element_to_be_clickable((By.XPATH, '//span[text() = "Admin"]')))
#     admin_tab.click()
#
# # @pytest.fixture()
# # def setup():
# #     print("pre condition")
# #     yield
# #     print("post condition")
# #
# #
# # def test_start1(setup):
# #     print('start 1')
# #
# #
# # def test_start2(setup):
# #     print('start 2')
