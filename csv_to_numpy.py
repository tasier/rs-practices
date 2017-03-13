# -*- coding: UTF-8 -*-


import numpy as np

if __name__ == '__main__':
    csvfilename = r'H:\ml-latest-small\test.csv'
    print np.genfromtxt(csvfilename, delimiter=',', dtype=None)