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

from configs.config_parser import username_adm, password_adm, password_user, username_user, logout_text, welcome_user, go_to_admin, welcome_admin
from pages.Login_page import LoginPage
from pages.Main_page import MainPage
from pages.User_page import UserPage
from pages.Admin_page import AdminPage


class Test2:

    def test_open_django_project(self, browser):
        open_page = MainPage(browser)
        open_page.open_main_page()
        assert open_page.current_url() == 'http://localhost:8000/'

    def test_login_to_admin(self, browser):
        open_page = LoginPage(browser)
        open_page.open_login_page()
        open_page.login(username_adm, password_adm)
        assert open_page.current_url() == 'http://localhost:8000/admin/'

    def test_logout_djando_project(self, browser):
        logout_user = UserPage(browser)
        logout_user.logout()
        text = logout_user.find_logged_text()
        assert logout_text == text

    def test_login_to_user(self, browser):
        open_page = LoginPage(browser)
        open_page.open_login_page()
        open_page.login(username_user, password_user)
        check_user_pages = AdminPage(browser)
        result_browser = check_user_pages.check_admin_page()
        assert result_browser == welcome_user

