import pytest
from selenium import webdriver


@pytest.fixture(scope="session", name="driver")
def browser():
    '''定义一个打开浏览器的fixture'''
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()  # 退出浏览器


@pytest.fixture(scope="session")
def base_url():
    url = "http://124.70.221.221:8200"
    return url


