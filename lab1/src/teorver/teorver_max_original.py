# Импорт библиотек
import pandas as pd
import numpy as np
from statsmodels.distributions.empirical_distribution import ECDF
import matplotlib.pyplot as plt


# Чтение выборки из файла sample.txt
sample = np.loadtxt('sample5.txt', delimiter=',')
n = sample.size
print('Выборка: ', sample)
print('Размер:', n)
# Выборка:  [-1.73 -0.73  1.66 -0.8   0.62  1.52  1.63  1.04  0.42 -1.21  0.9  -1
#             0.24  0.62  0.55 -1.45 -1.45 -0.52  0.17 -1.31]
# Размер: 20


# Вариационный ряд
variation_series = np.sort(sample)
print(variation_series)
# [-1.73 -1.45 -1.45 -1.31 -1.21 -1    -0.8  -0.73 -0.52  0.17  0.24  0.42
#   0.55  0.62  0.62  0.9   1.04  1.52  1.63  1.66]


# Экстремальные значения и размах
extreme_1 = variation_series[0]
extreme_n = variation_series[n - 1]
variation_size = extreme_n - extreme_1
print('Первая порядковая статистика x(1) = ', extreme_1)
print('n-ая порядковая статистика x(n) = ', extreme_n)
print('Размах выборки w* = ', variation_size)
# Первая порядковая статистика x(1) =  -1.73
# n-ая порядковая статистика x(n) =  1.66
# Размах выборки w* =  3.3899999999999997


# Оценки математического ожидания и среднеквадратичного отклонения
# а) Математическое ожидание
expected_value = 0
for val in variation_series:
    expected_value += val / n
print('Математическое ожидание (цикл) M = ', expected_value)
print('Математическое ожидание (библиотека) M = ', variation_series.mean())
# Математическое ожидание (цикл) M =  -0.041499999999999926
# Математическое ожидание (библиотека) M =  -0.04150000000000006


# б) Среднеквадратичное отклонение
standard_deviation = 0
for val in variation_series:
    delta = (val - expected_value)
    standard_deviation += delta**2 / n
dispersion = standard_deviation
standard_deviation = standard_deviation**(1/2)
fixed_dispersion = dispersion * n / (n - 1)
print('Среднеквадратичное отклонение (цикл) sigma = ', standard_deviation)
print('Среднеквадратичное отклонение (библиотека) sigma = ', np.std(variation_series))
print('Выборочная дисперсия dispersion = ', dispersion)
print('Исправленное СКО s^2 = :', fixed_dispersion)
# Среднеквадратичное отклонение (цикл) sigma =  1.0893955893062905
# Среднеквадратичное отклонение (библиотека) sigma =  1.0893955893062905
# Выборочная дисперсия dispersion =  1.1867827499999999
# Исправленное СКО s^2 = : 1.249245


# Эмпирическая функция распределения и её график
# а) Построение руками

#  создание статистического ряда
x, counts = np.unique(variation_series, return_counts=True)
p = counts / len(variation_series)
F_x = np.cumsum(p)

data = {'x': x, 'Количество': counts, 'Частости': p, 'F(x)': F_x}
df = pd.DataFrame(data)

#  вывод статистического ряда
print(df[['x', 'F(x)']])

#  использование кумулятивных частот для построения эмпирической функции распределения
plt.step(df['x'], df['F(x)'], where='post')

#  настройка заголовка и меток осей
plt.title('Эмпирическая функция распределения')
plt.xlabel('x')
plt.ylabel('F(x)')

#  вывод графика
plt.show()

#        x  F(x)
# 0  -1.73  0.05
# 1  -1.45  0.15
# 2  -1.31  0.20
# 3  -1.21  0.25
# 4  -1.00  0.30
# 5  -0.80  0.35
# 6  -0.73  0.40
# 7  -0.52  0.45
# 8   0.17  0.50
# 9   0.24  0.55
# 10  0.42  0.60
# 11  0.55  0.65
# 12  0.62  0.75
# 13  0.90  0.80
# 14  1.04  0.85
# 15  1.52  0.90
# 16  1.63  0.95
# 17  1.66  1.00


# Построение гистограммы и полигона приведенных частот группированной выборки

#  количество интервалов разбиения
m = int( 1 + np.log2(n) ) + 1

#  ширина шага
h = (variation_size) / m

#  определение начала интервала
x_start = extreme_1 - h/2

#  инициализация массивов интервалов (bins) и количества вхождений (frequencies)
bins = []
frequencies = []

for i in range(m):
  count = 0
  left = x_start + h * i
  right = x_start + h * (i + 1)
  for val in variation_series:
    if val >= left and val < right:
      count += 1
  frequencies.append(count / n / h)
  bins.append((left + right) / 2)

plt.bar(bins, frequencies, width=h, edgecolor='black')
plt.title('Гистограмма частостей')
plt.xlabel('x')
plt.ylabel('p*_i / h')
plt.show()

### Полигон частотностей ###

for i in range(len(frequencies)):
  frequencies[i] *= h

plt.plot(bins, frequencies, marker='*')
plt.xlabel('x')
plt.ylabel('p*_i')
plt.title('Полигон приведенных частостей')
plt.show()

### Полигон частот ###

for i in range(len(frequencies)):
  frequencies[i] *= n

plt.plot(bins, frequencies, marker='*')
plt.xlabel('x')
plt.ylabel('n_i')
plt.title('Полигон приведенных частот')
plt.show()

# Разница между полигоном частот и частостей в том, что именно мы отображаем на оси ординат:
# Частоты - количество
# Частости - относительные частоты

