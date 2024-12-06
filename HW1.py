# Создай гистограмму для случайных данных
import numpy as np
import matplotlib.pyplot as plt

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(0, 1, 1000)

# Построение гистограммы
plt.hist(data, bins=12)

# Заголовок, подписи осей
plt.title("Гистограмма")
plt.xlabel("x")
plt.ylabel("y")

# Вызов гистограммы
plt.show()
