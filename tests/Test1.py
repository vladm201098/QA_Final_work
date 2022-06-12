'''
TC_1:
    1. Создать группу в bd
    2. Открыть приложение
    3. Войти в админку
    4. Проверить, что группа отображается
'''
from selenium import webdriver
from configs.config_parser import username_adm, password_adm, name_group, go_to_admin, welcome_admin
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
        assert open_page.text_admin_button == go_to_admin

    def test_login_to_admin(self, browser):
        open_page = LoginPage(browser)
        open_page.open_login_page()
        open_page.login(username_adm, password_adm)
        check_admin_pages = AdminPage(browser)
        result_browser = check_admin_pages.check_admin_page()
        assert result_browser == welcome_admin

    def test_check_new_group(self, browser):
        group_page = GroupsPage(browser)
        group_page.open_group_page()
        group_page.check_status_new_group()
        element = group_page.check_fill_field_page()
        assert name_group == element
