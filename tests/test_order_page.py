import allure
import pytest
from selenium import webdriver
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
import urls
from pages.order_page import OrderPage
from data import Data

class TestOrder():
    driver = None
    
    @classmethod
    def setup_method(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Firefox()
        

    @allure.title('Проверка позитивного сценария заказа самоката для юзера') # декораторы
    @allure.description('Проверяем заказ самоката для юзера при нажатии на кнопку заказать')
    @pytest.mark.parametrize('locator_order_btn, user', [[MainPageLocators.button_order_in_header, Data.user_1], [MainPageLocators.button_order_in_page, Data.user_2]])
    def test_order(self, locator_order_btn, user):
        order_page = OrderPage(self.driver)
        main_page = MainPage(self.driver)
        main_page.open_page(urls.main_page)
        main_page.accept_cookie()
        main_page.scroll_to_element(locator_order_btn)
        main_page.wait_of_visible_element(locator_order_btn)
        
        main_page.click_btn_order(locator_order_btn)
        order_page.wait_main_text_for_order()
        order_page.fill_first_form(user)
        order_page.wait_text_about_order()
        order_page.fill_second_form(user)
        
        order_page.click_yes_button()
        order_page.wait_order_placed()
        assert order_page.check_order_complete()
        
    @classmethod
    def teardown_method(cls):
        # закрыли браузер
        cls.driver.quit() 