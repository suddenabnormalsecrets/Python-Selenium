from seleniumpagefactory.Pagefactory import PageFactory


class Home(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {'my_info': ('xpath', '//span[text()="My Info"]'),
               'user': ("XPATH", '//span[@class="oxd-userdropdown-tab"]'),
               'logout': ("LINK_TEXT", 'Logout')}

    def info_click(self):
        self.my_info.click()

    def user_log(self):
        self.user.click()

    def log_out(self):
        self.logout.click()
