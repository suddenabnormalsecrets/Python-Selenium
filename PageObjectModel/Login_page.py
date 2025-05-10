from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from PageObjectModel.LoginPage import Login
from PageObjectModel.Home_page import Home
from PageObjectModel.Admin_page import Admin

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)
dr = webdriver.Chrome(options=opt)
act = ActionChains(dr)
exp_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
dr.maximize_window()
dr.implicitly_wait(10)
dr.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

log = Login(dr)
home_page = Home(dr)
admin_page = Admin(dr)

log.send_username('Admin')
sleep(1)
log.send_password('admin123')
sleep(1)
log.login_click()
sleep(1)


act_url = dr.current_url
assert act_url == exp_url, 'Login Unsuccessful'
print("Login Successful")


home_page.admin_click()
sleep(1)


admin_page.adda()
sleep(1)

admin_page.user()
act.key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
sleep(1)
dup = 'https://www.orangehrm.com/'
ax = dr.current_url
if ax == dup:
    sleep(2)
    dr.back()
    # sleep(1)
    # dr.back()
sleep(2)

admin_page.stat()
act.key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
if dup == ax:
    sleep(1)
    dr.back()
    # sleep(1)
    # dr.back()
sleep(1)

admin_page.emp()
sleep(1)

admin_page.send_emp('Monkey D. Luffy')
sleep(3)

# sleep(1)

act.key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
sleep(1)

admin_page.send_username('Gol.D.Asce')
sleep(1)

admin_page.send_password('Demo@0907')
sleep(2)

admin_page.send_conf_password('Demo@0907')
sleep(1)

admin_page.click_save()
sleep(5)

home_page.user_log()
sleep(1)

home_page.log_out()
sleep(3)

# dr.quit()