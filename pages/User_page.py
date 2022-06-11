from locators.User_page_locators import UserPageLocators
from pages.Base_page import BasePage


class UserPage(BasePage):

    user_page = BasePage.main_url + '/admin/auth/user/'

    def open_user_page(self):
        self.open(self.user_page)

    def find_logout_field(self):
        field = self.find_element(UserPageLocators.LOG_OUT)
        return field

    def click_logout_field(self):
        field = self.find_logout_field()
        field.click()
        return field


class AddUserPage(BasePage):

    add_user_page = BasePage.main_url + '/admin/auth/user/add'

    def open_add_user_page(self):
        self.open(self.add_user_page)

    def find_username_fild(self):
        field = self.find_element(UserPageLocators.USERNAME)
        return field

    def fill_username_field(self, username_user):
        field = self.find_username_fild()
        field.send_keys(username_user)
        return field

    def find_password_field(self):
        field = self.find_element(UserPageLocators.PASSWORD)
        return field

    def fill_password_field(self,password_user):
        field = self.find_password_field()
        field.send_keys(password_user)
        return field

    def find_confirm_passwd_field(self):
        field = self.find_element(UserPageLocators.PASSWORD_CONFIRM)
        return field

    def fill_confirm_passwd_field(self, password_user):
        field = self.find_confirm_passwd_field()
        field.send_keys(password_user)
        return field

    def find_staff_field(self):
        field = self.find_element(UserPageLocators.GIVE_STAFF_STATUS)
        return field

    def click_staff_field(self):
        field = self.find_staff_field()
        field.click()
        return field

    def add_to_group_field(self):
        field = self.find_element(UserPageLocators.ADD_USER_TO_GROUP)
        return field

    def click_add_to_group_field(self):
        field = self.add_to_group_field()
        field.click()
        return field

    def find_save_field(self):
        field = self.find_element(UserPageLocators.SAVE_USER)
        return field

    def click_save_field(self):
        field = self.find_save_field()
        field.click()
        return field

    def user_creation(self, username_user, password_user):
        self.fill_username_field(username_user)
        self.fill_password_field(password_user)
        self.fill_confirm_passwd_field(password_user)
        self.click_save_field()
        self.click_staff_field()
        self.click_add_to_group_field()
        self.click_save_field()