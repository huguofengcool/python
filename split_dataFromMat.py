import sys
import scipy.io as scio
import numpy
import time

def readMat(matFile):
	data=scio.loadmat(matFile)
	dataMat=data['feats']
	datalist=dataMat.tolist()
	return datalist
'''
def matTolist(array):
	row, column=array.shape
	matlist=[]
	for r in xrange(row):
		for c in xrange(column):
			matlist.append(array[i,j])
		array[-1,-1]=array[-1,-1]+'/n'
	return matlist
'''
def loadlabel(filename):
	filelists=[]
	with open(filename,'r') as fn:
		for rline in fn.readlines():
			rline=rline.strip()
			rline=rline+'\n'
			filelists.append(rline)

	return filelists

def splitfile(filename1,filename2):
	fn1=readMat(filename1)
	fn2=loadlabel(filename2)
	for n in xrange(26):    ###26-labels(for example: 1 2 3 4 1 2 3    sum:7)
		tempfile=[]		
		number=0
		for i in xrange(len(fn2)-1):
			if fn2[i]==fn2[i+1]:
				number+=1
			else: break
		number+=1	
		for j in xrange(number):
			tempfile.append(fn1[j])
			tempfile.append('\n')
		writefile=str(n)+'.txt'
		with open(writefile,'w+') as wf:
			for line in tempfile:
				for l in line:
					wf.write(str(l)+' ')
				wf.write('\n')
		for m in xrange(number):
			fn1.pop(0)
			fn2.pop(0)

if __name__ == '__main__':
	if len(sys.argv)!=3:
		print 'Usage: python *.py datafile labelfile'
		exit(1)
	print 'It begins, just wait...'
	starttime=time.clock()
	splitfile(sys.argv[1],sys.argv[2])
	endtime=time.clock()
	print 'Done'	
	print 'It uses %d seconds' %(endtime-starttime)
