# -*- coding: utf-8 -*-
"""
4 different ways of sampling from the normal distribution

@author: vntmb
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from random import uniform

def sums_of_uniforms(n):
    """This returns n random samples from N(0,1)
    Input: n
    Output: n random samples from N(0,1)"""
    X = np.zeros((n))
    for i in range(n):
        Us = np.random.uniform(0,1,12)
        X[i] = np.sum(Us) - 6
    plt.figure(1)
    plt.hist(X)
    return X

def box_muller(n):
    """This returns 2 random samples from N(0,1) of size n
    Input: n
    Output: 2 random samples from N(0,1) of size n"""
    X1 = np.zeros((n))
    X2 = np.zeros((n))
    for i in range(n):
        u1 = np.random.uniform(0,1)
        u2 = np.random.uniform(0,1)
        X1[i] = np.cos(2 * np.pi * u1) * np.sqrt(-2 * np.log(u2))
        X2[i] = np.sin(2 * np.pi * u1) * np.sqrt(-2 * np.log(u2))
    
    plt.figure(2)
    plt.hist(X1)
    plt.figure(3)
    plt.hist(X2)
    return X1, X2

def metropolis_hastings_normal(n):
    """This returns 2 random samples from N(0,1) of size n
    Input: n
    Output: 2 random samples from N(0,1) of size n"""
    X = np.zeros((n))
    # Burn-in period first
    x0 = 0
    for i in range(100):
        y = x0 + uniform(-3, 3)
        prob = min(1, norm.pdf(y)/norm.pdf(x0))
        if (uniform(0,1) < prob):
            x0 = y
    
    # Now the MH algorithm
    acceptances = 0
    for i in range(n):
        y = x0 + uniform(-3, 3)
        prob = min(1, norm.pdf(y)/norm.pdf(x0))
        if (uniform(0,1) < prob):
            X[i] = y
            x0 = y
            acceptances += 1
        else:
            X[i] = x0
    print(f"The acceptance rate was: {acceptances/n * 100}%")
    plt.figure(4)
    plt.hist(X)
    return X

def cholesky_normal(n, mean, var_cov):
    """This returns random samples from N(mu,C) of size n
    Caveat: Currently assumes 2 dimensions
    Input: n, mean of rvs, variance-covariance matrix
    Output: random samples from N(mean,var_cov) of size n"""
    X = np.zeros((n,var_cov.shape[1]))
    L = np.linalg.cholesky(var_cov)
    for i in range(n):
        Y = np.random.normal(0,1,2)
        X[i] = mean + L.dot(Y)
    
    x_vals = X[:,0]
    y_vals = X[:,1]
    plt.figure(5)
    plt.scatter(x_vals, y_vals)
    return X

# Length of random sample
n = 10000

# 1st 
sums_of_uniforms(n)

# 2nd 
box_muller(n)

# 3rd 
metropolis_hastings_normal(n)

# 4th
mean = np.array([1,1])
var_cov = np.array([[3,-1],[-1,3]])
cholesky_normal(n, mean, var_cov)















