# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
# import random
# import string
#
# username = "User_" + ''.join(random.choices(string.ascii_letters, k=5))
# email = username.lower() + "@testmail.com"
# password = "Test@1234"
#
#
# def test_registration():
#     dr = webdriver.Chrome()
#     dr.maximize_window()
#     dr.implicitly_wait(10)
#     dr.get('https://demowebshop.tricentis.com/')
#     sleep(2)
#     dr.find_element(By.LINK_TEXT, 'Register').click()
#
#     gender = dr.find_element(By.ID, 'gender-male')
#     assert gender.is_enabled()
#     gender.click()
#
#     f_name = dr.find_element(By.ID, 'FirstName')
#     assert f_name.is_enabled()
#     f_name.send_keys(username)
#     sleep(1)
#     print(username)
#
#     l_name = dr.find_element(By.ID, 'LastName')
#     assert l_name.is_enabled()
#     l_name.send_keys('loo')
#     sleep(1)
#     print(l_name)
#
#     mail = dr.find_element(By.ID, 'Email')
#     assert mail.is_enabled()
#     mail.send_keys(email)
#     print(email)
#     sleep(1)
#
#     pas = dr.find_element(By.ID, 'Password')
#     assert pas.is_enabled()
#     pas.send_keys(password)
#     print(pas)
#     sleep(1)
#
#     dr.find_element(By.ID, 'ConfirmPassword').send_keys(password)
#     sleep(1)
#
#     dr.find_element(By.ID, 'register-button').click()
#     sleep(1)
#     rege = dr.find_element(By.XPATH, '//input[@value="Continue"]')
#     assert rege.is_enabled()
#     rege.click()
#     sleep(2)
#     dr.close()
#
#
# def test_log():
#     dr = webdriver.Chrome()
#     dr.implicitly_wait(10)
#     dr.get('https://demowebshop.tricentis.com/')
#     sleep(1)
#     dr.find_element(By.LINK_TEXT, 'Log in').click()
#
#     dr.find_element(By.ID, 'Email').send_keys(email)
#     dr.find_element(By.ID, 'Password').send_keys(password)
#
#     dr.find_element(By.XPATH, '//input[@value="Log in"]').click()
#     sleep(2)
#     dr.close()
