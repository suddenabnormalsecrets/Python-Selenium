from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

opt = webdriver.ChromeOptions()

opt.add_experimental_option('detach', True)

dr = webdriver.Chrome(options=opt)
dr.maximize_window()
act = ActionChains(dr)
dr.get('https://demo.guru99.com/test/simple_context_menu.html')

ex = 'https://demo.guru99.com/test/simple_context_menu.html'

a = dr.current_url
if a == ex:
    right = dr.find_element(By.XPATH, '//span[text() = "right click me"]')
    act.context_click(right).perform()

    ele = dr.find_elements(By.XPATH, '//ul[@class="context-menu-list context-menu-root"]/li')
    for i in ele:
        if i.text == "":
            continue
        i.click()
        sleep(1)
        alt = dr.switch_to.alert
        print(alt.text)
        alt.accept()
        sleep(1)
        act.context_click(right).perform()
        sleep(1)

sleep(1)
dr.quit()
