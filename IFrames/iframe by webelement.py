from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)
opt.add_argument('--disable-notifications')

dr = webdriver.Chrome(options=opt)
dr.maximize_window()

dr.get('https://www.dream11.com/')
sleep(1)
a = dr.find_element(By.ID, "send-sms-iframe")
dr.switch_to.frame(a)
dr.find_element(By.ID, 'regEmail').send_keys('7972369527')
sleep(1)
dr.switch_to.parent_frame()
# dr.switch_to.default_content()
dr.find_element(By.ID, 'menu_parent').click()
