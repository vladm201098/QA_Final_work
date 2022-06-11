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

import allure
import pytest


class Test1:

    def test_open_django_project(self, browser):
        # LOgin
        open_page = MainPage(browser)
        open_page.open_main_page()
        # assert

    def test_login_to_admin(self, browser):
        open_page = LoginPage(browser)
        open_page.open_login_page()
        open_page.login(username_adm, password_adm)
        # assert на то что мы на админ странице

    def test_check_new_group(self, browser):
        group_page = GroupsPage(browser)
        group_page.open_group_page()
        group_page.check_status_new_group()
        element = group_page.check_fill_field_page()
        assert name_group == element
