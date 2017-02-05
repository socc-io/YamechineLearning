#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 becxer <becxer87@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Singular Vector Decomposition
"""

import os, sys, time, random, base64, socket, string
from struct import pack, unpack
from konlpy.tag import Twitter
from konlpy.utils import pprint
import numpy as np

def preprocess(s, excludeCharset) :
    return ''.join(ch for ch in s if ch not in excludeCharset)

class Line() :
    def __init__(self, parent, raw='', nouns=None) :
        self.raw = raw
        self.parent = parent
        if nouns :
            self.nouns = nouns
        else :
            self.nouns = list()
    def updateVector(self) :
        voca_dic = self.parent.voca_dic
        vocas = self.parent.vocas
        vector = [0 for x in range(len(vocas))]
        for noun in self.nouns :
            idx = voca_dic[noun]
            vector[idx] = 1
        self.vector = np.array(vector)
    def printVector(self) :
        if self.vector :
            print ''.join(str(ch) for ch in self.vector)

class SVD() :
    def __init__(self) :
        self.article = u'Initial sample article'
    def readFromFile(self, path) :
        try :
            f = open(path,'r')
            self.article = unicode(f.read().decode('utf-8'))
            f.close()
        except e :
            print 'failed to read file {}'.format(path)
    def preprocess(self, excludeCharset=string.punctuation) :
        self.article = preprocess(self.article, excludeCharset)
        raw_lines = self.article.split('\n')
        tknzer = Twitter()
        lines = list()
        vocas = list()
        for raw_line in raw_lines :
            if len(raw_line) < 2: continue
            nouns = tknzer.nouns(raw_line)
            line_obj = Line(self, raw_line, nouns)
            lines.append(line_obj)
            vocas += nouns
        voca_dic = { w : idx for idx, w in enumerate(vocas) }
        self.lines = lines
        self.vocas = vocas
        self.voca_dic = voca_dic
        for line in lines :
            line.updateVector()
        feat_mat = np.array([line.vector for line in self.lines])
        U,s,Vh = np.linalg.svd(feat_mat, full_matrices=False)
        Wonhae = np.matmul(U,np.diag(s))
        mutual_point = np.matmul(Wonhae, np.transpose(Wonhae)).sum(axis=1)
        ranks = np.argsort(mutual_point)[::-1]
        for idx, rank in enumerate(ranks) :
            print 'rank',idx,'point:',mutual_point[rank],':',lines[rank].raw
def main(args=[]) :
    svd = SVD()
    svd.readFromFile('./article.txt')
    svd.preprocess()


if __name__ == '__main__' :
    main()
