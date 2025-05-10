from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

dr = webdriver.Chrome(options=opt)

dr.maximize_window()
dr.get('https://demoapps.qspiders.com/ui/browser?sublist=0')
dr.implicitly_wait(15)
dr.find_element(By.XPATH, '//section[text() = "Popups"]').click()
dr.find_element(By.XPATH, '//section[text() = "Javascript"]').click()
dr.find_element(By.LINK_TEXT, 'Default Alert').click()
dr.find_element(By.ID, 'buttonAlert2').click()
sleep(2)

alert = dr.switch_to.alert
alert.accept()
sleep(2)
dr.find_element(By.LINK_TEXT, 'Confirm').click()
dr.find_element(By.ID, 'buttonAlert5').click()
alert.dismiss()
sleep(2)
dr.find_element(By.LINK_TEXT, 'Prompt').click()
dr.find_element(By.ID, 'buttonAlert1').click()
sleep(2)
alert.send_keys('Yes')
alert.accept()
