from selenium.webdriver.common.by import By


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    userNametxa = (By.CSS_SELECTOR, "input[id='txtUsername']")
    passWordtxa = (By.CSS_SELECTOR, "input[id='txtPassword']")
    submitbtn = (By.CSS_SELECTOR, "input[name='Submit']")

    def username(self):
        return self.driver.find_element(*LoginPage.userNametxa)

    def password(self):
        return self.driver.find_element(*LoginPage.passWordtxa)

    def submit(self):
        return self.driver.find_element(*LoginPage.submitbtn)
