from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opt)
driver.maximize_window()
driver.get("https://demoapps.qspiders.com/ui?scenario=1")
driver.implicitly_wait(15)

driver.find_element(By.XPATH, "//section[contains(text(),'Popups')]").click()
driver.find_element(By.XPATH, "//section[text()='File Uploads']").click()
file = driver.find_element(By.XPATH, "//input[@id='fileInput']")
file.send_keys("C://Users//PRANAY CHAVHAN//Desktop//selenium notes.pdf'")
sleep(3)
