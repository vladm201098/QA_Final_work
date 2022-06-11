'''
TC_2:
    1. Открыть приложение
    2. Войти в админку
    3. Создать пользователя
    4. Добавить созданного пользователя в группу
    5. Проверить, что в базе данных пользователь добавлен в группу
'''


from configs.config_parser import username_adm, password_adm, name_group
from pages.Login_page import LoginPage
from pages.Main_page import MainPage
from pages.Groups_page import GroupsPage


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

    def test_create_user(self, browser):

