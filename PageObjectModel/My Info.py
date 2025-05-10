from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

dr.find_element(By.XPATH, '//span[text()="My Info"]').click()
sleep(1)
first = dr.find_element(By.XPATH, '')
act.double_click(first).click().perform()
sleep(2)
first.send_keys('Monkey')
sleep(2)
mid = dr.find_element(By.XPATH, '')
act.double_click(mid).click().perform()
sleep(2)
mid.send_keys('D.')
sleep(2)
last = dr.find_element(By.XPATH, '')
act.double_click(last).click().perform()
sleep(2)
last.send_keys('Luffy')
sleep(2)
emp_id = dr.find_element(By.XPATH, '')
act.double_click(emp_id).perform()
emp_id.send_keys('00000')
sleep(1)
# date = dr.find_element(By.XPATH, "//div[@class='oxd-date-input']/input")
# act.double_click(date).click().perform()
# sleep(2)
# date.clear()
# sleep(2)
# date.send_keys('2023-04-10')
dr.find_element(By.XPATH, '').click()
sleep(2)
dr.find_element(By.XPATH, '//button[text()=" Save "]').click()
dr.refresh()