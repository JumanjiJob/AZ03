#Построй диаграмму рассеяния для двух наборов случайных данных
import numpy as np
import matplotlib.pyplot as plt

# массив из 5 случайных чисел
random_array1 = np.random.rand(5)
random_array2 = np.random.rand(5)

# Построение графика
plt.scatter(random_array1,random_array2)

# Заголовок, подписи осей
plt.title("Линейный график")
plt.xlabel("x")
plt.ylabel("y")

# Вызов графика
plt.show()