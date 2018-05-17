# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 19:27:35 2017

@author: t-blu
"""




import pymc3 as py
import theano
import numpy as np
import matplotlib.pyplot as plt
size = 200
true_intercept = 1
true_slope = 2

x = np.linspace(0, 1, size)
# y = a + b*x
true_regression_line = true_intercept + true_slope * x
# add noise
y = true_regression_line + np.random.normal(scale=.5, size=size)

data = dict(x=x, y=y)


plt.figure(figsize=(7, 7))

plt.tight_layout();