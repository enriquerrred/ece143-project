import numpy as np
import os
import glob
#import cv2
#import torch
from numpy import genfromtxt
import pandas as pd
from sklearn.preprocessing import OneHotEncoder


def convert(x):
    if x=='Yes':
        return 1
    else:
        return 0
    


class DataLoader():
    def __init__(self,path_to_file,ignore = ['BusinessTravel','Department','EducationField','Gender','JobRole','MaritalStatus','EmployeeNumber','EmployeeCount','Over18','OverTime','StockOptionLevel','StandardHours'],categorical = ['Education','EnvironmentSatisfaction','JobInvolvement','JobLevel','JobSatisfaction','PerformanceRating','RelationshipSatisfaction','WorkLifeBalance']):
        dm = pd.read_csv(path_to_file,usecols = lambda x: x not in ignore+categorical)
        cols = dm.columns.tolist()
        cols = [cols[1]] + [cols[0]] + cols[2:]
        dm = dm[cols]
        data_mtx = dm.values
        data_mtx[:,0] = np.array([convert(i) for i in data_mtx[:,0]])
        #data_mtx = data_mtx[:,[1,0] + list(range(2,data_mtx.shape[1]))]
        
        
        
        train_split = 0.8
        test_split = 0.2
        dm_cat = pd.read_csv(path_to_file,usecols = categorical)
        dm_cat_mtx = dm_cat.values
        #print(np.amax(dm_cat_mtx,axis=0))
        dm_cat_mtx1 = OneHotEncoder(sparse = False).fit_transform(dm_cat_mtx)
        output_features  = OneHotEncoder(sparse = False).fit(dm_cat_mtx).get_feature_names(input_features = categorical)
        #print(output_features)
        #print(dm_cat_mtx1.shape)
        data_mtx = np.concatenate((data_mtx,dm_cat_mtx1),axis = 1)
        
        #print(cols[1:])
        self._training = data_mtx[:int(0.8*data_mtx.shape[0]),:]
        self._testing = data_mtx[int(0.8*data_mtx.shape[0]):,:]
        self.feature_names = list(cols[1:])  + list(output_features)
        self.new_names = list(cols[1:]) + categorical
    
    def get_data(self,mode = 'training'):
        assert isinstance(mode,str)
        assert(mode == 'training' or mode == 'testing')
        
        if(mode  == 'training'):
            X = self._training[:,1:]
            y = self._training[:,0]
            y = y.astype('int')
            return(X,y,self.feature_names,self.new_names)
        else:
            X = self._testing[:,1:]
            y = self._testing[:,0]
            y = y.astype('int')
            return(X,y,self.feature_names,self.new_names)
        
   
        
    