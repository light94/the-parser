from pyparsing import Word, alphanums,alphas
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

#print atomUrlList
# atomUrlList = ['http://kurucz.harvard.edu/atoms/0400/']

#now see if .gam file regarding each atom is present or not.

dataFile = []
filename = Word(alphanums)+".gam"
for url in atomUrlList:
	fileListing = urlopen(url).read()
	generator = filename.scanString(fileListing)
	dataFile.append(next(generator,None))
