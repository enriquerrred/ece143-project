# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 16:03:08 2019

Show and save plot 'Keywords_statistics.jpg' 
Pre-processed file 'sall_pros.csv' and 'all_cons.csv' are required

@author: Enriq
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dat1 = pd.read_csv('./all_pros.csv',header = None)
dat2 = pd.read_csv('./all_cons.csv',header = None)
n1 = dat1.shape[0]
n2 = dat2.shape[0]
threshold = 15
x1 = np.array(dat1[0][n1-threshold:])
y1 = np.array(dat1[1][n1-threshold:])
x2 = np.array(dat2[0][n2-threshold:])
y2 = np.array(dat2[1][n2-threshold:])
y_pos = np.arange(threshold)

fig,axs = plt.subplots(2,1,figsize=(15,15))

ax1, ax2 = axs

ax1.barh(y_pos, x1, color = 'orange')
ax1.set_yticks(y_pos)
ax1.set_yticklabels(y1, fontsize = 20)
ax1.set_title('Most Common Keywords in "Pros"',size=24)
ax1.tick_params(labelsize=20)

ax2.barh(y_pos, x2, color = 'blue')
ax2.set_yticks(y_pos)
ax2.set_yticklabels(y2, fontsize = 20)
ax2.set_title('Most Common Keywords in "Cons"',size=24)
ax2.tick_params(labelsize=20)

plt.subplots_adjust(left = 0.2, right = 0.9, hspace = 0.2)
plt.savefig('Keywords_statistics.jpg')
plt.show()