def log_sample(sample, n):
    print('Выборка:', sample)
    print('Размер:', n)
    print()


def log_variation_series(variation_series):
    print('Вариационный ряд')
    print(variation_series)
    print()


def log_extremes(extreme_1, extreme_n, variation_size):
    print('Первая порядковая статистика x(1) =', extreme_1)
    print('n-ая порядковая статистика x(n) =', extreme_n)
    print('Размах выборки w* =', variation_size)
    print()


def log_expected_value(expected_value):
    print('Математическое ожидание M =', expected_value)
    print()


def log_standard_deviation(standard_deviation):
    print('Среднеквадратичное отклонение sigma =', standard_deviation)
    print()


def log_dispersions(dispersion, fixed_dispersion):
    print('Выборочная дисперсия dispersion =', dispersion)
    print('Исправленное СКО s^2 = :', fixed_dispersion)
    print()


def log_statistical_series(df):
    print(df[['x', 'F(x)']])
    print()
