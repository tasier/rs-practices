# -*- coding: UTF-8 -*-

import csv

if __name__ == '__main__':
    csvfilename = r'H:\ml-latest-small\test.csv'
    with open(csvfilename, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print row