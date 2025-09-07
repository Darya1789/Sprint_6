from selenium.webdriver.common.by import By


class MainPageLocators():

    button_order_in_header = (By.XPATH, ".//div[@class = 'Header_Nav__AGCXC']/button[text() = 'Заказать']")
    button_order_in_page = (By.XPATH, ".//div[@class = 'Home_FinishButton__1_cWm']/button[text() = 'Заказать']")
    logo_yandex = (By.XPATH, ".//div[@class = 'Header_Logo__23yGT']/a[@class = 'Header_LogoYandex__3TSOI']")
    logo_scooter = (By.XPATH, ".//div[@class = 'Header_Logo__23yGT']/a[@class = 'Header_LogoScooter__3lsAR']")
    text_scooter_in_main_page = (By.XPATH, ".//div[@class='Home_Header__iJKdX']")
    accept_cookies_button = (By.XPATH, ".//button[@id = 'rcc-confirm-button']")
