# Sean Smith k nearest neighbors
import pandas as pd
import numpy as np
import sys
import math
from heapq import heappush, heappop

def knn(testing, training, k):
	l = testing.shape[1]
	testing[l] = np.NaN
	for r in testing.iterrows():
		label = nearest_neighbors(k, r, training, l)
		testing.ix[r[0], l] = label
	return testing

def nearest_neighbors(k, r, b, l):
	h = []
	for r_2 in b.iterrows():
		label = r_2[1][l-1]
		heappush(h, (distance(r, r_2), label))

	lst = []
	for i in range(int(k)):
		d, label = heappop(h)
		lst += [label]
	return max(set(lst), key=lst.count)

def distance(a,b):
	d_sum = 0
	l = len(b[1])
	for col in range(l - 1):
		if not isinstance(a[1][col], str):
			d_sum += math.pow((a[1][col] - b[1][col]), 2)
		else:
			if not a[1][col] == b[1][col]:
				d_sum += 1

	return math.sqrt(d_sum)

# read in csv
if len(sys.argv) > 3:
	k = int(sys.argv[1])
	print "k =",k
	for file in sys.argv[2:]:
		testing_data = pd.read_csv(sys.argv[2], header=None)
		training_data = pd.read_csv(sys.argv[3], header=None)
		testing_data = knn(testing_data, training_data, k)
		testing_data.to_csv("testing_k"+str(k), header=False, index=False)
else:
	print("Please enter a file name.")