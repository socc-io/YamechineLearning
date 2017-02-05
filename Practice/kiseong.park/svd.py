#-*- coding: utf-8 -*-
article = open("article.txt").read().decode("utf-8")
# 점 날리기!
import string
exclude = set(string.punctuation)
print exclude

article_line = article.strip().split("\n")
for idx, line in enumerate(article_line):
    s = ''.join([ch for ch in line if ch not in exclude])
    article_line[idx] = s

for line in article_line:
    print line

from konlpy.tag import Twitter
from konlpy.utils import pprint

tknzer = Twitter()
row = tknzer.nouns(article_line[0])
pprint(row)

voca = []
for line in article_line:
    row = tknzer.nouns(line)
    voca.extend(row)

voca = list(set(voca))

pprint (voca)
print len(voca)

voca_idx = {w: idx for idx, w in enumerate(voca)}

pprint(voca_idx)

trg_matrix = []
for line in article_line:
    row = tknzer.nouns(line)
    bag_of_word = [0 for x in range(len(voca))]
    for word in row:
        if word in voca:
            bag_of_word[voca_idx[word]] += 1
    trg_matrix.append(bag_of_word)

print trg_matrix



import numpy as np 
feat_mat = np.array(trg_matrix)
U,s,vh = np.linalg.svd(feat_mat, full_matrices=False)
Wonhae = np.matmul(U,np.diag(s))
print Wonhae

mutual_point = np.matmul(Wonhae, np.transpose(Wonhae)).sum(axis=1)

print mutual_point
rank = np.argsort(mutual_point)[::-1]
print rank

for r in rank:
    print "(point : ", mutual_point[r], ") ", article_line[r]
