from selenium.webdriver.common.by import By


class PostsPageLocators:

    # POSTS
    POSTS_LINK = (By.XPATH, '//*[@id="content-main"]/div[1]/table/tbody/tr/th/a')
    POSTS_OBJECT_1 = (By.XPATH, '//*[@id="result_list"]/tbody/tr[17]/th/a')  # НАЙТИ ЕГО И КЛИКНУТЬ
    DELETE_OBJECT = (By.CLASS_NAME, 'deletelink')
    SURE_BUTTON = (By.XPATH, '//*[@id="content"]/form/div/input[2]')
