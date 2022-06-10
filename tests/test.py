from configs.config_parser import username_adm, password_adm
from pages.Login_page import LoginPage
from pages.Main_page import MainPage
from pages.Posts_page import PostsPage

import allure
import pytest


class TestUI:


    @allure.feature('ui')
    @allure.story('Check first')
    def test_first_pic_is_delete