from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)
opt.add_argument('--disable-notifications')

dr = webdriver.Chrome(options=opt)

dr.maximize_window()

dr.get('https://demoapps.qspiders.com/ui/frames?sublist=0')
sleep(1)

dr.switch_to.frame(0)
sleep(1)
dr.find_element(By.ID, 'username').send_keys('Hello')
sleep(1)
dr.find_element(By.ID, 'password').send_keys('Teddy Bear')
sleep(1)
dr.find_element(By.ID, 'submitButton').click()
