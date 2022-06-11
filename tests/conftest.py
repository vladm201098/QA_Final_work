import pytest
from selenium import webdriver

from pages.Admin_page import AdminPage
from pages.Groups_page import GroupsPage
from pages.Login_page import LoginPage
from pages.Main_page import MainPage
from pages.Posts_page import PostsPage
from pages.User_page import UserPage

from configs.config_parser import username_adm, password_adm, username_user, password_user
# Дописать запросы к базе данных на удаление группы/ юзера/

@pytest.fixture(scope= 'class')
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture(scope= 'class')
def login_page(browser):
    login_page = LoginPage(browser)
    login_page.open_login_page()
    yield login_page
    browser.quit()

@pytest.fixture(scope= 'class')
def main_page(browser):
    main_page = MainPage(browser)
    main_page.open_main_page()
    yield main_page
    browser.quit()

@pytest.fixture()
def group_page(browser):
    login_page = LoginPage(browser)
    login_page.open_login_page()
    login_page.login(username_adm, password_adm)
    group_page = GroupsPage(browser)
    group_page.open_group_page()
    yield group_page

@pytest.fixture()
def add_user_page(browser):
    add_user_page = UserPage(browser)
    add_user_page.open_user_page()
    yield add_user_page

@pytest.fixture()
def log_in_user(browser):
    user_page = UserPage(browser)
    user_page.click_logout_field()
    login_page = LoginPage(browser)
    login_page.open_login_page()
    login_page.login(username_user, password_user)
    admin_page = AdminPage(browser)
    admin_page.open_main_page()
    yield admin_page
    browser.quit()

@pytest.fixture()
def posts_page(browser):
    posts_page = PostsPage(browser)
    posts_page.open_posts_page()
    yield posts_page
    browser.quit()

# Вот сюда добавить функции для БД

