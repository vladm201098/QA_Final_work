'''
TC_2:
    1. Открыть приложение
    2. Войти в админку
    3. Создать пользователя
    4. Добавить созданного пользователя в группу
    5. Проверить, что в базе данных пользователь добавлен в группу
'''


from configs.config_parser import username_adm, password_adm, password_user, username_user, go_to_admin, welcome_admin
from pages.Login_page import LoginPage
from pages.Main_page import MainPage
from pages.User_page import AddUserPage
from pages.User_page import UserPage
from pages.Admin_page import AdminPage


class Test2:

    def test_open_django_project(self, browser):
        open_page = MainPage(browser)
        open_page.open_main_page()
        assert open_page.text_admin_button == go_to_admin

    def test_login_to_admin(self, browser):
        open_page = LoginPage(browser)
        open_page.open_login_page()
        open_page.login(username_adm, password_adm)
        check_admin_pages = AdminPage(browser)
        result_browser = check_admin_pages.check_admin_page()
        assert result_browser == welcome_admin

    def test_create_user(self, browser):
        create_user = AddUserPage(browser)
        create_user.open_add_user_page()
        create_user.user_creation(username_user, password_user)
        test_created_user = UserPage(browser)
        test_created_user.open_user_page()
        test_created_user.find_and_click_new_user()
        element = test_created_user.check_username_info_field()
        assert element == username_user

