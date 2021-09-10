import os

import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path=os.getcwd() + "/chromedriver")
    driver.implicitly_wait(10)
    driver.get("https://opensource-demo.orangehrmlive.com")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    # driver.close()
