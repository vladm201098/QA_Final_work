'''
TC_3:
    1. Открыть приложение
    2. Войти в админку
    3. Создать пользователя - пропускаем
    4. Проверить что пользователь создан
    5. Выйти из приложение
    6. Войти как созданный пользователь
    7. Проверить, что приложение открылось
'''

from configs.config_parser import username_adm, password_adm, password_user, username_user, logout_text, welcome_user
from pages.Login_page import LoginPage
from pages.Main_page import MainPage
from pages.Admin_page import AdminPage
from pages.User_page import UserPage


class Test2:

    def test_open_django_project(self, browser):
        # Login
        open_page = MainPage(browser)
        open_page.open_main_page()
        # assert

    def test_login_to_admin(self, browser):
        open_page = LoginPage(browser)
        open_page.open_login_page()
        open_page.login(username_adm, password_adm)
        # assert на то что мы на админ странице

    def test_logout_djando_project(self, browser):
        logout_user = UserPage(browser)
        logout_user.logout()
        text = logout_user.find_logged_text()
        assert logout_text == text

    def test_login_to_user(self, browser):
        open_page = LoginPage(browser)
        open_page.open_login_page()
        open_page.login(username_user, password_user)
        # assert на то что мы на юзер странице

    def check_admin_page(self, browser):
        check_open = AdminPage(browser)
        text_from_page = check_open.check_admin_page()
        assert text_from_page == welcome_user

