from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)
opt.add_argument('--disable-notification')

dr = webdriver.Chrome(options=opt)
dr.maximize_window()
dr.implicitly_wait(10)

dr.get('https://x.com/OnePieceAnime?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor')
sleep(1)

a = dr.find_element(By.XPATH, '//div[@class="css-175oi2r r-1habvwh"]/div/h1')
d = datetime.now()
s = str(d).replace(':', '-')
dr.save_screenshot(f'..//ScrnSht//twitter {s}.png')

dr.quit()   