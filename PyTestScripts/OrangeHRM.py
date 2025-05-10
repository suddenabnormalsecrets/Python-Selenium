from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

dr = webdriver.Chrome(options=opt)
dr.maximize_window()
dr.implicitly_wait(10)
dr.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

exp = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'

dr.find_element(By.NAME, 'username').send_keys('Admin')
dr.find_element(By.NAME, 'password').send_keys('admin123')
log = dr.find_element(By.XPATH, '//button[text() = " Login "]')
assert log.is_enabled()
print('Login Button is Enabled...')
log.click()
act = dr.current_url
assert exp == act

dr.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys('Teddy Bear')
sleep(2)
dr.find_element(By.CLASS_NAME, 'oxd-userdropdown-name').click()
sleep(2)
dr.find_element(By.LINK_TEXT, 'Logout').click()
dr.close()
