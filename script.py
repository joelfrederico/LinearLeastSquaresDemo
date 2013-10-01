#!/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import mytools as mt
import collections as col

plt.close('all')

# Functional relationship
def myfun(x):
	sig_fun = 0
	y = 1 + np.random.randn(len(x)) * sig_fun
	# y = 1
	return y*x

def iter():
	
	num_pts = 10000
	sig = 10
	
	x = np.random.randn(num_pts)*3
	# x = np.ones(num_pts)
	
	y = myfun(x) + np.random.randn(num_pts)*sig
	
	# mt.hist2d(x,y,bins=50)
	
	x = np.array([x]).transpose()
	y = np.array([y]).transpose()
	
	A = x / sig
	B = y / sig
	beta = np.dot(np.linalg.pinv(A),B)
	
	covar = np.linalg.inv(np.dot(np.transpose(A),A))
	
	# print '-------'
	# print beta
	# print covar
	# print np.sqrt(covar)
	output = col.namedtuple('fitbowtie_output',['beta','covar','x','y'])
	out = output(beta,covar,x,y)
	return out

num_samples = 1000
variances = np.ones(num_samples)
for i in np.linspace(1,num_samples,num_samples)-1:
	out = iter()
	variances[i] = out.beta
	# mt.hist2d(out.x.flatten(),out.y.flatten(),bins=70)

plt.hist(variances)
# print 'Std Dev. is {}'.format(np.std(variances))
