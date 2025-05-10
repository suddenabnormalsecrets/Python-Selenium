from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

dr = webdriver.Chrome(options=opt)
dr.maximize_window()
dr.implicitly_wait(15)
# a = ActionChains(dr)

dr.get('https://demoapps.qspiders.com/ui?scenario=1')
dr.find_element(By.XPATH, '//section[text() = "Popups"]').click()
dr.find_element(By.XPATH, '//section[text()= "Browser Windows"]').click()
dr.find_element(By.ID, 'browserLink1').click()
b = dr.window_handles
# print(b)
dr.switch_to.window(b[1])

dr.find_element(By.ID, 'email').send_keys('Teddy Bear')
dr.find_element(By.ID, 'password').send_keys('Chavhan@25')
dr.find_element(By.ID, 'confirm-password').send_keys('Chavhan@25')
dr.find_element(By.XPATH, '//button[@type="submit"]').click()

dr.close()
dr.switch_to.window(b[0])
dr.find_element(By.LINK_TEXT, 'New Tab').click()
dr.find_element(By.ID, 'browserButton4').click()

c = dr.window_handles
# print(c)
dr.switch_to.window(c[1])

dr.find_element(By.ID, 'email').send_keys('Teddy Bear')
dr.find_element(By.ID, 'password').send_keys('Pranay@25')
dr.find_element(By.ID, 'confirm-password').send_keys('Pranay@25')
dr.find_element(By.XPATH, '//button[@type="submit"]').click()

dr.close()
dr.switch_to.window(c[0])
dr.find_element(By.LINK_TEXT, 'Multiple Windows').click()
dr.find_element(By.ID, 'browserButton3').click()
parent = dr.current_window_handle

hand = dr.window_handles
print(hand)

sign_up_page = 'https://demoapps.qspiders.com/ui/browser/SignUpPage'

for i in range(1, len(hand)):
    dr.switch_to.window(hand[i])
    sleep(1)

    if dr.current_url == sign_up_page:
        dr.find_element(By.ID, 'email').send_keys('TeddyBear0907@gmail.com')
        sleep(1)
        dr.find_element(By.ID, 'password').send_keys('demo@123')
        sleep(1)
        dr.find_element(By.ID, 'confirm-password').send_keys('demo@123')
        sleep(1)
        dr.find_element(By.XPATH, '//button[@type="submit"]').click()
        sleep(2)
        dr.close()

sign_up = 'https://demoapps.qspiders.com/ui/browser/SignUp'

for i in range(1, len(hand)):
    dr.switch_to.window(hand[i])
    sleep(1)

    if dr.current_url == sign_up:

        dr.find_element(By.ID, 'username').send_keys('Teddy Bear')
        sleep(1)
        dr.find_element(By.ID, 'email').send_keys('TeddyBear0907@gmail.com')
        sleep(1)
        dr.find_element(By.ID, 'password').send_keys('demo@123')
        sleep(1)
        dr.find_element(By.XPATH, '//button[@type="submit"]').click()
        sleep(2)
        dr.close()

dr.switch_to.window(hand[0])

log_in = 'https://demoapps.qspiders.com/ui/browser/Login'

if dr.current_url == log_in:
    dr.find_element(By.ID, 'username').send_keys('Teddy Bear')
    sleep(1)
    dr.find_element(By.ID, 'password').send_keys('demo@123')
    sleep(1)
    dr.find_element(By.XPATH, '//button[@type="submit"]').click()
    sleep(2)
    dr.close()

dr.switch_to.window(hand[0])

dr.find_element(By.LINK_TEXT, 'Multiple Tabs').click()