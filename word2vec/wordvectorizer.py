from gensim.models import Word2Vec
from gensim import utils
import random


lines=open('cordata/hy_wikipedia.cor').readlines()+open('cordata/encyclopedia_am.cor').readlines()+open('cordata/parlament_am.cor').readlines()+open('cordata/pdfs.cor').readlines()+open('cordata/hrantmatevosian.cor').readlines()
random.shuffle(lines)

open('comb.cor', 'w').writelines(set(lines))

class   CorpusGen(object):

    def __iter__(self):
        for line in open('comb.cor'):
            yield utils.simple_preprocess(line) # preprocessing data

sentences = CorpusGen()


modelvec=Word2Vec(sentences=sentences,size=16,workers=256,min_count=2) 


modelvec.save("word2vec.model")