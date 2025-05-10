from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

dr = webdriver.Chrome(options=opt)
dr.maximize_window()
dr.get('https://www.shoppersstack.com/')
wait = WebDriverWait(dr, 30)
wait.until(expected_conditions.visibility_of_element_located((By.ID, 'loginBtn')))
dr.find_element(By.ID, 'loginBtn').click()
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//span[text()="Create Account"]')))
dr.find_element(By.XPATH, '//span[text()="Create Account"]').click()
