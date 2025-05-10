from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)
opt.add_argument('--disable-notifications')

dr = webdriver.Chrome(options=opt)

dr.maximize_window()

dr.get('https://demoapps.qspiders.com/')

dr.maximize_window()
sleep(1)
dr.find_element(By.XPATH, '//main[@data-aos="zoom-in"]/div[1]').click()
sleep(1)
dr.find_element(By.XPATH, '//section[contains(text(), "Frames")]').click()
sleep(1)
dr.find_element(By.XPATH, '//section[contains(text(), "iframes")]').click()
sleep(1)
dr.find_element(By.XPATH, '//a[text()="Multiple iframe"]').click()
sleep(1)
dr.switch_to.frame(0)
dr.find_element(By.ID, 'email').send_keys("Admin@gmail.com")
sleep(1)
dr.find_element(By.ID, 'password').send_keys('Admin@1234')
sleep(1)
dr.find_element(By.ID, 'confirm-password').send_keys('Admin@1234')
sleep(1)
dr.find_element(By.ID, 'submitButton').click()
sleep(1)
dr.switch_to.parent_frame()
sleep(1)
dr.switch_to.frame(1)
sleep(1)
dr.find_element(By.ID, 'username').send_keys('SuperAdmin@gmail.com')
dr.find_element(By.ID, 'password').send_keys('SuperAdmin@1234')
dr.find_element(By.ID, 'submitButton').click()
