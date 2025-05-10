# 01-APR-25
"""

There are several ways to take screenshot()

- Save_screenshot()
- get_screenshot_as_png()
- get_screenshot_as_file()
- get_screenshot_as_base64()

"""
from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

dr = webdriver.Chrome(options=opt)
dr.maximize_window()
dr.implicitly_wait(10)
dr.get('https://demowebshop.tricentis.com/')

# dr.save_screenshot('homepage.png')


img = dr.find_element(By.XPATH, '//div[@class="header-logo"]')

img.screenshot('../Screenshots/dws.png')