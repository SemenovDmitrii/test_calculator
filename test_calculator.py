from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

# Открываем браузер Chrome
driver = webdriver.Chrome()

try:
    # Открываем страницу http://google.com
    driver.get("http://google.com")

    # Находим поисковую строку и вводим в нее слово "Калькулятор"
    search_box = driver.find_element(By.NAME,("q"))
    search_box.send_keys("Калькулятор")

    # Нажимаем Enter для выполнения поиска
    search_box.send_keys(Keys.RETURN)

    # Ждем 2 секунды, чтобы калькулятор загрузился
    time.sleep(2)

    # Жмем на кнопки 1 * 2 - 3 + 1 =
    button1 = driver.find_element(By.XPATH, "//div[@role='button'][normalize-space()='1']").click()

    button1_2 = driver.find_element(By.CSS_SELECTOR, ("[aria-label='умножение']")).click()

    button2 = driver.find_element(By.XPATH, "//div[@role='button'][normalize-space()='2']").click()

    button2_3 = driver.find_element(By.CSS_SELECTOR, ("[aria-label='вычитание']")).click()

    button3 = driver.find_element(By.XPATH, "//div[@role='button'][normalize-space()='3']").click()

    button3_4 = driver.find_element(By.CSS_SELECTOR, ("[aria-label='сложение']")).click()

    button4 = driver.find_element(By.XPATH, "//div[@role='button'][normalize-space()='1']").click()

    button5 = driver.find_element(By.CSS_SELECTOR, ("[aria-label='равно']")).click()

    # Ждем 2 секунды, чтобы результат отобразился
    time.sleep(2)

    # Находим результат вычисления
    # result = driver.find_element(By.ID, "cwos")

    # # Проверяем, что результат равен 0
    # assert result.text == "0"
    result0 = EC.presence_of_element_located((By.ID, "cwos"))
    result = result0.text
    assert result == "0", f"Ожидался результат '0', а получен '{result}'"

finally:
    # Закрываем браузер
    driver.quit()