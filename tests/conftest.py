import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.Login_page import LoginPage

@pytest.fixture(scope='class')
def browser():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(
        executable_path="/home/vladislav/les/my_work/QA_Final_work/chromedriver",
        options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def login_page(browser):
    login_page = LoginPage(browser)
    login_page.open_login_page()
    yield login_page
    browser.quit()
