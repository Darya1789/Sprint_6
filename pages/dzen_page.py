import allure
from locators.dzen_page_locators import DzenPageLocators
from pages.base_page import BasePage


class DzenPage(BasePage):

    @allure.step("Ожидаем загрузки Кнопки 'Главная'")
    def wait_visible_main_navigation_tab(self):
        return self.wait_of_visible_element(DzenPageLocators.button_main_navigation_tab)
    
    @allure.step("Получаение текст кнопки 'Главная")
    def get_text_from_main_navigation_tab(self, locator):
        return self.get_text_from_element(locator)

    
    @allure.step('Проверка отображения кнопки "Главная" на странице DZEN')
    def check_element_main_in_navigation_tab(self):
        return self.wait_until_present(DzenPageLocators.button_main_navigation_tab, timeout=5)