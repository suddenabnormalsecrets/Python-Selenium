from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

dr = webdriver.Chrome(options=opt)
dr.maximize_window()
dr.implicitly_wait(10)

dr.get('https://www.oracle.com/in/java/technologies/downloads/')

a = dr.find_element(By.LINK_TEXT, 'jdk-17.0.14_linux-x64_bin.deb')

dr.execute_script("arguments[0].scrollIntoView(false)", a)
a.click()
sleep(0.01)
b = dr.find_element(By.LINK_TEXT, 'Download jdk-17.0.14_linux-x64_bin.deb')

dr.execute_script("arguments[0].click()", b)
