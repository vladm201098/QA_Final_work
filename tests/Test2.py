'''
TC_2:
    1. Открыть приложение
    2. Войти в админку
    3. Создать пользователя
    4. Добавить созданного пользователя в группу
    5. Проверить, что в базе данных пользователь добавлен в группу
'''


from configs.config_parser import username_adm, password_adm, password_user, username_user
from pages.Login_page import LoginPage
from pages.Main_page import MainPage
from pages.User_page import *
from pages.Admin_page import AdminPage


class Test2:

    def test_open_django_project(self, browser):
        open_page = MainPage(browser)
        open_page.open_main_page()
        assert open_page.current_url() == open_page.main_url

    def test_login_to_admin(self, browser):
        open_page = LoginPage(browser)
        open_page.open_login_page()
        result = AdminPage(browser)
        open_page.login(username_adm, password_adm)
        assert open_page.current_url() == result.admin_url

    def test_create_user(self, browser):
        create_user = AddUserPage(browser)
        create_user.open_add_user_page()
        create_user.user_creation(username_user, password_user)
        result = UserPage(browser)
        assert create_user.current_url() == result.user_page

