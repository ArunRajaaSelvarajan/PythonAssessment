from selenium.webdriver.common.by import By


class CandidatesPage():

    def __init__(self, driver):
        self.driver = driver

    contenttxa = (By.XPATH, "//div[@id='content']//div/h1")
    tablerow = (By.XPATH, "//table[@id='resultTable']/tbody/tr")

    def content(self):
        return self.driver.find_element(*CandidatesPage.contenttxa)

    def tableRow(self):
        return self.driver.find_elements(*CandidatesPage.tablerow)