# -*- coding: UTF-8 -*-

from surprise import Dataset
from surprise import Reader
from surprise import SVD
from surprise import evaluate, print_perf


if __name__ == '__main__':
    reader = Reader(line_format='user item rating', sep='|')

    data = Dataset.load_from_file('/home/binjie/ratings.dat', reader)
    data.split(2)

    algo = SVD(n_factors=1000)

    perf = evaluate(algo, data)

    print_perf(perf)