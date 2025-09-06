import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Открываем страницу url: {page}")
    def open_page(self, page):
        self.driver.get(page)

    @allure.step("Ждем загрузки логотипа Яндекс")
    def wait_visible_logo_yandex(self):
        return self.wait_of_visible_element(MainPageLocators.logo_yandex)
    
    @allure.step("Ждем загрузки логотипа Самокат")
    def wait_visible_logo_scooter(self):
        return self.wait_of_visible_element(MainPageLocators.logo_scooter)
    
    @allure.step("Нажимаем на логотип Самокат")
    def click_logo_scooter(self):
        self.click_on_element(MainPageLocators.logo_scooter)

    @allure.step("Нажимаем на логотип Яндекс")
    def click_logo_yandex(self):
        self.click_on_element(MainPageLocators.logo_yandex)

    @allure.step("Проверка текста Самокат на главной странице самоката")
    def check_text_scooter_in_main_page(self):
        return self.wait_until_present(MainPageLocators.text_scooter_in_main_page).is_displayed()
    
    @allure.step("Нажимаем на кнопку заказать")
    def click_btn_order(self, locator_btn):
        self.click_on_element(locator_btn)

    @allure.step("Подтверждаем куки")
    def accept_cookie(self):
        self.click_on_element(MainPageLocators.accept_cookies_button)


 