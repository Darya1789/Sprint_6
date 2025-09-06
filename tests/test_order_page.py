from mailbox import MaildirMessage
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
# import locators
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
# from locators.dzen_page_locators import DzenPageLocators

from pages import dzen_page
from pages.main_page import MainPage
import urls
from pages.order_page import OrderPage
# from pages.dzen_page import DzenPage

from data import ExpectedTest, Data

class TestOrder():
    driver = None
    
    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Firefox()
        

    @allure.title('Проверка позитивного сценария заказа самоката для первого юзера') # декораторы
    @allure.description('Проверяем заказ самоката для первого юзера при нажатии на кнопку заказать в заголовке')
    
    def test_order(self):
        order_page = OrderPage(self.driver)
        main_page = MainPage(self.driver)
        main_page.open_page(urls.main_page)
        locator_order_btn = MainPageLocators.button_order_in_header
        user = Data.user_1
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


    @allure.title('Проверка позитивного сценария заказа самокатадля второго юзера') # декораторы
    @allure.description('Проверяем заказ самоката для второго юзера при нажатии на кнопку заказать на странице')
    def test_order_2(self):
        order_page = OrderPage(self.driver)
        main_page = MainPage(self.driver)
        main_page.open_page(urls.main_page)
        locator_order_btn = MainPageLocators.button_order_in_page
        user = Data.user_2
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
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit() 