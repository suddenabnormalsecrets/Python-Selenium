import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Fixtures_using_POM.Home_page import Home
from Fixtures_using_POM.Info import My_Info


@pytest.fixture()
def my_info(setup):

    dr = webdriver.Chrome()
    home = Home(dr)
    info = My_Info(dr)
    act = ActionChains(dr)

    home.info_click()
    info.first()
    act.double_click().click().perform()
    # info.first('Mo')