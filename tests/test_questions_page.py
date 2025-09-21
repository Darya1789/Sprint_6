import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators
from locators.questions_page_locators import QuestionsPageLocators
import urls
from pages.questions_page import QuestionsPage
from data import ExpectedTest, Data

class TestPageQuestions():
    driver = None
    
    
    @classmethod
    def setup_method(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Firefox()
        
    @pytest.mark.parametrize('question, expected_text', Data.questions)
    @allure.title('Проверка текста выпадающего списка {question} вопроса') # декораторы
    @allure.description('Прокручиваем главную страницу вниз и проверяем текст {question} вопроса')
    def test_first_question(self, question, expected_text):
        question_page = QuestionsPage(self.driver)
        question_page.open_page(urls.main_page)
        question_page.scroll_questions()
        question_page.wait_for_questions()
        question_page.click_on_question(question)
        question_page.wait_answer(question)
        assert question_page.check_text(question, expected_text)

    
    @classmethod
    def teardown_method(cls):
        # закрыли браузер
        cls.driver.quit() 