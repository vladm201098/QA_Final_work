from pages.Base_page import BasePage


class AdminPage(BasePage):

    admin_url = BasePage.main_url + 'admin/'

    def open_main_page(self):
        self.open(self.admin_url)
