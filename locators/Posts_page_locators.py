from selenium.webdriver.common.by import By


class PostsPageLocators:

    # POSTS
    POSTS_LINK = (By.XPATH, '//*[@id="content-main"]/div[1]/table/tbody/tr/th/a')
    DELETE_OBJECT = (By.CLASS_NAME, 'deletelink')
    SURE_BUTTON = (By.XPATH, '//*[@id="content"]/form/div/input[2]')
    # POST_1_ON_MAINPAGE = (By.XPATH, '/html/body/main/div/div/div/div[25]/div/div/div/small')
    POST_1_ON_MAINPAGE = (By.XPATH, '/html/body/main/div/div/div/div[25]/div/div/div/small')