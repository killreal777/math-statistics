import matplotlib.pyplot as plt


def show_statistical_series(df):
    """График эмпирической функции распределения"""
    plt.step(df['x'], df['F(x)'], where='post')
    plt.title('Эмпирическая функция распределения')
    plt.xlabel('x')
    plt.ylabel('F(x)')
    plt.show()


def show_bar_chart(interval_series):
    """Гистограмма распределения"""
    plt.bar(interval_series['bins'], interval_series['frequencies'], width=interval_series['step_width'], edgecolor='black')
    plt.title('Гистограмма частостей')
    plt.xlabel('x')
    plt.ylabel('p*_i / h')
    plt.show()

