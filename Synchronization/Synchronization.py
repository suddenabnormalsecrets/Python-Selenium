# 31-MAR-25
"""
Synchronization :

- It is the process of matching the selenium speed with the browser speed.
To achieve synchronization, we can go for four ways

1. Explicit wait
2. Implicit wait
3. Time.sleep
4. Fluent wait

1. Explicit wait:-

- Create WebDiver Wait.
- Provide condition based on the state of the web element.

2. Implicit wait:-

Syntax:-
- driver.implicit_wait(2)
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

dr = webdriver.Chrome(options=opt)
dr.maximize_window()
dr.get('https://www.shoppersstack.com/')
sleep(0.5)
dr.find_element(By.XPATH, '')
