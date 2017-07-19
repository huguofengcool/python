filelist=[]
with open('train.txt','r') as ta:
	readlist=ta.readlines()
	for line in readlist:
		line=line.strip().split()
		line=line.pop(0)
		filelist.append(line)
with open('train1.txt','w+') as ta1:
	for readline in filelist:
		ta1.write(readline+'\n')

