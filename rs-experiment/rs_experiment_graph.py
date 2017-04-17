# -*- coding: UTF-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager


def douban_alpha_parameter_graph():
    zh_font = font_manager.FontProperties(fname=r'C:\Windows\Fonts\simfang.ttf')
    x = np.arange(0.0, 1.1, 0.1)
    # y_rmse = np.array([0.8034, 0.8023, 0.8011, 0.7969, 0.7978, 0.7988, 0.7999, 0.8045, 0.8056, 0.8067, 0.8095])
    # y_mae = np.array([0.6372, 0.6262, 0.6252, 0.6217, 0.6224, 0.6233, 0.6242, 0.6282, 0.6290, 0.6298, 0.6318])

    # y_rmse = np.array([1.1853, 1.1845, 1.1834, 1.1829, 1.1825, 1.1820, 1.1815, 1.1823, 1.1838, 1.1858, 1.1877])
    y_mae = np.array([0.8990, 0.8985, 0.8973, 0.8968, 0.8961, 0.8954, 0.8940, 0.8943, 0.8956, 0.8984, 0.9002])

    # plt.subplot(121)
    plt.title(u'Foursquare数据集', fontproperties=zh_font)
    plt.plot(x, y_mae, 'bs--')
    plt.ylabel(u'MAE值', fontproperties=zh_font)
    plt.xlabel(u'参数α', fontproperties=zh_font)

    plt.show()


def plot_rmse_mae_histogram(dataset_name, rmse, mae, y_rmse_limit, y_mae_limit):
    index = np.array([0.0, 0.5, 1.0, 1.5])
    bar_width = 0.15
    zh_font = font_manager.FontProperties(fname=r'C:\Windows\Fonts\simfang.ttf')

    plt.figure(1)

    plt.subplot(121)
    plt.bar(index, rmse, width=bar_width, color='r', alpha=0.6)
    plt.title(dataset_name+u'RMSE评测指标', fontproperties=zh_font)
    plt.ylim(ymin=y_rmse_limit[0], ymax=y_rmse_limit[1])
    plt.xticks(index, (u'测试集1', u'测试集2', u'测试集3', u'平均值'), fontproperties=zh_font)

    plt.subplot(122)
    plt.bar(index, mae, width=bar_width, color='b', alpha=0.3)
    plt.title(dataset_name+u'MAE评测指标', fontproperties=zh_font)
    plt.ylim(ymin=y_mae_limit[0], ymax=y_mae_limit[1])
    plt.xticks(index, (u'测试集1', u'测试集2', u'测试集3', u'平均值'), fontproperties=zh_font)

    plt.tight_layout()
    plt.show()


def plot_compare_rmse_mae_histogram(dataset_name, rmse, mae, y_rmse_limit, y_mae_limit):
    index = np.array([0.0, 0.5, 1.0, 1.5, 2.0])
    bar_width = 0.1
    zh_font = font_manager.FontProperties(fname=r'C:\Windows\Fonts\simfang.ttf')

    plt.figure(1)

    plt.subplot(121)
    plt.bar(index, rmse, width=bar_width, color='r', alpha=0.6)
    plt.title(dataset_name+u'RMSE评测指标', fontproperties=zh_font)
    plt.ylim(ymin=y_rmse_limit[0], ymax=y_rmse_limit[1])
    plt.xticks(index, (u'CF', u'SVD', u'α=0.0', u'α=0.6', u'α=1.0'), fontproperties=zh_font)

    plt.subplot(122)
    plt.bar(index, mae, width=bar_width, color='b', alpha=0.3)
    plt.title(dataset_name+u'MAE评测指标', fontproperties=zh_font)
    plt.ylim(ymin=y_mae_limit[0], ymax=y_mae_limit[1])
    plt.xticks(index, (u'CF', u'SVD', u'α=0.0', u'α=0.6', u'α=1.0'), fontproperties=zh_font)

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    rmse = (1.2433, 1.1845, 1.1853, 1.1815, 1.1877)
    mae = (0.9786, 0.8984, 0.8990, 0.8940, 0.9002)
    plot_compare_rmse_mae_histogram(u'Foursquare ', rmse, mae, [1.18, 1.25], [0.89, 0.98])

