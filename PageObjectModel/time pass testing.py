from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjectModel.LoginPage import Login

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

dr = webdriver.Chrome(options=opt)
dr.maximize_window()
dr.implicitly_wait(10)
dr.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
log = Login(dr)
log.send_username('Admin')
log.send_password('admin123')
log.login_click()

dr.find_element(By.XPATH, '//span[text()="Admin"]').click()