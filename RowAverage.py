def rowAverageSum(filename):
	import numpy as np
	FullMean = 0
	li = [map(int, x) for x in [i.strip().split() for i in open(filename).readlines()]]
	i=0
	while i<len(li):
		for k in li:
			print "Mean of row ",i+1,":",np.mean(k)
			FullMean+=np.mean(k)
			i+=1
	print "***************************"
	print "Grand Average:",FullMean
	print "***************************"
