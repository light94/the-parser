from pyparsing import Word, alphanums
from urllib2 import urlopen

expression = 'HREF="'+Word(alphanums+':/.')+'"'
atomData =  urlopen('http://kurucz.harvard.edu/atoms/0atoms.readme')
atomUrlList = []

#remove interfering data
for i in range(30):
	atomData.readline()

#store urls in memory	
data = atomData.read()
for i,j,k in expression.scanString(data):
	atomUrlList.append(i[1])

print atomUrlList


