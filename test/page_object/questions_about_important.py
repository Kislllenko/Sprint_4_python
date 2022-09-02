import time
import allure
from selenium.webdriver.common.by import By


class QuestionsAboutImportant:
    how_much_btn = [By.XPATH, "//*[text() ='Сколько это стоит? И как оплатить?']"]

    wanna_some_bikes_btn = [By.XPATH, "//*[text() ='Хочу сразу несколько самокатов! Так можно?']"]

    how_time_calculated_btn = [By.XPATH, "//*[text() ='Как рассчитывается время аренды?']"]

    order_today_btn = [By.XPATH, "//*[text() ='Можно ли заказать самокат прямо на сегодня?']"]

    give_back_bike_btn = [By.XPATH, "//*[text() ='Можно ли продлить заказ или вернуть самокат раньше?']"]

    charge_for_bike_btn = [By.XPATH, "//*[text() ='Вы привозите зарядку вместе с самокатом?']"]

    cancel_order_btn = [By.XPATH, "//*[text() ='Можно ли отменить заказ?']"]

    not_into_mkad_btn = [By.XPATH, "//*[text() ='Я жизу за МКАДом, привезёте?']"]

    accept_cookei_btn = [By.XPATH, "//button[text() = 'да все привыкли']"]

    text_how_much_btn = [By.XPATH, "//*[text() = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.']"]

    text_wanna_some_bikes_btn = [By.XPATH, "//*[text() = 'Пока что у нас так: один заказ — один самокат. "
                                           "Если хотите покататься с друзьями, "
                                           "можете просто сделать несколько заказов — один за другим.']"]

    text_how_time_calculated_btn = [By.XPATH, "//*[text() = 'Допустим, вы оформляете заказ на 8 мая. "
                                              "Мы привозим самокат 8 мая в течение дня. "
                                              "Отсчёт времени аренды начинается с момента, "
                                              "когда вы оплатите заказ курьеру. "
                                              "Если мы привезли самокат 8 мая в 20:30, "
                                              "суточная аренда закончится 9 мая в 20:30.']"]

    text_order_today_btn = [By.XPATH, "//*[text() = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.']"]

    text_give_back_bike_btn = [By.XPATH, "//*[text() = 'Пока что нет! "
                                         "Но если что-то срочное — "
                                         "всегда можно позвонить в поддержку по красивому номеру 1010.']"]

    text_charge_for_bike_btn = [By.XPATH, "//*[text() = 'Самокат приезжает к вам с полной зарядкой. "
                                          "Этого хватает на восемь суток — "
                                          "даже если будете кататься без передышек и во сне. Зарядка не понадобится.']"]

    text_cancel_order_btn = [By.XPATH, "//*[text() = 'Да, пока самокат не привезли. "
                                       "Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.']"]

    text_not_into_mkad_btn = [By.XPATH, "//*[text() = 'Да, обязательно. "
                                        "Всем самокатов! И Москве, и Московской области.']"]

    @allure.step('Открываем браузер Firefox')
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    @allure.step('Нажимем кнопку "да все привыкли"')
    def accept_cookei_btn_click(self):
        self.driver.find_element(*self.accept_cookei_btn).click()

    @allure.step('Выполняем проскролл до нужного элемента')
    def scroll(self):
        time.sleep(3)
        element = self.driver.find_element(*self.cancel_order_btn)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Нажимем на поле с вопросом "Сколько это стоит? И как оплатить?"')
    def how_much_click(self):
        self.driver.find_element(*self.how_much_btn).click()

    @allure.step('Нажимем на поле с вопросом "Хочу сразу несколько самокатов! Так можно?"')
    def wanna_some_bikes_click(self):
        self.driver.find_element(*self.wanna_some_bikes_btn).click()

    @allure.step('Нажимем на поле с вопросом how_time_calculated_btn')
    def how_time_calculated_click(self):
        self.driver.find_element(*self.how_time_calculated_btn).click()

    @allure.step('Нажимем на поле с вопросом "Как рассчитывается время аренды?"')
    def order_today_btn_click(self):
        self.driver.find_element(*self.order_today_btn).click()

    @allure.step('Нажимем на поле с вопросом "Можно ли продлить заказ или вернуть самокат раньше?"')
    def give_back_bike_btn_click(self):
        self.driver.find_element(*self.give_back_bike_btn).click()

    @allure.step('Нажимем на поле с вопросом "Вы привозите зарядку вместе с самокатом?"')
    def charge_for_bike_btn_click(self):
        self.driver.find_element(*self.charge_for_bike_btn).click()

    @allure.step('Нажимем на поле с вопросом "Можно ли отменить заказ?"')
    def cancel_order_btn_click(self):
        self.driver.find_element(*self.cancel_order_btn).click()

    @allure.step('Нажимем на поле с вопросом "Я живу за МКАДом, привезёте?"')
    def not_into_mkad_btn_click(self):
        self.driver.find_element(*self.not_into_mkad_btn).click()

    @allure.step('Проверяем соответствие текста ответа на вопрос "Сколько это стоит? И как оплатить?"')
    def check_text_how_much_btn(self):
        text = self.driver.find_element(*self.text_how_much_btn).text
        assert text == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.', 'Error'

    @allure.step('Проверяем соответствие текста ответа на вопрос "Хочу сразу несколько самокатов! Так можно?"')
    def check_text_wanna_some_bikes_btn(self):
        text = self.driver.find_element(*self.text_wanna_some_bikes_btn).text
        assert text == 'Пока что у нас так: один заказ — один самокат. ' \
                       'Если хотите покататься с друзьями, ' \
                       'можете просто сделать несколько заказов — один за другим.', 'Error'

    @allure.step('Проверяем соответствие текста ответа на вопрос "Как рассчитывается время аренды?"')
    def check_text_how_time_calculated_btn(self):
        text = self.driver.find_element(*self.text_how_time_calculated_btn).text
        assert text == 'Допустим, вы оформляете заказ на 8 мая. ' \
                       'Мы привозим самокат 8 мая в течение дня. ' \
                       'Отсчёт времени аренды начинается с момента, ' \
                       'когда вы оплатите заказ курьеру. ' \
                       'Если мы привезли самокат 8 мая в 20:30, ' \
                       'суточная аренда закончится 9 мая в 20:30.', 'Error'

    @allure.step('Проверяем соответствие текста ответа на вопрос "Можно ли заказать самокат прямо на сегодня?"')
    def check_text_order_today_btn(self):
        text = self.driver.find_element(*self.text_order_today_btn).text
        assert text == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.', 'Error'

    @allure.step('Проверяем соответствие текста ответа на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"')
    def check_text_give_back_bike_btn(self):
        text = self.driver.find_element(*self.text_give_back_bike_btn).text
        assert text == 'Пока что нет! ' \
                       'Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.', 'Error'

    @allure.step('Проверяем соответствие текста ответа на вопрос "Вы привозите зарядку вместе с самокатом?"')
    def check_text_charge_for_bike_btn(self):
        text = self.driver.find_element(*self.text_charge_for_bike_btn).text
        assert text == 'Самокат приезжает к вам с полной зарядкой. ' \
                       'Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. ' \
                       'Зарядка не понадобится.', 'Error'

    @allure.step('Проверяем соответствие текста ответа на вопрос "Можно ли отменить заказ?"')
    def check_text_cancel_order_btn(self):
        text = self.driver.find_element(*self.text_cancel_order_btn).text
        assert text == 'Да, пока самокат не привезли. ' \
                       'Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.', 'Error'

    @allure.step('Проверяем соответствие текста ответа на вопрос "Я живу за МКАДом, привезёте?"')
    def check_text_not_into_mkad_btn(self):
        text = self.driver.find_element(*self.text_not_into_mkad_btn).text
        assert text == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.', 'Error'
