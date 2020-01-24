import pytest
from selenium import webdriver
import time


def pytest_adoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="/Users/madinaochilova/Downloads/chromedriver")
        driver.maximize_window()
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="/Users/madinaochilova/Downloads/geckodriver")
    elif browser_name == "IE":
        print("IE driver")
        driver = webdriver.Ie(executable_path="/Users/madinaochilova/Downloads/chromedriver")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture()
def dataLoad():
    print("User profile data is created")
    return ["Rahul", "Shetty", "rahulshettyacademy.com"]


@pytest.fixture(params=["Chrome", "Firefox", "IE"])
def crossBrowser(request):  # request belongs fixture. request is like an object
    return request.param