# -*- coding: UTF-8 -*-

import os
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


def get_user_social_dict(filename, sperate):
    '''
    计算用户关注的用户数，用户的粉丝数
    '''
    user_friends = {}
    user_fans = {}
    with open(filename) as f:
        for line in f:
            item = line.split(sperate)
            user, friend = item[0].strip(), item[1].strip()
            if user not in user_friends:
                user_friends[user] = 1
            else:
                user_friends[user] += 1

            if friend not in user_fans:
                user_fans[friend] = 1
            else:
                user_fans[friend] += 1

    return user_friends, user_fans


def get_max_min_avg_dict(mydict):
    tmp_list = []
    for key in mydict:
        tmp_list.append(mydict[key])

    arr = np.array(tmp_list)

    return arr.max(), arr.min(), np.mean(arr)


def plot_social(user_friendsnumber_dict, user_fansnumber_dict):
    friendsnumber_number = {}
    fansnumber_number = {}

    for user in user_friendsnumber_dict:
        number = user_friendsnumber_dict[user]
        if number not in friendsnumber_number:
            friendsnumber_number[number] = 1
        else:
            friendsnumber_number[number] += 1

    for user in user_fansnumber_dict:
        number = user_fansnumber_dict[user]
        if number not in fansnumber_number:
            fansnumber_number[number] = 1
        else:
            fansnumber_number[number] += 1

    friends_point_list = []
    plot_number = 50
    i = 0
    for key in friendsnumber_number:
        if i <= plot_number:
            friends_point_list.append(key)
            friends_point_list.append(friendsnumber_number[key])
            i += 1
        else:
            break

    point_array = np.array(friends_point_list).reshape(len(friends_point_list) / 2, 2)
    friends_x = point_array[:, 0]
    friends_y = point_array[:, 1]

    fans_point_list = []
    i = 0
    for key in fansnumber_number:
        if i <= plot_number:
            fans_point_list.append(key)
            fans_point_list.append(fansnumber_number[key])
            i += 1
        else:
            break

    point_array = np.array(fans_point_list).reshape(len(fans_point_list) / 2, 2)
    fans_x = point_array[:, 0]
    fans_y = point_array[:, 1]

    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    ax1.plot(friends_x, friends_y, 'b.--')
    ax2.plot(fans_x, fans_y, 'g^--')
    zh_font = font_manager.FontProperties(fname=r'C:\Windows\Fonts\simfang.ttf')
    ax1.set_xlabel(u'follwing人数', fontproperties=zh_font)
    ax1.set_ylabel(u'用户数', fontproperties=zh_font)
    ax2.set_xlabel(u'follower人数', fontproperties=zh_font)
    plt.show()


if __name__ == '__main__':
    douban_dir = r'H:\douban_small'
    foursquare_dir = r'H:\foursquare-user-dataset'

    douban_user_book_rating = 'user-book-rating.csv'
    foursquare_user_venue_rating = 'ratings.dat'

    douban_social = 'social_small.csv'
    foursquare_social = 'socialgraph.dat'

    douban_sperate = ','
    foursquare_sperate = ','

    # douban_user_friends, douban_user_fans = get_user_social_dict(join(douban_dir, douban_social), douban_sperate)
    # plot_social(douban_user_friends, douban_user_fans)

    # foursquare_user_friends, foursquare_user_fans = get_user_social_dict(join(foursquare_dir, foursquare_social), foursquare_sperate)
    # plot_social(foursquare_user_friends, foursquare_user_fans)



