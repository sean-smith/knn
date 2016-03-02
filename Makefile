# Makefile for testing homework 2 programming part 

k = 3

crx: preprocess run_

lenses: run_lenses

preprocess:
	./process crx.data.training crx.data.testing

run_:
	./run $(k) crx.testing.processed crx.training.processed

run_lenses:
	./run $(k) lenses.testing lenses.training
