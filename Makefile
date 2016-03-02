# Makefile for testing homework 2 programming part 

k = 3

crx: preprocess run show

lenses: lenses_preprocess run_lenses show

preprocess:
	./processed crx.data.training crx.data.testing

lenses_preprocess:
	./processed lenses.training lenses.testing

run:
	./run $(k) crx.testing.processed crx.training.processed

run_lenses:
	./run $(k) lenses.testing.processed lenses.training.processed

show:
	cat testing_k$(k) | perl accuracy.pl