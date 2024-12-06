# Построим график функции у=х**2
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

y = x**2

# Построение графика
plt.plot(x,y)

# Заголовок, подписи осей
plt.title("Линейный график")
plt.xlabel("x")
plt.ylabel("y")

# Сетка на графике
plt.grid(True)

# Вызов графика
plt.show()
