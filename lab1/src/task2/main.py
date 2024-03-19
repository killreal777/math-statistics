import data
import statistic


species_areas = data.get_data()

# Вывод количества экзкемпляров по видам
for key in species_areas.keys():
    print(key, len(species_areas[key]))


for key in species_areas.keys():
    variation_series = species_areas[key]
    variation_length = len(variation_series)
    expected_value = statistic.expected_value(variation_series)
    dispersion = statistic.dispersion(variation_series, expected_value)
    median = statistic.median(variation_series, variation_length)
    print(expected_value, dispersion, median)


# Выборочные среднее и дисперия
