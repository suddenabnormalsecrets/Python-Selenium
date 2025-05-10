# 26-MAR-25
"""
Iframe is also known as Embedded Frame:
- A Webpage inside another Webpage.

To operate on an Iframe, we have to switch to the iframe from the main frame.

- Syntax to Switch from one page to another page is

driver.switch_to.frame(arg)

1. int = index of the Iframe

# dr.switch_to.frame(0)

2. String = Value of name/id attribute

# dr.switch_to.frame("send-sms-iframe")

3. Web Element = Web element ref of the Iframe

# dr.switch_to.frame("send-sms-iframe")

There are Multiple Types of Iframe

1. Nested Iframe
    - One iframe inside another iframe is called as Nested Iframe.

2. Multiple Iframe


3. Nested Multiple Iframe:
    -

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)
opt.add_argument('--disable-notifications')

dr = webdriver.Chrome(options=opt)

dr.maximize_window()

dr.get('https://www.dream11.com/')
sleep(1)
dr.switch_to.frame(0)
# dr.switch_to.frame("send-sms-iframe")
# dr.switch_to.frame()
dr.find_element(By.ID, 'regEmail').send_keys('7972369527')
