import numpy as np

for chipID in range(4):
	for coreID in range(1,17):
		seed=[]
		for i in range(4):
			seed.append(i + (coreID | (chipID+1)<<i))
		print 'core{} on chip{} has seeds={}'.format(coreID,chipID,seed)

