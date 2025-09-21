import allure
from selenium import webdriver
from locators.main_page_locators import MainPageLocators
import urls
from pages.main_page import MainPage
from pages.dzen_page import DzenPage

class TestMain():
    driver = None
    
    @classmethod
    def setup_method(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Firefox()
        

    @allure.title('Проверка открытия страницы Дзена при нажатии на логотип Яндекс') # декораторы
    @allure.description('Проверяем редирект на главную страницу Дзена в новой вкладке при нажатиии на логотип Яндекс')
    def test_logo_yandex(self):
        main_page = MainPage(self.driver)
        dzen_page = DzenPage(self.driver)
        main_page.open_page(urls.main_page)
        order_locator = MainPageLocators.button_order_in_header
        main_page.click_btn_order(order_locator)
        main_page.wait_visible_logo_yandex()
        main_page.click_logo_yandex()
        main_page.swich_tab()
        main_page.wait_url_contain(urls.dzen_page)
        assert dzen_page.check_element_main_in_navigation_tab()


    @allure.title('Проверка открытия страницы Самоката при нажатии на логотип Самокат') # декораторы
    @allure.description('Проверяем открытие главной страницы Самоката при нажатиии на логотип Самоката')
    def test_logo_scooter(self):
        main_page = MainPage(self.driver)
        main_page.open_page(urls.main_page)
        order_locator = MainPageLocators.button_order_in_header
        main_page.click_btn_order(order_locator)
        main_page.wait_visible_logo_scooter()
        main_page.click_logo_scooter()
        main_page.wait_url_contain(urls.main_page)
        assert main_page.check_text_scooter_in_main_page()

    
    @classmethod
    def teardown_method(cls):
        # закрыли браузер
        cls.driver.quit() 