# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 15:55:33 2019

@author: Enriq


Import data from database 'Employee Review'

Mostly focusing on processing comments

'data' is the original dataset, 'current' contains data of current
employees, 'former' comtains data of former employees

'sort_by_company' is the list of sub_datasets for each company in 
the dataset 

After running the script, we should get a new csv file 'company_pros_cons.csv',
which will be used by 'employee_vs_company.py'.

*****NOTICE*****

i) line 45-49 are relevant to distributed computation,
should be run one-by-one outside to aviod potential breakdown.

ii) The acquired csv file 'all_pros.csv' and'all_cons.csv' are not 
final versions: They contains meaningless words. Since we do not want
to do NLP in the project, we decided to export them, select keywords 
manually in Microsoft Excel, and then import again.

"""
from get_high_frequency_words import *
import pandas as pd

data = pd.read_csv('./employee_reviews.csv', index_col=0)

companies = data.groupby('company')
company = pd.unique(data['company'])
total = [companies.get_group(i).shape[0] for i in company]

sort_by_company = {}
for company_name in company:
    sort_by_company[company_name] = companies.get_group(company_name)


#Get high-frequency_words form column "Pros" and "Cons":
#Should be run OUTSIDE the script!
'''
kwds_pros = get_words(data['pros'])
kwds_cons = get_words(data['cons'])

kwds_pros.to_csv('all_pros.csv')
kwds_cons.to_csv('all_cons.csv')
'''


#Get .csv file 'company_pros_cons.py':

pros = [get_that_word(sort_by_company[name]['pros'], name) for name in company]
cons = [get_that_word(sort_by_company[name]['cons'], name) for name in company]
company_pros_cons = pd.DataFrame({'pros':pros,'cons':cons,'total':total},index=company)
company_pros_cons.to_csv('company_pros_cons.csv')