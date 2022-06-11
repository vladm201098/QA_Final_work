from selenium.webdriver.common.by import By


class GroupsPageLocators:

    # GROUP
    GROUP_LINK = (By.XPATH, '//*[@id="content-main"]/div[2]/table/tbody/tr[1]/th/a')
    ADD_GROUP = (By.XPATH, '//*[@id="content-main"]/ul/li/a')
    NAME_GROUP = (By.XPATH, '//*[@id="id_name"]')
    SAVE_GROUP = (By.XPATH, '//*[@id="group_form"]/div/div/input[1]')
    # ВОЗМОЖНО НУЖНО ПОМЕНЯТЬ - УКАЗАН КОНКРЕТНЫЙ ПОЛЬЗОВАТЕЛЬ
    CHECK_NEW_GROUP = (By.XPATH, '//*[@id="result_list"]/tbody/tr/th/a')
    FILLED_NAME_GROUP = (By.NAME, 'name')

