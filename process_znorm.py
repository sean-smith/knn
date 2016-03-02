import pandas as pd
import numpy as np
import sys

def process(X):

	# columns to fill
	fill_in = [0,3,4,5,6]

	X = X.replace('?', np.NaN)

	for i in fill_in:
		X[i] = X[i].fillna(X[i].mode()[0])
		print "filled in column", i

	# continous columns that need to be imputated
	fill_in = [1,13]
	class_ = ['+', '-']
	for col in fill_in:
		X[col] = X[col].apply(float)
		for c in class_:
			X.loc[ (X[col].isnull()) & ( X[15]==c ), col ] = X[col][X[15] == c].mean()

	return X

def znorm(X):
	cols = [1,2,7,10,13,14]
	for col in cols:
		X[col] = (X[col] - X[col].mean())/X[col].std()
	return X



# read in csv
if len(sys.argv) > 1:
	for file in sys.argv[1:]:
		print file
		df = pd.read_csv(file, header=None)
		df = process(df)
		df = znorm(df)
		if file == "crx.data.testing":
			outfile = "crx.testing.processed"
		elif file == "crx.data.training":
			outfile = "crx.training.processed"
		elif file == "lenses.testing":
			outfile = "lenses.testing.processed"
		elif file == "lenses.training":
			outfile = "lenses.training.processed"
		df.to_csv(outfile, header=False, index=False)
else:
	print("Please enter a file name.")