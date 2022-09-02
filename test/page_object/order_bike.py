import time
import allure
from selenium.webdriver.common.by import By


class OrderBike:

    bike_bth = [By.XPATH, "//img[@alt='Scooter']"]

    submit_bth = [By.XPATH, "//button[@type='submit']"]

    yandex_logo_bth = [By.XPATH, "//img[@alt='Yandex']"]

    header_order_btn = [By.XPATH, "//button[text()='Статус заказа']/..//button[text()='Заказать']"]

    footer_order_btn = [By.XPATH, "//div[contains(@class,'Home_FinishButton')]//button[text()='Заказать']"]

    name_field = [By.XPATH, "//input[@placeholder='* Имя']"]

    last_name_field = [By.XPATH, "//input[@placeholder='* Фамилия']"]

    address_field = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]

    subway_station_field = [By.XPATH, "//input[@placeholder='* Станция метро']"]

    subway_station_btn = [By.XPATH, "//input[@placeholder='* Станция метро']/../..//ul[contains(@class,'select')]//*[@data-value='4']"]

    subway_station_btn_set_2 = [By.XPATH, "//input[@placeholder='* Станция метро']/../..//ul[contains(@class,'select')]//*[@data-value='6']"]

    phone_number_field = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]

    cookei_btn = [By.XPATH, "//button[text() = 'да все привыкли']"]

    next_btn = [By.XPATH, "//button[text()='Далее']"]

    when_deliver_bike_btn = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]

    date_btn = [By.XPATH, "//div[@aria-label='Choose среда, 14-е сентября 2022 г.']"]

    date_set_2_btn = [By.XPATH, "//div[@aria-label='Choose пятница, 16-е сентября 2022 г.']"]

    period_rent_btn = [By.XPATH, "//div[text()='* Срок аренды']"]

    one_day_btn = [By.XPATH, "//div[text()='сутки']"]

    four_days_btn = [By.XPATH, "//div[text()='четверо суток']"]

    bike_color_checkbox = [By.XPATH, "//*[text()='серая безысходность']"]

    bike_color_checkbox_set_2 = [By.XPATH, "//*[text()='чёрный жемчуг']"]

    comment_for_deliver_field = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]

    last_step_order_btn = [By.XPATH, "//div[contains(@class,'Order_Buttons')]//button[text()='Заказать']"]

    yes_btn = [By.XPATH, "//div[@class='Order_Modal__YZ-d3']//button[text()='Да']"]

    order_overlay_window = [By.XPATH, "//div[contains(@class,'Overlay')]"]

    text_on_window_after_order = [By.XPATH, "//div[text()='Заказ оформлен']"]

    text_on_main_page = [By.XPATH, "//div[text()='Самокат ']"]

    text_on_captcha = [By.XPATH, "//span[text()='Подтвердите, что запросы отправляли вы, а не робот']"]

    @allure.step('Открываем браузер Chrome')
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    @allure.step('Выполняем проскролл до кнопки «Заказать» внизу страницы')
    def scroll_to_element_order_btn(self):
        time.sleep(3)
        element = self.driver.find_element(*self.footer_order_btn)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Нажимем кнопку "Yandex"')
    def yandex_logo_bth_click(self):
        self.driver.find_element(*self.yandex_logo_bth).click()

    @allure.step('Нажимаем кнопку "Заказать" вверху страницы')
    def header_order_btn_click(self):
        self.driver.find_element(*self.header_order_btn).click()

    @allure.step('Нажимем кнопку "Самокат"')
    def bike_bth_click(self):
        self.driver.find_element(*self.bike_bth).click()

    @allure.step('Нажимем кнопку "Заказать" внизу страницы')
    def footer_order_btn_click(self):
        self.driver.find_element(*self.footer_order_btn).click()

    @allure.step('Нажимем кнопку "да все привыкли"')
    def cookei_btn_click(self):
        self.driver.find_element(*self.cookei_btn).click()

    @allure.step('Нажимем кнопку "Далее"')
    def next_btn_click(self):
        self.driver.find_element(*self.next_btn).click()

    @allure.step('Нажимем кнопку "Заказать" на последнем шаге')
    def last_step_order_btn_click(self):
        self.driver.find_element(*self.last_step_order_btn).click()

    @allure.step('Нажимем кнопку "Да" для подтверждения заказа')
    def yes_btn_click(self):
        self.driver.find_element(*self.yes_btn).click()

    @allure.step('Переключаемся на новое окно')
    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Заполняем форму заказа set_1')
    def fill_order_form_set_1(self, name, last_name, address, phone_number):
        self.driver.find_element(*self.name_field).send_keys(name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.address_field).send_keys(address)
        self.driver.find_element(*self.subway_station_field).click()
        self.driver.find_element(*self.subway_station_btn).click()
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)

    @allure.step('Заполняем форму заказа set_2')
    def fill_order_form_set_2(self, name, last_name, address, phone_number):
        self.driver.find_element(*self.name_field).send_keys(name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.address_field).send_keys(address)
        self.driver.find_element(*self.subway_station_field).click()
        self.driver.find_element(*self.subway_station_btn_set_2).click()
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)

    @allure.step('Заполняем форму "Про аренду" set_1')
    def fill_about_rent_form_set_1(self, comment_for_deliver):
        self.driver.find_element(*self.when_deliver_bike_btn).click()
        self.driver.find_element(*self.date_btn).click()
        self.driver.find_element(*self.period_rent_btn).click()
        self.driver.find_element(*self.one_day_btn).click()
        self.driver.find_element(*self.bike_color_checkbox).click()
        self.driver.find_element(*self.comment_for_deliver_field).send_keys(comment_for_deliver)

    @allure.step('Заполняем форму "Про аренду" set_2')
    def fill_about_rent_form_set_2(self, comment_for_deliver):
        self.driver.find_element(*self.when_deliver_bike_btn).click()
        self.driver.find_element(*self.date_set_2_btn).click()
        self.driver.find_element(*self.period_rent_btn).click()
        self.driver.find_element(*self.four_days_btn).click()
        self.driver.find_element(*self.bike_color_checkbox_set_2).click()
        self.driver.find_element(*self.comment_for_deliver_field).send_keys(comment_for_deliver)

    @allure.step('Проверить, что появилось всплывающее окно с сообщением об успешном создании заказа.')
    def check_text_on_window_after_order(self):
        text = self.driver.find_element(*self.text_on_window_after_order).text.split()
        assert 'Заказ' and 'оформлен' in text

    @allure.step('Проверяем текст на главной странице заказа самоката')
    def check_text_on_main_page(self):
        text = self.driver.find_element(*self.text_on_main_page).text.split()
        assert 'Самокат' and 'Привезём' in text

    @allure.step('Проверяем текст на главной странице Яндекса')
    def check_text_on_yandex_page(self):
        time.sleep(3)

        if self.driver.find_element(*self.submit_bth):
            text = self.driver.find_element(*self.submit_bth).text
            assert text == 'Найти', 'Error'
