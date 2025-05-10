from seleniumpagefactory.Pagefactory import PageFactory


class Home(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {'admin': ('xpath', '//span[text()="Admin"]'),
               'user': ("XPATH", '//span[@class="oxd-userdropdown-tab"]'),
               'logout': ("LINK_TEXT", 'Logout')}

    def admin_click(self):
        self.admin.click()

    def user_log(self):
        self.user.click()

    def log_out(self):
        self.logout.click()
