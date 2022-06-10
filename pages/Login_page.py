from locators.Login_page_locators import LoginPageLocators
from pages.Base_page import BasePage


class LoginPage(BasePage):

    login_url = BasePage.main_url + '/admin/login/?next=/admin/'

    def open_login_page(self):
        self.open(self.login_url)

    # Admin
    def get_username_field(self):
        field = self.find_element(LoginPageLocators.USERNAME_ADMIN)
        return field

    def fill_username_field(self, username_adm):
        field = self.get_username_field()
        field.send_keys(username_adm)
        return field

    def get_password_field(self):
        field = self.find_element(LoginPageLocators.PASSWORD_ADMIN)
        return field

    def fill_password_field(self, password_adm):
        field = self.get_password_field()
        field.send_keys(password_adm)
        return field

    def get_submit_field(self):
        field = self.find_element(LoginPageLocators.SUBMIT)
        return field

    def click_submit_field(self):
        field = self.get_submit_field()
        field.click()
        return field

    def login(self, username_adm, password_adm):
        self.fill_username_field(username_adm)
        self.fill_password_field(password_adm)
        self.click_submit_field()
        return
