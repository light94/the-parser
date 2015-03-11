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

#dataFile = []
filename = Word(alphanums)+".gam"
for url in atomUrlList:
	fileListing = urlopen(url).read()
	generator = filename.scanString(fileListing)
	#dataFile.append(next(generator,None))
	data = urlopen(next(generator,None)).read()
	create_dictionary(data)


def create_dictionary(data):
	

	#read atom detail which is 5 characters long
	atom = data.read(5)

	dictionary = {}
	dictionary['atom'] = atom

	label = delimitedList(Word(alphas+'-'+nums), delim=' ', combine=True)
	line = Word(nums) + label

	#create dictionary to store observation metadata for atom = 'atom'
	for line_tokens, start_location, end_location in line.scanString(data.readline()):
		dictionary[line_tokens[1]] = line_tokens[0]	

	print dictionary
