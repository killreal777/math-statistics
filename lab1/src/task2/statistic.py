import pandas as pd
import numpy as np


def expected_value(variation_series):
    """Выборочное среднее (матожидание)"""
    expected_value = 0
    for value in variation_series:
        expected_value += value / len(variation_series)
    return expected_value


def dispersion(variation_series, expected_value):
    """Выборочная дисперсия"""
    dispersion = 0
    for value in variation_series:
        delta = (value - expected_value)
        dispersion += delta ** 2 / len(variation_series)
    return dispersion


def median(variation_series, variation_length):
    """Медиана"""
    if variation_length % 2 == 0:
        first_value = variation_series[variation_length // 2 - 1]
        second_value = variation_series[variation_length // 2]
        return (first_value + second_value) / 2
    else:
        return variation_series[variation_length // 2]


def statistical_series(variation_series):
    """Эмпирическая функция распределения"""
    x, counts = np.unique(variation_series, return_counts=True)
    p = counts / len(variation_series)
    F_x = np.cumsum(p)
    data = {'x': x, 'Количество': counts, 'Частости': p, 'F(x)': F_x}
    return pd.DataFrame(data)


def interval_series(variation_series, variation_length):
    extreme_left = variation_series[0]
    extreme_right = variation_series[variation_length - 1]
    variation_size = extreme_right - extreme_left
    intervals_count = int(1 + np.log2(variation_length)) + 1
    step_width = variation_size / intervals_count  # ширина шага
    x_start = extreme_left - step_width / 2  # определение начала интервала
    bins = []  # инициализация массивов интервалов
    frequencies = []  # инициализация количества вхождений

    for i in range(intervals_count):
        count = 0
        left = x_start + step_width * i
        right = x_start + step_width * (i + 1)
        for value in variation_series:
            if left <= value < right:
                count += 1
        frequencies.append(count / variation_length / step_width)
        bins.append((left + right) / 2)

    return {'bins': bins, 'frequencies': frequencies, 'step_width': step_width}
