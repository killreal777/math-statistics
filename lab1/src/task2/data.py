import pandas as pd


def get_area(line):
    """Сумарная площадь из строки данных"""
    length1 = line[0]
    width1 = line[1]
    area1 = length1 * width1
    length2 = line[2]
    width2 = line[3]
    area2 = length2 * width2
    return area1 + area2


def get_specie(line):
    """Вид из строки данных"""
    return line[4]


def get_data():
    """Словарь со списками суммарных площадей по видам"""

    # Чтение файла
    data = pd.read_csv('iris.csv').to_numpy()

    # Словарь: ключ - вид, значение - список суммарных площадей по строкам данных
    species_areas = {
        'all': [],
        'setosa': [],
        'versicolor': [],
        'virginica': []
    }

    # Заполнение словаря
    for line in data:
        specie = get_specie(line)
        species_areas[specie].append(get_area(line))
        species_areas['all'].append(get_area(line))

    # Сортировка списков словаря
    for key in species_areas.keys():
        species_areas[key].sort()

    return species_areas
