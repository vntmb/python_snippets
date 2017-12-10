# -*- coding: utf-8 -*-
"""Demonstrate high quality docstrings."""
from math import pi
from cmath import exp


def dft(arr):
	"""Calculates the dft of a vector to 3 decimal places
	Input: Vector to be transformed
	Output: DFT transform of input"""
    upper_bound = len(arr)
	w = exp(-2 * pi * 1j / upper_bound)
	x_dft = [0]*upper_bound
	for k in range(0, upper_bound):
	    temp = 0
    for j in range(0, upper_bound):
	    temp += arr[j]*((w)**(j*k))
	    x_dft[k] = temp
	  return(x_dft)

x = [0,1,1,1,1]

transf = dft(x)
form_transf = ['{:.3f}'.format(elem) for elem in transf]
print(form_transf)