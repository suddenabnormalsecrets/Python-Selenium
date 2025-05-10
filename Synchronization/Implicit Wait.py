from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

dr = webdriver.Chrome(options=opt)
dr.maximize_window()
dr.implicitly_wait(15)
dr.get('https://www.shoppersstack.com/')
dr.find_element(By.ID, 'loginBtn').click()
dr.find_element(By.XPATH, '//span[text()="Create Account"]').click()
