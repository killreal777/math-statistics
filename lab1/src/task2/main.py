import data
import statistic
import plots


species_areas = data.get_dictionary()

# Вывод количества экзкемпляров по видам
for key in species_areas.keys():
    print(key, len(species_areas[key]))


for key in species_areas.keys():
    variation_series = species_areas[key]
    variation_length = len(variation_series)
    expected_value = statistic.expected_value(variation_series)
    dispersion = statistic.dispersion(variation_series, expected_value)
    median = statistic.median(variation_series, variation_length)
    statistical_series = statistic.statistical_series(variation_series)
    interval_series = statistic.interval_series(variation_series, variation_length)
    plots.show_bar_chart(interval_series)
