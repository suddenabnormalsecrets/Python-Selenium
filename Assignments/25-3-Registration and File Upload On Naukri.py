from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)
opt.add_argument('--disable-notifications')

dr = webdriver.Chrome(options=opt)

dr.maximize_window()

z = ActionChains(dr)

dr.get('https://www.naukri.com/')
dr.find_element(By.ID, "register_Layer").click()
sleep(1)
dr.find_element(By.XPATH, '//input[@placeholder="What is your name?"]').send_keys('Pranay Chavhan')
sleep(1)
dr.find_element(By.ID, "email").send_keys('pranaych007@gmail.com')
z.key_down(Keys.PAGE_DOWN).perform()
sleep(1)
dr.find_element(By.ID, "password").send_keys('Chavhan@25')
sleep(1)
dr.find_element(By.ID, "mobile").send_keys('8767644406')
sleep(1)
dr.find_element(By.XPATH, '(//div[@class="textWrap"])[1]').click()
sleep(1)
resume = dr.find_element(By.ID, "resumeUpload")
resume.send_keys("C:\\Users\\PRANAY CHAVHAN\\Documents\\Resume\\Pranay-Chavhan-Data Analyst.pdf")
sleep(1)
dr.find_element(By.XPATH, "//button[contains(text(),'Register now')]").click()
sleep(5)
# dr.close()