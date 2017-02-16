# -*- coding: utf-8 -*-

import MeCab
import sys

tagger = MeCab.Tagger('-d /usr/lib/mecab/dic/mecab-ipadic-neologd/ -F\s%f[6] -U\s%m -E\\n')

fi = open(sys.argv[1],'r')
fo = open(sys.argv[2],'w')

line = fi.readline()
while line:
    result = tagger.parse(line)
    fo.write(result[1:])
    line = fi.readline()

fi.close()
fo.close()
