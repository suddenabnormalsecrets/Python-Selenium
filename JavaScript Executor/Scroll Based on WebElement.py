from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

dr = webdriver.Chrome(options=opt)
dr.maximize_window()

dr.get('https://omayo.blogspot.com/')
sleep(1)

a = dr.find_element(By.XPATH, '//button[@class="dropbtn"]')
dr.execute_script("arguments[0].scrollIntoView(true);", a)
