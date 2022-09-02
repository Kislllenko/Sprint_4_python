import allure
from selenium import webdriver
from page_object.questions_about_important import QuestionsAboutImportant


class TestCheckDropDownList:
    driver = None

    @classmethod
    def setup_class(cls):
        # Создаём драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()
        cls.driver.get('https://qa-scooter.praktikum-services.ru/')

    @allure.title('Проверка текста в вопросе: "Сколько это стоит? И как оплатить?"')
    def test_how_much_question(self):
        # Создаём объект класса страницы авторизации
        questions_about = QuestionsAboutImportant(self.driver)
        # Нажимаем кнопку "да все привыкли"
        questions_about.accept_cookei_btn_click()
        # Выполняем проскролл до нужного элемента
        questions_about.scroll()
        # Выполняем клик по вопросу "Сколько это стоит? И как оплатить?"
        questions_about.how_much_click()
        # Выполняем проверку текста в открывшемся списке
        questions_about.check_text_how_much_btn()

    @allure.title('Проверка текста в вопросе: "Хочу сразу несколько самокатов! Так можно?"')
    def test_wanna_some_bikes_question(self):
        # Создаём объект класса страницы авторизации
        questions_about = QuestionsAboutImportant(self.driver)
        # Выполняем проскролл до нужного элемента
        questions_about.scroll()
        # Выполняем клик по вопросу "Хочу сразу несколько самокатов! Так можно?"
        questions_about.wanna_some_bikes_click()
        # Выполняем проверку текста в открывшемся списке
        questions_about.check_text_wanna_some_bikes_btn()

    @allure.title('Проверка текста в вопросе: "Как рассчитывается время аренды?"')
    def test_how_time_calculated_question(self):
        # Создаём объект класса страницы авторизации
        questions_about = QuestionsAboutImportant(self.driver)
        # Выполняем проскролл до нужного элемента
        questions_about.scroll()
        # Выполняем клик по вопросу, "Как рассчитывается время аренды?"
        questions_about.how_time_calculated_click()
        # Выполняем проверку текста в открывшемся списке
        questions_about.check_text_how_time_calculated_btn()

    @allure.title('Проверка текста в вопросе: "Можно ли заказать самокат прямо на сегодня?"')
    def test_order_today_question(self):
        # Создаём объект класса страницы авторизации
        questions_about = QuestionsAboutImportant(self.driver)
        # Выполняем проскролл до нужного элемента
        questions_about.scroll()
        # Выполняем клик по вопросу "Можно ли заказать самокат прямо на сегодня?"
        questions_about.order_today_btn_click()
        # Выполняем проверку текста в открывшемся списке
        questions_about.check_text_order_today_btn()

    @allure.title('Проверка текста в вопросе: "Можно ли продлить заказ или вернуть самокат раньше?"')
    def test_give_back_bike_question(self):
        # Создаём объект класса страницы авторизации
        questions_about = QuestionsAboutImportant(self.driver)
        # Выполняем проскролл до нужного элемента
        questions_about.scroll()
        # Выполняем клик по вопросу "Можно ли продлить заказ или вернуть самокат раньше?"
        questions_about.give_back_bike_btn_click()
        # Выполняем проверку текста в открывшемся списке
        questions_about.check_text_give_back_bike_btn()

    @allure.title('Проверка текста в вопросе: "Вы привозите зарядку вместе с самокатом?"')
    def test_charge_for_bike_question(self):
        # Создаём объект класса страницы авторизации
        questions_about = QuestionsAboutImportant(self.driver)
        # Выполняем проскролл до нужного элемента
        questions_about.scroll()
        # Выполняем клик по вопросу "Вы привозите зарядку вместе с самокатом?"
        questions_about.charge_for_bike_btn_click()
        # Выполняем проверку текста в открывшемся списке
        questions_about.check_text_charge_for_bike_btn()

    @allure.title('Проверка текста в вопросе: "Можно ли отменить заказ?"')
    def test_cancel_order_question(self):
        # Создаём объект класса страницы авторизации
        questions_about = QuestionsAboutImportant(self.driver)
        # Выполняем проскролл до нужного элемента
        questions_about.scroll()
        # Выполняем клик по вопросу "Можно ли отменить заказ?"
        questions_about.cancel_order_btn_click()
        # Выполняем проверку текста в открывшемся списке
        questions_about.check_text_cancel_order_btn()

    @allure.title('Проверка текста в вопросе: "Я живу за МКАДом, привезёте?"')
    def test_not_into_mkad_question(self):
        # Создаём объект класса страницы авторизации
        questions_about = QuestionsAboutImportant(self.driver)
        # Выполняем проскролл до нужного элемента
        questions_about.scroll()
        # Выполняем клик по вопросу "Я живу за МКАДом, привезёте?"
        questions_about.not_into_mkad_btn_click()
        # Выполняем проверку текста в открывшемся списке
        questions_about.check_text_not_into_mkad_btn()

    @classmethod
    def teardown_class(cls):
        # Закрываем браузер
        cls.driver.quit()


