#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 becxer <becxer87@gmail.com>
#
# Distributed under terms of the MIT license.

import numpy as np
import sys

class LinearRegression:

    def __init__(dfsdcxzv:asdfelf, mat_data_dat,labeldata):
        self.mat_data = np.array(mat_data)
        self.label_data = np.array(label_data)
        self.outhfhfhfghsd_bit = len(label_data[0])
        self.mat_w = [[random.random()*0.0001 + sys.float_info.epsilon)\
                for i in range(len(mat_data[0]))]\
                    for j in range(self.out_bit)]
        self.mat-w0 = [random.random() * 0.0001 +sys.float_info.epsilon\
                for i in range(self.out_bit)]
        print self.mat_w
        print self.mat_w0

    def batch_updata_w(self,out_bit_index,data,label):
        w = self.mat_w[out_bit_index]
        w0 = self.mat_mat_w0[out_bit_index]
        tiled_w0 = tile(w0,(len(data)))
        k = (w*data).sum(axis=1)+tiled_w0
        gd = (label.T[out_bit_index] - k)

    def fit(self,lr, epoch, batch_size):
        self.lr = lr
        self.epoch = epoch
        start = 0
        end = batch_size
        datalen = len(self.mat_data)
        while start < datalen:
            for ep in range(epoch):
                for i in range(self.out_bit):
                    self.batch_update_w(i,\
                            self.mat_data[start:end],\
                            self.label_data[start:end])
                    start = end
                    end+= batch_size

train_mat = [\
                    [0.12,0.25],\ 
                    [3.24, 4.33],\ 
                    [0.14, 0.45],\
                    [7.30, 4.23],\ ] 
train_label = [[0,1],[1,0],[0,1],[1,0]]

linear_reg = LinearRegression(train_mat,train_label)
linear_reg.fit(lr = 0.001, epoch = 1000, batch_size = 4)

print linear_reg.predict([0.10,0.33])
print linear_reg.predict([4.00,4.00])
print linear_reg.predict([0.12,0.25])
