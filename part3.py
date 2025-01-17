# Построение простого графика рассеяния

import matplotlib.pyplot as plt

# Списки как значения аргументов
x = [2, 5, 9, 14, 19]
y = [3, 5, 9, 20, 23]

# Построение графика
plt.scatter(x,y)

# Заголовок, подписи осей
plt.title("Линейный график")
plt.xlabel("x")
plt.ylabel("y")

# Вызов графика
plt.show()