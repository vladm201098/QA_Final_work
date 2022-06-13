'''
TC_1:
    1. Создать группу в bd
    2. Открыть приложение
    3. Войти в админку
    4. Проверить, что группа отображается
'''
from configs.config_parser import username_adm, password_adm, name_group
from pages.Login_page import LoginPage
from pages.Main_page import MainPage
from pages.Groups_page import GroupsPage
from pages.Admin_page import AdminPage


import allure
import pytest


class Test1:

    def test_open_django_project(self, browser):
        open_page = MainPage(browser)
        open_page.open_main_page()
        assert open_page.current_url() == open_page.main_url

    def test_login_to_admin(self, browser):
        open_page = LoginPage(browser)
        result = AdminPage(browser)
        open_page.open_login_page()
        open_page.login(username_adm, password_adm)
        assert open_page.current_url() == result.admin_url

    def test_group_create(self, browser):
        group_page = GroupsPage(browser)
        group_page.open_group_page()
        group_page.group_creation(name_group)
        assert group_page.current_url() == group_page.group_url
