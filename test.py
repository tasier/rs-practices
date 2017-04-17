# -*- coding: UTF-8 -*-

from surprise import Dataset
from surprise import Reader
from surprise import SVD
from surprise import KNNBasic,KNNWithMeans,KNNBaseline
from surprise import NormalPredictor
from surprise import BaselineOnly
from surprise import SlopeOne
from surprise import evaluate, print_perf
from surprise import CoClustering
from surprise import GridSearch
from surprise import accuracy
from os.path import join


if __name__ == '__main__':
    douban_dir = r'H:\douban_small'
    foursquare_dir = r'H:\foursquare-user-dataset'

    douban_user_book_rating = 'user-book-rating.csv'
    foursquare_user_venue_rating = 'ratings_small.dat'

    douban_social = 'social_small.csv'
    foursquare_social = 'socialgraph_small.dat'

    douban_sperate = ','
    foursquare_sperate = ','

    reader = Reader(line_format='user item rating', sep=',')
    data = Dataset.load_from_file(join(foursquare_dir, foursquare_user_venue_rating), reader)
    data.split(n_folds=3)

    algo = SVD()
    perf = evaluate(algo, data, measures=['RMSE', 'MAE'])
    print_perf(perf)


























