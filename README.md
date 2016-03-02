# Homework 2 Programming Part

I created an executable `process` which can be run to pre-process the data. It fills in gaps and normalizes the data using znorm. Run it like so:

	./processed crx.data.training crx.data.testing

This will output two files `crx.training.processed` and `crx.testing.processed`. 

Next feed this into the knn algorithm with k = 3.

	./run 3 crx.testing.processed crx.training.processed

This will produce a file `testing_k3` which can be piped into the program `accuracy.pl` to get the percent correct.

	cat testing_k3 | perl accuracy.pl

The results from 1 <= k <= 10 for `crx.testing.processed` are in the file `results.csv` and listed below:


| K     | Accuracy Rate   |
| ----- | --------------- |
| 1 | 0.826086956521739 |
| 2 | 0.826086956521739 |
| 3 | 0.855072463768116 |
| 4 | 0.847826086956522 |
| 5 | 0.847826086956522 |
| 6 | 0.869565217391304 |
| 7 | 0.847826086956522 |
| 8 | 0.833333333333333 |
| 9 | 0.86231884057971 |
| 10 | 0.847826086956522 |