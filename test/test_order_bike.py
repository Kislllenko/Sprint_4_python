import allure
from selenium import webdriver
from page_object.order_bike import OrderBike


class TestOrderBike:
    driver = None

    @allure.title('Проверка заказа самоката через кнопку «Заказать» вверху страницы "первый набор"')
    def test_order_bike_set_1(self):
        # Создаём драйвер для браузера Firefox
        self.driver = webdriver.Firefox()
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        # Создаём объект класса страницы авторизации
        order_bike_set_1 = OrderBike(self.driver)
        # Нажимем кнопку "Заказать"
        order_bike_set_1.header_order_btn_click()
        # Нажимем кнопку "да все привыкли"
        order_bike_set_1.cookei_btn_click()
        # Заполняем форму заказа
        order_bike_set_1.fill_order_form_set_1('Сергей', 'Кисленко', 'Санкт-Петербург ул. Яхтенная', '89991234532')
        # Нажимаем кнопку "Далее"
        order_bike_set_1.next_btn_click()
        # Заполняем форму "Про аренду"
        order_bike_set_1.fill_about_rent_form_set_1('комментарий')
        # Нажимаем кнопку "Заказать" на последнем шаге
        order_bike_set_1.last_step_order_btn_click()
        # Нажимаем кнопку "Да" для подтверждения заказа
        order_bike_set_1.yes_btn_click()
        # Проверяем что появилось всплывающее окно с сообщением об успешном создании заказа.
        order_bike_set_1.check_text_on_window_after_order()
        # Закрываем браузер
        self.driver.quit()

    @allure.title('Проверка заказа самоката через кнопку «Заказать» внизу страницы второй набор')
    def test_order_bike_set_2(self):
        # Создаём драйвер для браузера Firefox
        self.driver = webdriver.Firefox()
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        # Создаём объект класса страницы авторизации
        order_bike_set_2 = OrderBike(self.driver)
        # Нажимаем кнопку "да все привыкли"
        order_bike_set_2.cookei_btn_click()
        # Выполняем проскролл до кнопки «Заказать» внизу страницы
        order_bike_set_2.scroll_to_element_order_btn()
        # Нажимаем кнопку "Заказать"
        order_bike_set_2.footer_order_btn_click()
        # Заполняем форму заказа
        order_bike_set_2.fill_order_form_set_2('Андрей', 'Острогорский', 'Москва ул. Шоссейная', '89111234538')
        # Нажимем кнопку "Далее"
        order_bike_set_2.next_btn_click()
        # Заполняем форму "Про аренду"
        order_bike_set_2.fill_about_rent_form_set_2('комментарий для второго набора')
        # Нажимем кнопку "Заказать" на последнем шаге
        order_bike_set_2.last_step_order_btn_click()
        # Нажимем кнопку "Да" для подтверждения заказа
        order_bike_set_2.yes_btn_click()
        # Проверяем что появилось всплывающее окно с сообщением об успешном создании заказа.
        order_bike_set_2.check_text_on_window_after_order()
        # Закрываем браузер
        self.driver.quit()

    @allure.title('Проверить: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».')
    def test_check_bike_btn(self):
        # Создаём драйвер для браузера Firefox
        self.driver = webdriver.Firefox()
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        # Создаём объект класса страницы авторизации
        order_bike_set_1 = OrderBike(self.driver)
        # Нажимаем кнопку "Заказать"
        order_bike_set_1.header_order_btn_click()
        # Нажимаем кнопку "Самокат"
        order_bike_set_1.bike_bth_click()
        # Проверяем текст на главной странице заказа самоката
        order_bike_set_1.check_text_on_main_page()
        # Закрываем браузер
        self.driver.quit()

    @allure.title('Проверить: если нажать на логотип Яндекса, в новом окне откроется главная страница Яндекса.')
    def test_check_yandex_btn(self):
        # Создаём драйвер для браузера Firefox
        self.driver = webdriver.Firefox()
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        # Создаём объект класса страницы авторизации
        order_bike_set_1 = OrderBike(self.driver)
        # Нажимаем кнопку "Yandex"
        order_bike_set_1.yandex_logo_bth_click()
        # Переключаемся на новое окно
        order_bike_set_1.switch_to_window()
        # Проверяем текст на главной странице Яндекса
        order_bike_set_1.check_text_on_yandex_page()
        # Закрываем браузер
        self.driver.quit()
