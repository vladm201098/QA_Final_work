'''
TC_4:
    1. Открыть приложение
    2. Войти в админку
    3. Удалить первое созданное изображение
    4. Вернуться на главную страницу
    5. Убедиться, что первое изображение не отображается на странице
'''
from configs.config_parser import username_adm, password_adm, go_to_admin, welcome_admin
from pages.Login_page import LoginPage
from pages.Main_page import MainPage
from pages.Posts_page import PostsPage
from pages.Admin_page import AdminPage


class Test3:

    def test_open_django_project(self, browser):
        open_page = MainPage(browser)
        open_page.open_main_page()
        assert open_page.current_url() == 'http://localhost:8000/'

    def test_login_to_admin(self, browser):
        open_page = LoginPage(browser)
        open_page.open_login_page()
        open_page.login(username_adm, password_adm)
        assert open_page.current_url() == 'http://localhost:8000/admin/'

    def delete_first_img(self, browser):
        delete_img = PostsPage(browser)
        delete_img.delete_first_pic()
        assert delete_img.find_post_object_field is True

    def test_open_django_project_2(self, browser):
        open_page = MainPage(browser)
        open_page.open_main_page()
        assert open_page.text_admin_button == go_to_admin

    def check_deleted_first_img(self,browser):
        check_deleted = PostsPage(browser)
        check = check_deleted.check_deleted_img()
        assert check == 0


