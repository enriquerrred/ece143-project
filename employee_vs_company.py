# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 16:03:08 2019

@author: Enriq

Show and save plot 'Percentages of employees mention their companies in comment'

"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


pros_cons = pd.read_csv('./company_pros_cons.csv', \
                        index_col = 'Unnamed: 0')

company = list(pros_cons.index)
y1 = pros_cons['pros']/pros_cons['total']
y2 = pros_cons['cons']/pros_cons['total']

x_pos = np.arange(6)

w =0.2

fig, ax = plt.subplots()
ax.bar(x_pos-w, y1, color ='orange', width=0.4, label = 'pros')
ax.bar(x_pos+w, y2, color ='blue',width=0.4, label='cons')
ax.set_ylabel('Percentage')
ax.set_title('Percentages of employees mention their companies in comment')
ax.set_xticks(x_pos) 
ax.set_xticklabels(company)
ax.legend()

plt.savefig('1.jpg')
plt.show()