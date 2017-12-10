# -*- coding: utf-8 -*-
"""Demonstrate high quality docstrings."""
from random import randint


def quicksort(arr):
	"""Doc String Here"""
    if len(arr) == 0 or len(arr) == 1:
        return arr
    else:
        pivot = randint(0, len(arr))
        sub_min = [i for i in arr if i < arr[pivot]]
        sub_pls = [i for i in arr if i > arr[pivot]]
        return(quicksort(sub_min) + [arr[pivot]] + quicksort(sub_pls))

print(quicksort([4, 5, 1, 2, 8, 9, 7]))
