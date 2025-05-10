from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep


def test_bankai():
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option('detach', True)
    exp_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    dr = webdriver.Chrome(options=opt)
    dr.maximize_window()
    act = ActionChains(dr)
    dr.implicitly_wait(10)
    dr.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    act_url = dr.current_url
    assert exp_url == act_url, 'i am not in HRM'
    print('i am in HRM')
    dr.find_element(By.NAME, 'username').send_keys('Admin')
    sleep(1)
    dr.find_element(By.NAME, 'password').send_keys('admin123')
    sleep(1)
    dr.find_element(By.XPATH, "//button[text() = ' Login ']").click()
    sleep(3)
    dr.find_element(By.XPATH, '//nav[@class="oxd-navbar-nav"]/div[2]//li[1]/a').click()
    sleep(1)
    dr.find_element(By.XPATH, '//div[@class="orangehrm-header-container"]/button').click()
    sleep(1)
    dr.find_element(By.XPATH, '//div[@class="oxd-select-text-input"]').click()
    act.key_up(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
    dr.find_element(By.XPATH, "//div[@class='orangehrm-header-container']/button").click()
    dr.find_element(By.XPATH, "//div[@class='oxd-select-text-input']").click()
    sleep(2)
    ActionChains(dr)
    act.key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
    dr.find_element(By.XPATH, "(//div[@class='oxd-select-text-input']) [2]").click()
    sleep(2)
    act.key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
    dr.find_element(By.XPATH, "//input[@type='password']").send_keys("manu2305")
    dr.find_element(By.XPATH, "//input[@placeholder='Type for hints...']").send_keys("payal")
    sleep(2)
    act.key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
    dr.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]").send_keys("samruddhi")
    dr.find_element(By.XPATH, "(//input[@type='password']) [2]").send_keys("manu2305")
    dr.find_element(By.XPATH, "//button[@type='submit']").click()
