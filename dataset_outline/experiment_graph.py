# -*- coding: UTF-8 -*-

from os.path import join
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np


def douban_rating_proportion_graph():
    '''
    豆瓣评分比例图
    '''
    labels = '1', '2', '3', '4', '5'
    sizes = [0.88, 3.07, 21.85, 39.72, 34.48]
    explode = (0, 0, 0, 0.1, 0)
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:purple', 'tab:olive']

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%.2f%%',
            shadow=True, colors=colors)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

def foursquare_rating_proportion_graph():
    '''
    豆瓣评分比例图
    '''
    labels = '1', '2', '3', '4', '5'
    sizes = [4.99, 34.36, 8.34, 21.27, 31.02]
    explode = (0, 0.1, 0, 0, 0)
    # colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:purple', 'tab:olive']

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%.2f%%',
            shadow=True, startangle=80)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()


def get_objectnumber_usernumber(filename, sperate):
    user_number = {}
    with open(filename) as fr:
        for line in fr:
            user = line.split(sperate)[0].strip()
            if user not in user_number:
                user_number[user] = 1
            else:
                user_number[user] += 1

    object_number = {}
    for user in user_number:
        number = user_number[user]
        if number not in object_number:
            object_number[number] = 1
        else:
            object_number[number] += 1

    for number in object_number:
        print number, object_number[number]

    return object_number


def plot_objectnumber_usernumber(objectnumber_usernumber, plot_number, xlabel, ylabel):
    tmp_point_list = []
    i = 0
    for key in objectnumber_usernumber:
        if i <= plot_number:
            tmp_point_list.append(key)
            tmp_point_list.append(objectnumber_usernumber[key])
            i += 1
        else:
            break

    point_array = np.array(tmp_point_list).reshape(len(tmp_point_list)/2, 2)
    x = point_array[:, 0]
    y = point_array[:, 1]

    plt.plot(x, y, linestyle='--', marker='.', color='b')
    zh_font = font_manager.FontProperties(fname=r'C:\Windows\Fonts\simfang.ttf')
    plt.xlabel(xlabel, fontproperties=zh_font)
    plt.ylabel(ylabel, fontproperties=zh_font)
    plt.show()



if __name__ == '__main__':
    douban_dir = r'H:\douban_small'
    foursquare_dir = r'H:\foursquare-user-dataset'

    douban_user_book_rating = 'user-book-rating.csv'
    foursquare_user_venue_rating = 'ratings.dat'

    douban_sperate = ','
    foursquare_sperate = '|'

    # douban_dict = get_objectnumber_usernumber(join(douban_dir, douban_user_book_rating), douban_sperate)
    # plot_objectnumber_usernumber(douban_dict, 200, u'书籍数', u'用户数')

    foursquare_dict = get_objectnumber_usernumber(join(foursquare_dir, foursquare_user_venue_rating), foursquare_sperate)
    plot_objectnumber_usernumber(foursquare_dict, 80, u'地点数', u'用户数')










