from scipy.stats import rankdata
import numpy as np
def byp(p_values):
	rank = rankdata(p_values,method='max')
	nbp = len(p_values)
	sigma = sum([1/(i+1.0) for i in range(nbp)])
	return [min(p_values[i]*nbp*sigma/rank[i],1) for i in range(nbp)]

def bhp(p_values):
	rank = rankdata(p_values,method='max')
	nbp = len(p_values)
	return [min(p_values[i]*nbp/rank[i],1) for i in range(nbp)]

def bon():
	nbp = len(p_values)
	return [min(p_values[i]*nbp,1) for i in range(nbp)]



