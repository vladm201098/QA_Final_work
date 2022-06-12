'''
TC_4:
    1. Открыть приложение
    2. Войти в админку
    3. Удалить первое созданное изображение
    4. Вернуться на главную страницу
    5. Убедиться, что первое изображение не отображается на странице
'''

from configs.config_parser import username_adm, password_adm, password_user, username_user, logout_text, welcome_user
from pages.Login_page import LoginPage
from pages.Main_page import MainPage
from pages.Admin_page import AdminPage
from pages.Posts_page import PostsPage


class Test3:

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

    def delete_first_img(self,browser):
        delete_img = PostsPage(browser)
        delete_img.delete_first_pic()

