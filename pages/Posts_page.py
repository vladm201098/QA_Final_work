from pages.Base_page import BasePage
from locators.Posts_page_locators import PostsPageLocators


class PostsPage(BasePage, PostsPageLocators):

    posts_url = BasePage.main_url + '/admin/app/post/'

    def open_posts_page(self):
        self.open(self.posts_url)

    def find_post_object_field(self):
        field = self.find_element(PostsPageLocators.POSTS_OBJECT_1)
        return field

    def click_post_object_field(self):
        field = self.find_post_object_field()
        field.click()
        return field

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
        self.click_post_object_field()
        self.click_delete_field()
        self.click_sure_field()
