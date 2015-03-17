from pyparsing import Word, alphanums,alphas
from urllib2 import urlopen

import pandas as pd
import numpy as np

import h5py

import os
os.chdir('/home/rahul/Rahul/X')
expression = 'HREF="'+Word(alphanums+':/.')+'"'
atomData =  urlopen('http://kurucz.harvard.edu/atoms/0atoms.readme')
atomUrlList = []
linesUrl = []
levelsUrl = []

#remove interfering data
for i in range(30):
	atomData.readline()

#store urls in memory	
data = atomData.read()
for i,j,k in expression.scanString(data):
	atomUrlList.append(i[1])



for url in atomUrlList:
	uniqueName = url[-5:-1]
	linesUrl.append(url+"gf"+uniqueName+".lines")
	levelsUrl.append(url + "gf"+ uniqueName + ".gam")

data = urlopen('http://kurucz.harvard.edu/atoms/1401/gf1401.gam')
colspaces = [(0,9),(10,12),(13,24),(26,29),(30,42),(43,48)]
dataFrame = pd.read_fwf(data,colspecs=colspaces,skiprows=38,nrows=1764)
levelsFile = pd.HDFStore('tardis.h5')
store['levels_data'] = dataFrame
levels_data = store['levels_data']
store['levels_data'].columns=['elem','index','E','J','label','glande']

for elem in store['levels_data']['elem']:
    print elem[:5]
