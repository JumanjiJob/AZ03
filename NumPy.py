import numpy as np

# Одномерный массив
a = np.array([1, 2, 3, 4])
#print(a)

# Массив из нулей
b = np.zeros((2, 5))
#print(b)

# Массив из единиц
c = np.ones((3,7))
#print(c)

# Массив из случайных чисел от 0 до 1
d = np.random.random((2, 5))
#print(d)

# Массив с последовательностью чисел
e = np.arange(0, 12, 3)
#print(e)

# Массив с равнораспределенными числами
f = np.linspace(0, 1, 10)
print(f)