from selenium.webdriver.common.by import By


class LandingPage():

    def __init__(self, driver):
        self.driver = driver

    contenttxa = (By.XPATH, "//div[@id='content']//div/h1")
    recruitmentlnk = (By.CSS_SELECTOR, "a[id='menu_recruitment_viewRecruitmentModule']")
    candidateslnk = (By.CSS_SELECTOR, "a[id='menu_recruitment_viewCandidates']")

    def content(self):
        return self.driver.find_element(*LandingPage.contenttxa)

    def recruitment(self):
        return self.driver.find_element(*LandingPage.recruitmentlnk)

    def candidate(self):
        return self.driver.find_element(*LandingPage.candidateslnk)
