import random
from matplotlib import pyplot as plt

#TODO

dict_month = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

list_month = ["January", "February", "March", "April", "May", "June", "August", "September", "October", "November", "December"]
month_day = dict_month[random.choice(list_month)]
month_days = [day+1 for day in range(month_day)]


def prices_stocks(
        days: int, stock_count: int) -> dict:
    """
    Функция принимает:
    1. Количество дней в месяце
    2. Количество акций, торгуемое на бирже
    Функция возвращает:
    1. Словарь, ключ - это каждая акция, значение - список стоимости этой акции за количество дней в месяце
    """
    if stock_count > 10:
        print("Количество акций не может быть больше 10")
        return 0
    NAME_STOCK = ["Pepsi", "BMW", "Apple", "Google", "Microsoft", "Coca-cola", "Billa", "Lenta", "Skyeng", "Fix-price"]
    random.shuffle(NAME_STOCK)
    name_stocks = NAME_STOCK[:stock_count]
    dict_price_stocks = {}
    for item_stock in range(stock_count):
        name_stock = random.choice(name_stocks)
        index = 0
        for item_name_stock in range(len(name_stock)):
            if name_stock == name_stocks[item_name_stock]:
                index = item_name_stock
        name_stocks.pop(index)
        dict_price_stocks[name_stock] = [float(random.randint(100, 500)) for item in range(days)]
    return dict_price_stocks


stocks_count = random.randint(2, 10)
dict_price_stocks_value = prices_stocks(month_day, stocks_count)


def draw_plot_price_for_stock(
        dict_price_stocks: dict, days: int) -> list:
    """
    Генерирует параметры для функций библиотеки matplotlib и для визуализации
    возвращает 2 списка
    """
    x = [digital for digital in range(days)]
    show_plot = []
    show_legend = []
    for key in dict_price_stocks:
        y = dict_price_stocks[key]
        show_plot.append(plt.plot(x, y))
        show_legend.append(key)
    show_result_plot = [show_plot, show_legend]
    return show_result_plot


show_result = draw_plot_price_for_stock(dict_price_stocks_value, month_day)


def draw_plot(
        show_p: list) -> None:
    """
    Функция визуализирует общий график
    """
    for item in range(len(show_p[0])):
        plt.legend([show_p[1][item]])
        plt.plot(show_p[0][item])
        plt.show()


draw_plot(show_result)