import numpy as np
import pandas as p
import matplotlib.pyplot as plt
import scipy.io as sio
from scipy.stats import pearsonr


def plot(a, index):
	b = [i for i in range(1961,1974)]
	z = ["FTP", "UEMP", "MAN", "LIC", "GR", "NMAN", "GOV", "HE", "WE", "HOM"]
	plt.plot(b,a[:,index], label = z[index])
	plt.xlabel("Years")
	plt.legend()

	
	

a = sio.loadmat("detroit.mat")['data']


# Normalize
a = (a - a.min(0))/a.ptp(0)


for i in range(1, 9):
	plot(a, 0)
	plot(a, -2)
	plot(a, -1)
	plot(a,i)
	print(pearsonr(a[:,i], a[:,-1]))
	plt.show()




# print(a)