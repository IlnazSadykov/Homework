"""Задание 2. Автоматизация позитивного тест-кейса. Добавление объявления в избранное в Desktop версии сайта"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Присваиваем переменной объект вебдрайвера хрома
driver = webdriver.Chrome()

# Ссылка на объявление из задания
link = 'https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363'
# Название книги для дальнейшей проверки
title = 'Domain-Driven Design Distilled Vaughn Vernon'

# Используем конструкцию try/finally, для закрытия браузера при ошибке
try:
    driver.get(link)    # Открываем ссылку в браузере
    driver.maximize_window()    # Открываем окно браузера на весь экран

    # Находим кнопку "добавить в избранное" и кликаем ее
    add_to_favorites = driver.find_element(By.CSS_SELECTOR, '.style-header-add-favorite-M7nA2 button.desktop-usq1f1')
    add_to_favorites.click()

    # Находим кнопку "Избранное", и переходим на страницу избранных объявлений
    favorites_button = driver.find_element(By.CSS_SELECTOR, '[data-marker="header/favorites"]')
    favorites_button.click()

    # Находим элнемент, содержащий название объявления
    item = driver.find_element(By.CSS_SELECTOR, '[class="styles-module-root-hwVld"]')
    # Записываем текст названия в переменную
    item_text = item.text

    # С помощью assert сравниваем название книги из тз с названием объявления
    assert title == item_text

finally:
    # Ожидание, чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # Закрываем браузер
    driver.quit()