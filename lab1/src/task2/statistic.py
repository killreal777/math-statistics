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
