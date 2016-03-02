# Homework 2 Programming Part

I created an executable `process` which can be run to pre-process the data. It fills in gaps and normalizes the data using znorm. Run it like so:

	./processed crx.data.training crx.data.testing

This will output two files `crx.training.processed` and `crx.testing.processed`. 

Next feed this into the knn algorithm with k = 3.

	./run 3 crx.testing.processed crx.training.processed

This will produce a file `testing_k3` which can be piped into the program `accuracy.pl` to get the percent correct.

	cat testing_k3 | perl accuracy.pl

The results from 1 <= k <= 10 for `crx.testing.processed` are in the file `results.csv`.

