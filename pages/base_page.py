import allure
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, driver: webdriver.Firefox):
        self.driver = driver

    @allure.step("Ожидаем загрузки элемента")
    def wait_of_visible_element(self, locator, timeout=10 ):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
    
    @allure.step("Прокручиваем страницу до элемента")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step(f"Нажимаем на элемент")
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step("Нажимаем Enter")
    def click_enter(self, locator):
        self.driver.find_element(*locator).send_keys(Keys.ENTER)

    @allure.step("Получаем текст элемента")
    def get_text_from_element(self, locator):
        return self.driver.find_element(*locator).text
    
    @allure.step("Получаем текущий урл")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Переход на новую вкладку")
    def swich_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Ждем загрузки урл")
    def wait_url_contain(self, url, timeout=10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.url_contains(url))
    
    @allure.step("Ждем загрузки урл")
    def wait_url_to_be(self, url, timeout=10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.url_to_be(url))
    
    @allure.step("Ожидаем появления элемента")
    def wait_until_present(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))
    
    @allure.step("Заполняем поле для ввода")
    def fill_text_in_form(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step("Ожидаем видимость элемента")
    def wait_visible_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_all_elements_located(locator))
