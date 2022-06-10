from locators.Groups_page_locators import GroupsPageLocators
from pages.Base_page import BasePage


class GroupsPage(BasePage):

    group_url = BasePage.main_url + '/admin/auth/group/'

    def open_group_page(self):
        self.open(self.group_url)

    def find_add_group_field(self):
        field = self.find_element(GroupsPageLocators.ADD_GROUP)
        return field

    def click_add_group_field(self):
        field = self.find_add_group_field()
        field.click()
        return field

    def find_name_field(self):
        field = self.find_element(GroupsPageLocators.NAME_GROUP)
        return field

    def fill_name_field(self):
        field = self.find_name_field()
        field.send_keys(username)
        return field

    def find_username_fild(self):
        field = self.find_element(UserPageLocators.USERNAME)
        return field

    def fill_username_field(self, username):
        field = self.find_username_fild()
        field.send_keys(username)
        return field
