from pages.Base_page import BasePage
from locators.Main_page_locators import MainPageLocators


class MainPage(BasePage):

    def main_page(self):
        self.open_main_page()

    def find_all_pictures_data(self, browser):
        picture_data = browser.find_element_by_css_selector('small.text-muted')
        data_text = [el.text for el in picture_data]
        return data_text

    def search_admin_button(self):
        field = self.find_element(MainPageLocators.GO_TO_ADMIN)
        return field

    def text_admin_button(self):
        field = self.search_admin_button()
        return field.text
