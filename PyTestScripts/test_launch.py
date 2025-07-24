# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
# #
# # @pytest.mark.regression
# # def test_dws():
# #     driver = webdriver.Chrome()
# #     driver.maximize_window()
# #     driver.implicitly_wait(10)
# #     driver.get('https://demowebshop.tricentis.com/')
# #     print("This is DWS page")
# #     driver.close()
# #
# #
# # @pytest.mark.smoke
# # def test_ducati():
# #     dr = webdriver.Chrome()
# #     dr.maximize_window()
# #     dr.implicitly_wait(10)
# #     dr.get('https://www.ducati.com/in/en/home')
# #     print('Vroom Vroom')
# #     dr.close()
# #
# #
# # @pytest.mark.smoke
# # def test_mv():
# #     dr = webdriver.Chrome()
# #     dr.maximize_window()
# #     dr.implicitly_wait(10)
# #     dr.get('https://www.mvagusta.com/')
# #     print('vroom vroom')
# #     dr.close()
#
#
# # @pytest.mark.parametrize("username, password", [("Admin", "admin123")])
# # def test_demo(username, password):
# #     print(username)
# #     print(password)
#
#
# @pytest.mark.parametrize("username, password", [("Admin", "admin123"), ("admin", "admin321")])
# def test_orange(username, password):
#     dr = webdriver.Chrome()
#     dr.maximize_window()
#     dr.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
#     sleep(2)
#     dr.find_element(By.NAME, 'username').send_keys(username)
#     dr.find_element(By.NAME, 'password').send_keys(password)
#     sleep(2)
#     dr.find_element(By.XPATH, '//button[text() = " Login "]').click()
#     dr.close()
