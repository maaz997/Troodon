#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import sys


# In[2]:


id = sys.argv[1]
size = sys.argv[2]
# id = 10238989
# size = 10500


# In[3]:


# Reading System Details
with open("../Data/Setup/System_Setup", "r") as f:
    file = f.readlines()
Temp = []
for f in file:
    if f.strip() is '':
        continue
    Temp.append(f.split("=")[-1].strip())  

_Path = Temp[0]
_Ram = Temp[1]
_CPU_Rank = Temp[2]
_GPU_Rank = Temp[3]
_CPU_Platform = Temp[4]
_GPU_Platform = Temp[5]
_CPU = 0
_GPU = 1

Temp.clear()


# In[4]:


#Reading Features
with open("../Data/Features/Temp/"+str(id)+".txt", "r") as f:
    file = f.readlines()
    
features = []
for f in file:
    if "Log" in f or f.strip() is '':
        continue
    features.append(  int( f.split(":")[-1].strip()) ) 
features.append(int(_Ram)) 
features.append(int(_CPU_Rank)) 
features.append(int(_GPU_Rank))
features.append(int(size))
print(features)


# In[5]:


# Loading Device classifier
import pickle
with open("../2_Model_Trainer/trained_classifier.pkl", 'rb') as fid:
    clf = pickle.load(fid)
class_ =  clf.predict(  [features] )[0]
print(class_)


# In[6]:


# Loading Speedup Regressor
import pickle
with open("../2_Model_Trainer/trained_regressor.pkl", 'rb') as fid:
    regr = pickle.load(fid)
    
speed_up = regr.predict( [features] )[0]
print(speed_up)


# In[9]:


# Saving Data
_features=""
for val in features:
    _features+=str(val)
    _features+="-"
    
with open("../Data/3/"+str(id)+".txt", "w") as f:
    f.write( _features[:-1] + "," )
    f.write( str(class_) + "," )
    f.write( str(speed_up) )


# In[ ]:




