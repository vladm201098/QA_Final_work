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
        executable_path="/home/vladislav/QA_Final_work/tests/chromedriver",
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

@pytest.fixture()
def groups_page(browser):
    login_page = LoginPage(browser)
    login_page.login(username_adm, password)
    groups_page = GroupsPage(browser)
    groups_page.open_groups_page()
    yield groups_page


@pytest.fixture()
def add_user_page(browser):
    add_user_page = User_add_page(browser)
    add_user_page.open_add_user_page()
    yield add_user_page


@pytest.fixture()
def log_in_new_user(browser):
    user_page = User_Page_Logout(browser)
    user_page.click_logout_field()
    login_page = LoginPage(browser)
    login_page.open_login_page()
    login_page.login(new_username, new_password)
    admin_page = WelcomePage(browser)
    admin_page.open_admin_page()
    yield admin_page
    browser.quit()


@pytest.fixture(scope="class")
def posts_page(browser):
    posts_page = PostsPage(browser)
    posts_page.open_posts_page()
    yield posts_page
    browser.quit()
