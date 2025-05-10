from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

dr = webdriver.Chrome(options=opt)
dr.maximize_window()

dr.implicitly_wait(15)

dr.get('https://omayo.blogspot.com/')

dr.find_element(By.XPATH, '//button[@class="dropbtn"]').click()

dr.find_element(By.LINK_TEXT, 'Facebook').click()
dr.back()

wait = WebDriverWait(dr, 20)
wait.until(expected_conditions.element_to_be_clickable((By.ID, 'timerButton')))

dr.find_element(By.ID, 'timerButton').click()

# alert = dr.switch_to.alert
# print(alert.text)
# alert.accept()
