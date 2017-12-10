# -*- coding: utf-8 -*-
"""Demonstrate high quality docstrings."""
from math import pi
from cmath import exp


def inv_dft(arr):
	"""Calculates the inverse dft of a vector to 3 decimal places
	Input: Vector to be transformed
	Output: Inverse DFT transform of input"""
    upper_bound = len(arr)
	w = exp(-2 * pi * 1j / upper_bound)
	x_dft = [0]*upper_bound
	for k in range(0, upper_bound):
		temp = 0
	for j in range(0, upper_bound):
		temp += arr[j]*((w)**(j*k))
		x_dft[k] = temp/upper_bound
	return(x_dft)

x = [4.000 + 0.000j, -1.000 + 0.000j, -1.000 - 0.000j, -1.000 - 0.000j, -1.000 + 0.000j]

transf = inv_dft(x)
form_transf = ['{:.3f}'.format(elem) for elem in transf]
print(form_transf)