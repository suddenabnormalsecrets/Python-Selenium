from seleniumpagefactory.Pagefactory import PageFactory


class My_Info(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {'first_name': ('XPATH', '//input[@placeholder="First Name"]'),
                'middle_name': ('XPATH', '//input[@placeholder="Middle Name"]'),
                'last_name': ('XPATH', '//input[@placeholder="Last Name"]'),
                'emp_id': ('XPATH', '(//input[@class="oxd-input oxd-input--active"])[2]'),
                'male': ('XPATH', '//label[text()="Male"]'),
                'submit': ('XPATH', '//button[text()=" Save "]')}

    def first(self, data):
        self.first_name.click()
        self.first_name.send_keys(data)

    def mid(self, data):
        self.middle_name.click()
        self.middle_name.send_keys(data)

    def last(self, data):
        self.last_name.click()
        self.last_name.send_keys(data)

    def id(self, data):
        self.emp_id.click()
        self.emp_id.send_keys(data)

    def gender(self):
        self.male.click()

    def send(self):
        self.submit.click()