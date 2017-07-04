#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np 
import matplotlib.pyplot as plt 

grehounds = 500
labs = 500

gre_height = 28 + 4 * np.random.randn(grehounds)
lab_height = 24 +4 * np.random.randn(labs)

plt.hist([gre_height,lab_height],stacked=True,color=['r','b'])
plt.show()