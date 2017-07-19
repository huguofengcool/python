import os, sys

def loadfileAndgetlabel(filename):
	filelists=[]
	with open(filename,'r') as fl:
		readlines=fl.readlines()
		for line in readlines:
			line=line.strip().split()
			filelists.append(line[1])
	return filelists

def writeTofile(filelists,labelfile):
	label=[]
	label=filelists
	with open(labelfile,'w+') as lf:
		for line in label:
			lf.write(line+'\n')

if __name__=="__main__":
	if len(sys.argv)!=3:
		print 'Usage: python *.py inputfile outputfile'
		exit(1)
	f=loadfileAndgetlabel(sys.argv[1])
	writeTofile(f,sys.argv[2])
	print 'Done'
