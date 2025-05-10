from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)
opt.add_argument('--disable-notifications')

dr = webdriver.Chrome(options=opt)

dr.maximize_window()

dr.get('https://demoapps.qspiders.com/ui/frames/nested?sublist=1')
sleep(1)
dr.switch_to.frame(0)
sleep(1)
dr.switch_to.frame(0)
sleep(1)
dr.find_element(By.ID, 'email').send_keys('Admin@gmail.com')
sleep(1)
dr.find_element(By.ID, 'password').send_keys('Admin@1234')
sleep(1)
dr.find_element(By.ID, "confirm-password").send_keys('Admin@1234')
sleep(1)
dr.find_element(By.ID, 'submitButton').click()