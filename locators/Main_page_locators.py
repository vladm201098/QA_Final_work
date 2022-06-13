from selenium.webdriver.common.by import By


class MainPageLocators:
    GO_TO_ADMIN = (By.CLASS_NAME, 'btn btn-primary my-2')
    SEARCH_IMAGE = (By.XPATH, '/html/body/main/div/div/div/div[1]/div/img')
    DATA_IMAGE = (By.CSS_SELECTOR, 'small.text-muted')
