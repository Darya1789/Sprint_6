import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Открываем страницу url: {page}")
    def open_page(self, page):
        self.driver.get(page)

    @allure.step("Проверяем вдимость текста 'Для кого самокат'")
    def wait_main_text_for_order(self):
        return self.wait_of_visible_element(OrderPageLocators.text_title_order)
    
    @allure.step("Зполняем первую форму")
    def fill_first_form(self, user):
        self.fill_text_in_form(OrderPageLocators.name_field, user['name'])
        self.fill_text_in_form(OrderPageLocators.last_name_field, user['last_name'])
        self.fill_text_in_form(OrderPageLocators.adress_field, user['address'])
        self.click_on_element(OrderPageLocators.metro_field)
        self.fill_text_in_form(OrderPageLocators.metro_field, user['metro'])
        self.click_on_element(OrderPageLocators.metro_sports)
        self.wait_of_visible_element(OrderPageLocators.phone_field)
        self.fill_text_in_form(OrderPageLocators.phone_field, user['phone'])
        self.click_on_element(OrderPageLocators.next_button)

    @allure.step("Ожилаем загрузки теста 'Про аренду'")
    def wait_text_about_order(self):
        return self.wait_of_visible_element(OrderPageLocators.text_about_order)

    @allure.step("Заполняем вторую форму")
    def fill_second_form(self, user):
        self.fill_text_in_form(OrderPageLocators.data_order_field, user['data'])
        self.click_on_element(OrderPageLocators.rent_period_field)
        self.click_on_element(OrderPageLocators.rent_period_two_days)
        self.click_on_element(OrderPageLocators.checkbox_black_color)
        self.fill_text_in_form(OrderPageLocators.comment_field, user['comment'])
        self.click_on_element(OrderPageLocators.order_button)

    @allure.step("Ожидаем загрузки текста подтверждения заказа")
    def wait_text_to_order(self):
        return self.wait_of_visible_element(OrderPageLocators.text_want_to_order)
    
    @allure.step("Нажимаем кнопу ДА")
    def click_yes_button(self):
        self.click_on_element(OrderPageLocators.button_yes)
    
    @allure.step("Ожидаем загрузки текста Заказ оформлен")
    def wait_order_placed(self):
        return self.wait_of_visible_element(OrderPageLocators.text_order_placed)
    
    @allure.step("Проверяем появления кнопки Посмотреть заказ")
    def check_order_complete(self):
        return self.wait_visible_element(OrderPageLocators.button_status)
        



    

    
    