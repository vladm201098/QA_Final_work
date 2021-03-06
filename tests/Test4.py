'''
TC_4:
    1. Открыть приложение
    2. Войти в админку
    3. Удалить первое созданное изображение
    4. Вернуться на главную страницу
    5. Убедиться, что первое изображение не отображается на странице
'''
from configs.config_parser import username_adm, password_adm, go_to_admin, welcome_admin, datetime, default_post
from pages.Login_page import LoginPage
from pages.Main_page import MainPage
from pages.Posts_page import PostsPage
from pages.Admin_page import AdminPage
import allure
import pytest


class Test3:

    @allure.feature('TC_2')
    @allure.story('Открытие главной страницы')
    @pytest.mark.positive
    def test_open_django_project(self, browser):
        open_page = MainPage(browser)
        open_page.open_main_page()
        assert open_page.current_url() == open_page.main_url

    @allure.story('Логин в админку')
    @pytest.mark.positive
    def test_login_to_admin(self, browser):
        open_page = LoginPage(browser)
        open_page.open_login_page()
        result = AdminPage(browser)
        open_page.login(username_adm, password_adm)
        assert open_page.current_url() == result.admin_url

    @allure.story('Тест удаления изображения')
    @pytest.mark.positive
    def test_delete_first_img(self, browser):
        delete_img = PostsPage(browser)
        delete_img.open_posts_page()
        delete_img.delete_first_pic()
        assert delete_img.current_url() == default_post

    @allure.story('Открытие главной страницы')
    @pytest.mark.positive
    def test_open_django_project_2(self, browser):
        open_page = MainPage(browser)
        open_page.open_main_page()
        assert open_page.current_url() == open_page.main_url

    @allure.story('Тест то что изображение было удалено с главной страницы')
    @pytest.mark.positive
    def test_check_deleted_first_img(self, browser):
        main_page = MainPage(browser)
        main_page.open_main_page()
        all_pic_data = main_page.find_all_pictures_data()
        assert datetime not in all_pic_data



