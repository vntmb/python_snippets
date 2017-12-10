# -*- coding: utf-8 -*-
"""Demonstrate high quality docstrings."""
from random import randint


def quickselect(arr, k):
    """Doc String."""
    pivot = randint(0, len(arr))
    sub_min = [i for i in arr if i < arr[pivot]]
    sub_pls = [i for i in arr if i > arr[pivot]]
    v = len(sub_min) + 1
    if v == k:
        return arr[pivot]
    else:
        if v > k:
            return(quickselect(sub_min, k))
        else:
            return(quickselect(sub_pls, k - v))
arr = [65, 28, 59, 33, 21, 56, 22, 95, 50, 12, 90, 53, 28, 77, 39]
print(quickselect(arr, 8))
