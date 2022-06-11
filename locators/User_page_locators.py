from selenium.webdriver.common.by import By


class UserPageLocators:

    # USER
    USER_LINK = (By.XPATH, '//*[@id="content-main"]/div[2]/table/tbody/tr[2]/th/a')
    ADD_USER = (By.XPATH, '//*[@id="content-main"]/ul/li/a')
    USERNAME = (By.CLASS_NAME, 'vTextField')
    PASSWORD = (By.XPATH, '//*[@id="id_password1"]')
    PASSWORD_CONFIRM = (By.XPATH, '//*[@id="id_password2"]')
    APPLY_USER = (By.NAME, 'save')
    GIVE_STAFF_STATUS = (By.XPATH, '//*[@id="user_form"]/div/fieldset[3]/div[2]/div/label')

    # ДОБАЛЕНИЕ ПОЛЬЗОВАТЕЛЯ В ГРУППУ
    ADD_USER_TO_GROUP = (By.XPATH, '//*[@id="id_groups_add_all_link"]')

    EMPTY_SPASE = (By.XPATH, '//*[@id="id_groups_from"]')  # НУЖНО ПРОВЕРИТЬ ЧТО ЭТО ПОЛЕ ПУСТОЕ

    SAVE_USER = (By.XPATH, '//*[@id="user_form"]/div/div/input[1]')
    # ВОЗМОЖНО НУЖНО ПОМЕНЯТЬ - УКАЗАН КОНКРЕТНЫЙ ПОЛЬЗОВАТЕЛЬ
    CHECK_NEW_USER = (By.XPATH, '//*[@id="result_list"]/tbody/tr[2]/th/a')
    CHECK_NEW_USER_FIELD = (By.NAME, 'username')

    # Common

    LOG_OUT = (By.XPATH, '//*[@id="user-tools"]/a[3]')
