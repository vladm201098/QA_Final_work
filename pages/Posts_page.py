from pages.Base_page import BasePage
from locators.Posts_page_locators import PostsPageLocators


class PostsPage(BasePage, PostsPageLocators):

    posts_url = BasePage.main_url + 'admin/app/post/5/change/'

    def open_posts_page(self):
        self.open(self.posts_url)

    def find_delete_field(self):
        field = self.find_element(PostsPageLocators.DELETE_OBJECT)
        return field

    def click_delete_field(self):
        field = self.find_delete_field()
        field.click()
        return field

    def find_sure_field(self):
        field = self.find_element(PostsPageLocators.SURE_BUTTON)
        return field

    def click_sure_field(self):
        field = self.find_sure_field()
        field.click()
        return field

    def delete_first_pic(self):
        self.click_delete_field()
        self.click_sure_field()

    def check_deleted_img(self):
        img = self.find_element(PostsPageLocators.POST_1_ON_MAINPAGE)
        if img is True:
            return img
        else:
            return 0
