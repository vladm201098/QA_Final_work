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

    def fill_name_field(self, name_group):
        field = self.find_name_field()
        field.send_keys(name_group)
        return field

    def find_save_group_field(self):
        field = self.find_element(GroupsPageLocators.SAVE_GROUP)
        return field

    def click_save_field(self):
        field = self.find_save_group_field()
        field.click()
        return field

    def group_creation(self, name_group):
        self.click_add_group_field()
        self.fill_name_field(name_group)
        self.click_save_field()

    def find_new_group_page(self):
        field = self.find_element(GroupsPageLocators.CHECK_NEW_GROUP)
        return field

    def click_new_group_page(self):
        field = self.find_new_group_page()
        field.click()
        return field

    def check_fill_field_page(self):
        field = self.find_element(GroupsPageLocators.FILLED_NAME_GROUP)
        return field

    def check_status_new_group(self):
        self.find_new_group_page()
        self.click_new_group_page()
        self.check_fill_field_page()
