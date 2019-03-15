# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 20:00:54 2019

@author: Enriq

Supporting methods for 'load_data.py'
"""

import pandas as pd
import re, string



def find_all_words(stri):
    '''
    find all words in a given string,
    return a list contains all those words.
    
    :param: stri
    :type : str
    
    '''
    assert isinstance(stri, str)
    strList = []
    spaceIndex = [-1]
    for i in range(len(stri)):
        if stri[i] == ' ':
            spaceIndex.append(i)
    spaceIndex.append(len(stri))
    for i in range(len(spaceIndex)-1):
        a = spaceIndex[i]
        b = spaceIndex[i+1]
        newWord = stri[a+1:b]
        if newWord:
            strList.append(newWord)
    return strList



def word_frequency(line):
    '''
    find the frequency of each word in a string,
    return words and their corresponding frequencies
    in a dictionary.
    
    :param: line
    :type : str
    
    '''
    assert isinstance(line, str)
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    allList = []
    allDict = {}
    
    if isinstance(line, str):
        line = line.lower()
        line = regex.sub(' ', line)
        wordList = find_all_words(line)
        for word in wordList:
            if word in allList:
                allDict[word] += 1
            else:
                allList.append(wordList)
                allDict[word] = 1
                    
    return allDict



def get_words(data):
    '''
    find all high_frequency_words in a given column of strings
    or other types of data whose elements are all strings
    
    a distributed client 'c' is applied 
    
    :param: data
    :type : pd.Series
    
    '''
    assert isinstance(data, pd.Series)
    assert all(isinstance(i, str) for i in data)
    from dask.distributed import Client
    
    c = Client()    
    lines = [_ for _ in data]     
    tasks = c.map(word_frequency, [_ for _ in lines])
    allDicts = c.gather(tasks)
    allDict = {}
    
    for dic in allDicts:
        for key in dic.keys():
            if key in allDict.keys():
                allDict[key] += 1
            else:
                allDict[key] = 1
                
    words = pd.Series(list(allDict.keys()), index = list(allDict.values()))
    words = words.sort_index()
    threshold = int(words.shape[0]/50)
    words = words.loc[threshold:]
    c.close()
    return words
    
def get_that_word(data, word):
    '''
    Find out how many times a word appears in one string
    element in a pandas Series
    
    :param: data
    :type : pd.Series
    
    :param: word
    :type : str
    
    '''

    assert isinstance(data, pd.Series)
    assert all(isinstance(i, str) for i in data)
    assert isinstance(word, str)
    import numpy as np
    lines = [_.lower() for _ in data]   
    all_results = [word in _ for _ in lines]
    return np.array(all_results).sum()

    
    
    
    
                
    