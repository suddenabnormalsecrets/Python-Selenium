from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

dr = webdriver.Chrome(options=opt)
dr.maximize_window()

dr.get('https://www.facebook.com')

dr.find_element(By.LINK_TEXT, 'Create new account').click()

gen = dr.find_element(By.ID, 'custom_gender')

dr.execute_script('arguments[0].value="Gay"', gen)

