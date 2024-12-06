# Построение простой гистограммы

import matplotlib.pyplot as plt

# Список для гистограммы
data = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6, 6]


# Построение гистограммы
plt.hist(data, bins=6)

# Заголовок, подписи осей
plt.title("Гистограмма")
plt.xlabel("x")
plt.ylabel("y")

# Вызов гистограммы
plt.show()
