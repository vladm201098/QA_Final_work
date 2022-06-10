from selenium.webdriver.common.by import By



class LoginPageLocators:

    USERNAME_ADMIN = (By.NAME, 'username')
    PASSWORD_ADMIN = (By.NAME,'password')
    SUBMIT = (By.XPATH, '//*[@id="login-form"]/div[3]/input')
