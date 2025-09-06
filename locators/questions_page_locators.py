from selenium.webdriver.common.by import By


class QuestionsPageLocators():

    text_important_question = (By.XPATH, ".//div[text() = 'Вопросы о важном']")

    @staticmethod
    def butter_question_number(question):
        return (By.ID, f'accordion__heading-{question}')
    
    @staticmethod
    def text_from_question_number(question):
        return By.XPATH, f".//div[@aria-labelledby='accordion__heading-{question}']/p"
    

    
    button_question_1 = (By.ID, "accordion__heading-0")
    button_question_2 = (By.ID, "accordion__heading-1")
    button_question_3 = (By.ID, "accordion__heading-2")
    button_question_4 = (By.ID, "accordion__heading-3")
    button_question_5 = (By.ID, "accordion__heading-4")
    button_question_6 = (By.ID, "accordion__heading-5")
    button_question_7 = (By.ID, "accordion__heading-6")
    button_question_8 = (By.ID, "accordion__heading-7")

    text_from_1_question = (By.XPATH, ".//div[@aria-labelledby='accordion__heading-0']/p")
    text_from_2_question = (By.XPATH, ".//div[@aria-labelledby='accordion__heading-1']/p")
    text_from_3_question = (By.XPATH, ".//div[@aria-labelledby='accordion__heading-2']/p")
    text_from_4_question = (By.XPATH, ".//div[@aria-labelledby='accordion__heading-3']/p")
    text_from_5_question = (By.XPATH, ".//div[@aria-labelledby='accordion__heading-4']/p")
    text_from_6_question = (By.XPATH, ".//div[@aria-labelledby='accordion__heading-5']/p")
    text_from_7_question = (By.XPATH, ".//div[@aria-labelledby='accordion__heading-6']/p")
    text_from_8_question = (By.XPATH, ".//div[@aria-labelledby='accordion__heading-6']/p")
