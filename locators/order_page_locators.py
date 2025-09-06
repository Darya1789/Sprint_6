from selenium.webdriver.common.by import By


class OrderPageLocators():

    text_title_order = (By.XPATH, ".//div[text() = 'Для кого самокат']")
    # первая форма
    name_field = (By.XPATH, ".//input[@placeholder = '* Имя']")
    last_name_field = (By.XPATH, ".//input[@placeholder = '* Фамилия']")
    adress_field = (By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']")
    metro_field = (By.XPATH, ".//input[@placeholder = '* Станция метро']")
    phone_field = (By.XPATH, ".//input[@placeholder = '* Телефон: на него позвонит курьер']")
    next_button = (By.XPATH, ".//button[text() = 'Далее']")
    metro_sports = (By.XPATH, ".//div[text() = 'Спортивная']")
    # вторая форма
    text_about_order = (By.XPATH, ".//div[text() = 'Про аренду']")
    data_order_field = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    rent_period_field = (By.XPATH, ".//span[@class='Dropdown-arrow']")
    rent_period_two_days = (By.XPATH, ".//div[text() = 'двое суток']")
    checkbox_black_color = (By.ID, 'black')
    checkbox_grey_color = (By.ID, 'grey')
    comment_field = (By.XPATH, ".//input[@placeholder= 'Комментарий для курьера']")
    order_button = (By.XPATH, "(.//button[text() = 'Заказать'])[2]")
    # третья форма
    text_want_to_order = (By.XPATH, ".//div[text() = 'Хотите оформить заказ?']")
    button_yes = (By.XPATH, ".//button[text() = 'Да']")

    # Окно заказа
    text_order_placed = (By.XPATH, ".//div[text() = 'Заказ оформлен']")
    button_status = (By.XPATH, ".//button[text() = 'Посмотреть статус']")