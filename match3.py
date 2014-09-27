# This file reads the Google descriptions collected in match2.py and does a 
# simple word frequency count. 

import operator, re
from collections import Counter

with open('descriptions_google.txt', 'r') as myFile: 
  data = myFile.read().replace('\n', '').lower().strip(',')

words = re.split('\s+', data)

wf = {}
for w in words: 
  if w in wf: wf[w] = wf[w] + 1
  else: wf[w] = 1

wfs = sorted(wf.iteritems(), key = operator.itemgetter(1), reverse=True)

for i in wfs: 
  print i
