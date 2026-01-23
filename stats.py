import random
import numpy as np

def RandomSampling(func, xbounds, ybounds, max_iters = 1000):
	num_iterations = 0
	while num_iterations < max_iters:
		xvalue = random.uniform(xbounds[0],xbounds[1])
		yvalue = random.uniform(ybounds[0],ybounds[1])
		if yvalue < func(xvalue):
			return (xvalue,yvalue,num_iterations)
		num_iterations += 1
	return (float('nan'),float('nan'),num_iterations)

def MetropolisHastingsStep(func, x, dx):
	step = random.uniform(-1,1)*dx
	xp = x + step
	a = func(xp)/func(x)
	if a >= 1:
		return xp
	else:
		if random.random() <= a:
			return xp
		else:
			return x

def MetropolisHastings(func,x0,dx,n):
	xs = np.zeros(n+1)
	xs[0] = x0
	for i in range(n):
		xs[i+1] = MetropolisHastingsStep(func,xs[i],dx)
	return xs