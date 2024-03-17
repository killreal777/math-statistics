import matplotlib.pyplot as plt


def show_statistical_series(df):
    plt.step(df['x'], df['F(x)'], where='post')
    plt.title('Эмпирическая функция распределения')
    plt.xlabel('x')
    plt.ylabel('F(x)')
    plt.show()


def show_bar_chart(bins, frequencies, h):
    plt.bar(bins, frequencies, width=h, edgecolor='black')
    plt.title('Гистограмма частостей')
    plt.xlabel('x')
    plt.ylabel('p*_i / h')
    plt.show()


def show_polygon_1(bins, frequencies):
    plt.plot(bins, frequencies, marker='*')
    plt.xlabel('x')
    plt.ylabel('p*_i')
    plt.title('Полигон приведенных частостей')
    plt.show()


def show_polygon_2(bins, frequencies):
    plt.plot(bins, frequencies, marker='*')
    plt.xlabel('x')
    plt.ylabel('n_i')
    plt.title('Полигон приведенных частот')
    plt.show()
