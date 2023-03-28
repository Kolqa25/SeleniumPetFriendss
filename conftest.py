import pytest
import uuid
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture(autouse=True, scope="session")
def browser():
    pytest.driver = webdriver.Chrome('C:\Chrome\chromedriver.exe')
    pytest.driver.set_window_size(1200, 2000)

    # активируем неявное ожидание
    pytest.driver.implicitly_wait(10)

    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    # Очищаем поле и вводим email
    field_email = pytest.driver.find_element(By.ID, 'email')
    field_email.clear()
    field_email.send_keys('kolqajj322@gmail.com')

    # Очищаем поле и вводим пароль
    field_pass = pytest.driver.find_element(By.ID, 'pass')
    field_pass.clear()
    field_pass.send_keys("783426470")
    time.sleep(2)

    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Проверяем, что находимся на главной странице пользователя

    if not pytest.driver.current_url == 'https://petfriends.skillfactory.ru/all_pets':
        pytest.driver.quit()
        raise Exception("Некорректный email или пароль")

    # Нажимаем на ссылку "Мои питомцы"
    pytest.driver.find_element(By.XPATH, "//a[contains(text(),'Мои питомцы')]").click()

    # Проверяем, что перешли на страницу "Мои питомцы"

    if not pytest.driver.current_url == 'https://petfriends.skillfactory.ru/my_pets':
        pytest.driver.quit()
        raise Exception("Это не страница Мои питомцы")

    yield

    pytest.driver.quit()