from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

dr = webdriver.Chrome(options=opt)
dr.maximize_window()
dr.implicitly_wait(10)
dr.get('https://demoapps.qspiders.com/ui?scenario=1')
sleep(2)
dr.find_element(By.XPATH, '//li[text()="Disabled"]').click()

name = dr.find_element(By.ID, 'name')
dr.execute_script("arguments[0].value='Teddy Bear'", name)
sleep(1)
email = dr.find_element(By.ID, 'email')

dr.execute_script("arguments[0].value='teddybear0907@gmail.com'", email)
sleep(1)
password = dr.find_element(By.ID, 'password')

dr.execute_script("arguments[0].value='TeddyBear@09'", password)
sleep(1)
dr.find_element(By.XPATH, '//button[text()="Register"]').click()
