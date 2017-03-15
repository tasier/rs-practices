# -*- coding: UTF-8 -*-

from surprise import Dataset
from surprise import Reader
from surprise import SVD
from surprise import evaluate, print_perf

reader = Reader(line_format='user item rating', sep='|')

data = Dataset.load_from_file(r'H:\ratings.dat', reader)
data.split(2)

algo = SVD()

perf = evaluate(algo, data)

print_perf(perf)