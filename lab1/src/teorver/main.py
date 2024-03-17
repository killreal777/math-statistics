import pandas as pd
import numpy as np

import logger
import plots


def read_sample():
    return np.loadtxt('sample5.txt', delimiter=',')


def expected_value(variation_series):
    expected_value = 0
    for value in variation_series:
        expected_value += value / n
    return expected_value


def dispersion(variation_series, expected_value):
    dispersion = 0
    for value in variation_series:
        delta = (value - expected_value)
        dispersion += delta ** 2 / n
    return dispersion


def standard_deviation_library(variation_series):
    return np.std(variation_series)


def statistical_series(variation_series):
    x, counts = np.unique(variation_series, return_counts=True)
    p = counts / len(variation_series)
    F_x = np.cumsum(p)
    data = {'x': x, 'Количество': counts, 'Частости': p, 'F(x)': F_x}
    return pd.DataFrame(data)


def fill_bins_and_frequencies(bins, frequencies):
    for i in range(m):
        count = 0
        left = x_start + h * i
        right = x_start + h * (i + 1)
        for val in variation_series:
            if left <= val < right:
                count += 1
        frequencies.append(count / n / h)
        bins.append((left + right) / 2)


# Выборка
sample = read_sample()
n = sample.size
logger.log_sample(sample, n)

# 1. Вариационный ряд
variation_series = np.sort(sample)
logger.log_variation_series(variation_series)

# 2. Экстремальные значения и размах
extreme_1 = variation_series[0]
extreme_n = variation_series[n - 1]
variation_size = extreme_n - extreme_1
logger.log_extremes(extreme_1, extreme_n, variation_size)

# 3. Оценки математического ожидания и среднеквадратичного отклонения
# a) Математическое ожидание
expected_value = expected_value(variation_series)
logger.log_expected_value(expected_value)

# б) Среднеквадратичное отклонение
dispersion = dispersion(variation_series, expected_value)
standard_deviation = dispersion ** (1 / 2)
fixed_dispersion = dispersion * n / (n - 1)
logger.log_standard_deviation(standard_deviation)
logger.log_dispersions(dispersion, fixed_dispersion)

# 4. Эмпирическая функция распределения и её график
df = statistical_series(variation_series)
logger.log_statistical_series(df)
plots.show_statistical_series(df)

# 5. Построение гистограммы и полигона приведенных частот группированной выборки
m = int(1 + np.log2(n)) + 1  # количество интервалов разбиения
h = variation_size / m  # ширина шага
x_start = extreme_1 - h / 2  # определение начала интервала
bins = []  # инициализация массивов интервалов
frequencies = []  # инициализация количества вхождений
fill_bins_and_frequencies(bins, frequencies)
plots.show_bar_chart(bins, frequencies, h)

# полигон частотностей
for i in range(len(frequencies)):
    frequencies[i] *= h
plots.show_polygon_1(bins, frequencies)

# полигон частот
for i in range(len(frequencies)):
    frequencies[i] *= n
plots.show_polygon_2(bins, frequencies)
