import allure
from locators.questions_page_locators import QuestionsPageLocators
from pages.base_page import BasePage


class QuestionsPage(BasePage):

    @allure.step("Открываем страницу url: {page}")
    def open_page(self, page):
        self.driver.get(page)

    @allure.step("Прокручиваем страницу до надписи 'Важные вопросы'")
    def scroll_questions(self):
        self.scroll_to_element(QuestionsPageLocators.text_important_question)

    @allure.step("Ожидаем загрузки Вопросов")
    def wait_for_questions(self):
        return self.wait_of_visible_element(QuestionsPageLocators.text_important_question)
    
    @allure.step(f"Нажимаем на вопрос")
    def click_on_question(self, question):
        question_locator = QuestionsPageLocators.butter_question_number(question)
        self.click_on_element(question_locator)

    @allure.step(f"Ждем загрузки ответа")
    def wait_answer(self, question):
        return self.wait_of_visible_element(QuestionsPageLocators.text_from_question_number(question))

    @allure.step("Получаем текст элемента")
    def get_text_from_question(self, locator):
        return self.get_text_from_element(locator)

    
    @allure.step(f"Нажимаем на выпадающий список вопроса")
    def click_btn(self, question):
        question_locator = QuestionsPageLocators.butter_question_number(question)
        self.click_on_element(question_locator)
 
    
    @allure.step("Проверяем текст ответа на вопрос с ожидаемым текстом")
    def check_text(self, question, expected_text):
        text_question_locator = QuestionsPageLocators.text_from_question_number(question)
        return self.get_text_from_question(text_question_locator) == expected_text
