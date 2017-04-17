# -*- coding: UTF-8 -*-

import numpy as np
from os.path import join
from collections import defaultdict
from surprise import AlgoBase, KNNBasic
from surprise import Dataset, evaluate, Reader
from surprise import print_perf
from surprise import PredictionImpossible
import logging
logging.basicConfig(filename='sbmf.log', level=logging.DEBUG)


class SBMF(AlgoBase):
    def __init__(self, sim_options, social_file,
                 n_factor=100, n_epochs=10,
                 lr=.005, reg=.02, alpha=0.5):
        self.n_factor = n_factor
        self.n_epochs = n_epochs
        self.lr = lr
        self.reg = reg
        self.alpha = alpha
        self.social_file = social_file

        AlgoBase.__init__(self, sim_options=sim_options)

    def train(self, trainset):
        AlgoBase.train(self, trainset)
        self.trainset = trainset

        self.sim = self.compute_similarities()
        self.iuid_ifriends = self.read_social(trainset)

        self.sbmf(trainset)

    def read_social(self, trainset):
        user_friends = defaultdict(list)
        with open(self.social_file) as f:
            for line in f:
                users = line.strip().split(',')
                user, friend = users[0], users[1]
                try:
                    inner_uid = trainset.to_inner_uid(user)
                    inner_friend_uid = trainset.to_inner_uid(friend)
                    user_friends[inner_uid].append(inner_friend_uid)
                except Exception, e:
                    logging.error(e)

        return user_friends

    def sbmf(self, trainset):
        print '--------------'+str(self.alpha)+'--------------'
        bu_inner = np.zeros(trainset.n_users, np.double)
        bu_social = np.zeros(trainset.n_users, np.double)
        bi = np.zeros(trainset.n_items, np.double)
        pu = np.zeros((trainset.n_users, self.n_factor), np.double) + .1
        qi = np.zeros((trainset.n_items, self.n_factor), np.double) + .1

        global_mean = trainset.global_mean
        alpha = self.alpha
        belta = 1.0 - self.alpha

        lr = self.lr
        reg = self.reg

        sim = self.sim

        for current_epoch in range(self.n_epochs):
            # print 'current epoch', current_epoch
            for u, i, r in trainset.all_ratings():
                # print u, i, r
                u_friends = self.iuid_ifriends[u]
                total_s_uf_puf = 0.
                total_s_uf = 0.

                # pus
                pu_social = np.zeros(self.n_factor, np.double)

                for friend in u_friends:
                    s_uf = sim[u, friend]
                    total_s_uf += s_uf
                    total_s_uf_puf += s_uf * np.linalg.norm(pu[u] - pu[friend])

                    pu_social += s_uf * (pu[u] - pu[friend])

                if cmp(total_s_uf, 0.0) != 0:
                    bu_social[u] = total_s_uf_puf / total_s_uf
                    pu_social /= total_s_uf

                dot = 0
                for f in range(self.n_factor):
                    dot += qi[i, f] * pu[u, f]
                err = r - (global_mean + bi[i] + belta*bu_inner[u] + alpha*bu_social[u] + dot)

                bi[i] += lr * (err - reg*bi[i])
                bu_inner[u] += lr*belta * (err - reg*belta*bu_inner[u])

                for f in range(self.n_factor):
                    puf = pu[u, f]
                    qif = qi[i, f]
                    pu[u, f] += lr * (err*(qif + alpha*pu_social[f]) - reg*puf)
                    qi[i, f] += lr * (err*puf - reg*qif)

        self.bu_inner = bu_inner
        self.bu_social = bu_social
        self.bi = bi
        self.pu = pu
        self.qi = qi


    def estimate(self, u, i):
        alpha = self.alpha
        belta = 1. - alpha

        est = self.trainset.global_mean

        if self.trainset.knows_user(u):
            est += belta * self.bu_inner[u]
            est += alpha * self.bu_social[u]

        if self.trainset.knows_item(i):
            est += self.bi[i]

        if self.trainset.knows_user(u) and self.trainset.knows_item(i):
            est += np.dot(self.qi[i], self.pu[u])
        else:
            raise PredictionImpossible

        return est


if __name__ == '__main__':
    douban_dir = r'./'
    foursquare_dir = r'./'

    douban_user_book_rating = 'user-book-rating.csv'
    foursquare_user_venue_rating = 'ratings_small.dat'

    douban_social = 'social_small.csv'
    foursquare_social = 'socialgraph_small.dat'


    reader = Reader(line_format='user item rating', sep=',')
    data = Dataset.load_from_file(join(douban_dir, douban_user_book_rating), reader)
    data.split(n_folds=3)

    sim_options = {'name': 'msd', 'user_based': True}

    for alpha in np.arange(0.0, 1.1, 0.1):
        print '=============start '+str(alpha)+'================='
        algo = SBMF(sim_options, join(douban_dir, douban_social), alpha=alpha)
        perf = evaluate(algo, data, measures=['RMSE', 'MAE'])
        print_perf(perf)
        print '=================end============================'


