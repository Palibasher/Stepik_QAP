from selenium.webdriver.common.by import By


class MainPageLocators():
    PAGE_URL = "https://selenium1py.pythonanywhere.com/ru/"
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    PAGE_URL = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")