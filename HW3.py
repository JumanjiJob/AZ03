import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import pandas as pd
import matplotlib.pyplot as plt

class SvetparsSpider:
    def __init__(self):
        # Настройка драйвера
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.start_url = "https://www.divan.ru/category/divany"
        self.divans_data = []  # Список для хранения данных о диванах

    def parse(self):
        # Открываем страницу
        self.driver.get(self.start_url)

        # Ожидаем, пока элементы не будут загружены
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.LlPhw')))

        # Найдем все элементы, содержащие информацию о диванах
        divans = self.driver.find_elements(By.CSS_SELECTOR, 'div.LlPhw')

        # Собираем данные
        for divan in divans:
            try:
                price_text = divan.find_element(By.CSS_SELECTOR, 'div.pY3d2 span.ui-LD-ZU.KIkOH').text
                # Очищаем цену от символов и оставляем только цифры и точки
                price = self.extract_price(price_text)
            except:
                price = None

            # Добавляем цену в список, если она числовая
            if price is not None:
                self.divans_data.append({
                    'Цена': price
                })

    def extract_price(self, price_text):
        # Убираем все нецифровые символы, оставляем только числа и точку для десятичных чисел
        price = re.sub(r'[^\d.,]', '', price_text)
        # Заменяем запятую на точку для возможных десятичных чисел
        price = price.replace(',', '.')
        try:
            return float(price)
        except ValueError:
            return None

    def save_to_csv(self):
        # Сохраняем данные в CSV файл
        with open("prices.csv", 'w', newline='', encoding='utf-8-sig') as file:
            # Определяем порядок столбцов
            fieldnames = ['Цена']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  # Записываем заголовки
            writer.writerows(self.divans_data)  # Записываем все данные из списка

    def close(self):
        # Закрываем браузер после выполнения
        self.driver.quit()

# Создаем объект паука и запускаем парсинг
spider = SvetparsSpider()
spider.parse()
spider.save_to_csv()  # Сохраняем данные в файл CSV
spider.close()

df= pd.DataFrame(spider.divans_data)

a = df.mean()
print(f'Средняя цена на диваны - {a}')

# Построение гистограммы
plt.hist(df, bins=12)

# Заголовок, подписи осей
plt.title("Гистограмма цен")
plt.xlabel("Цена")
plt.ylabel("Количество диванов")

# Вызов гистограммы
plt.show()