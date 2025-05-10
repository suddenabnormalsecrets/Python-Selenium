# 03-APR-25
"""
JavaScript Executor:
- When normal elements and webdriver methods are not working that when we have to go for JavaScript executor.

Execute_script()
execute_asyal_script()

- Scrolling
    1. Scroll by
    2. Scroll to
    3. Scroll into view
- perform action on disabled element
- perform action on a hidden element

"""

from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.select import Select
from time import sleep


opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

dr = webdriver.Chrome(options=opt)
dr.maximize_window()

dr.get('https://omayo.blogspot.com/')
sleep(1)

dr.execute_script('window.scrollBy(0, 500);')
sleep(1)
dr.execute_script('window.scrollBy(0, 500);')

sleep(1)

dr.execute_script('window.scrollTo(0, 500);')
sleep(1)
dr.execute_script('window.scrollTo(0, 500);')

# a = dr.find_element(By.XPATH, '//p[@id="testdoubleclick"]')
