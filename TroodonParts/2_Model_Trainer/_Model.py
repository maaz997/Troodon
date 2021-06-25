#!/usr/bin/env python
# coding: utf-8

# # 1.Data Processing

# In[39]:


#Reading Execution Data
with open("../Data/1/Execution_Data.csv", "r") as f:
    fr = f.readlines()
_CPU = []
_GPU = []
for val in fr:
    val = val.strip().split(',')
    if(val[1]=='0'):
        _CPU.append(val)
    elif(val[1]=='1'):
        _GPU.append(val)


# In[40]:


#Reading Scheduling Data
with open("../Data/3/Exec_History.csv", "r") as f:
    fr = f.readlines()[1:]
for val in fr:
    val = val.strip().split(',')
    temp_val = [val[2],val[-3],val[-1]]
    if(temp_val[1]=='0'):
        _CPU.append(temp_val)
    elif(temp_val[1]=='1'):
        _GPU.append(temp_val)


# In[41]:


#Calculating Average Execution Time w.r.t features
_Avg_CPU = []
for val in _CPU:
    _T_Feat = val[0]
    _T_Time = val[2]
    if(len(_Avg_CPU)>0):
        if(_Avg_CPU[-1][0]==_T_Feat):
            _Avg_CPU[-1][1] = float(_Avg_CPU[-1][1])+float(_T_Time)
            _Avg_CPU[-1][2]+=1
        else:
            _Avg_CPU.append([_T_Feat,_T_Time,1])
    else:
        _Avg_CPU.append([_T_Feat,_T_Time,1])
        
_Avg_GPU = []
for val in _GPU:
    _T_Feat = val[0]
    _T_Time = val[2]
    if(len(_Avg_GPU)>0):
        if(_Avg_GPU[-1][0]==_T_Feat):
            _Avg_GPU[-1][1] = float(_Avg_GPU[-1][1])+float(_T_Time)
            _Avg_GPU[-1][2]+=1
        else:
            _Avg_GPU.append([_T_Feat,_T_Time,1])
    else:
        _Avg_GPU.append([_T_Feat,_T_Time,1])
for i in range(0,max(len(_Avg_CPU),len(_Avg_GPU))):
    if(i<len(_Avg_CPU)):
        _Avg_CPU[i] = {"Features": _Avg_CPU[i][0],"Execution_Time": float(_Avg_CPU[i][1])/float(_Avg_CPU[i][2])}
    if(i<len(_Avg_GPU)):
        _Avg_GPU[i] = {"Features": _Avg_GPU[i][0],"Execution_Time": float(_Avg_GPU[i][1])/float(_Avg_GPU[i][2])}


# In[42]:


#Filtering complete information and saving
_Final = []
for i in range(0,len(_Avg_CPU)):
    _T_CPU = _Avg_CPU[i]
    _T_GPU = next((item for item in _Avg_GPU if item["Features"] == _T_CPU["Features"]), None)
    if(_T_GPU!=None):
        _Final.append([_T_CPU["Features"],_T_CPU["Execution_Time"],_T_GPU["Execution_Time"]])


# In[43]:


#Data Conversion to suitable format
for i in range(0,len(_Final)):
    _Speed_up = _Final[i][1]-_Final[i][2]
    if(_Speed_up>0):
        _Final[i][1] = _Speed_up
        _Final[i][2] = 1
    else:
        _Final[i][1] = _Speed_up*-1
        _Final[i][2] = 0


# In[44]:


with open("../Data/2/Classification_data.csv", "w") as f:
    f.write("[1]-Total no of Return statement,[2]-Total no of Control Statement,[3]-Total no of Allocation instruction,[4]-Total no of Load Instructions,[5]-Total no of Store Instructions,[6]-Total no of Multiplication (Float Datatype) Operation,[7]-Total no of Addition(Integer Datatype) Instruction,[8]-Total no of Multiplication(Integer Datatype) Instruction,[9]-Total no of Division(Float Datatype) instruction,[10]-Total no of Division(Integer Datatype) instruction,[11]-Total no of Condition Check instruction,[12]-Total no of Addition(Float Datatype) instruction,[13]-Total no of Addition(Integer Datatype) instruction,[14]-Total no of Subtraction(Float Datatype) instruction,[15]-Total no of Subtraction(Integer Datatype) instruction,[16]-Total no of Function Call instruction,[17]-Total no of Functions,[18]-Total no of Blocks,[19]-Total no of Instructions,[20]-Total no of Float Operation,[21]-Total no of Integer Operation,[22]-Total no of Loop Operation,[23]-Total no of Loop,[24]-Ram,[25]-CPU Rank,[26]-GPU Rank,[27]-Matrix Size,[28]-Prefered Device\n")
with open("../Data/2/Regression_Data.csv", "w") as f:
    f.write("[1]-Total no of Return statement,[2]-Total no of Control Statement,[3]-Total no of Allocation instruction,[4]-Total no of Load Instructions,[5]-Total no of Store Instructions,[6]-Total no of Multiplication (Float Datatype) Operation,[7]-Total no of Addition(Integer Datatype) Instruction,[8]-Total no of Multiplication(Integer Datatype) Instruction,[9]-Total no of Division(Float Datatype) instruction,[10]-Total no of Division(Integer Datatype) instruction,[11]-Total no of Condition Check instruction,[12]-Total no of Addition(Float Datatype) instruction,[13]-Total no of Addition(Integer Datatype) instruction,[14]-Total no of Subtraction(Float Datatype) instruction,[15]-Total no of Subtraction(Integer Datatype) instruction,[16]-Total no of Function Call instruction,[17]-Total no of Functions,[18]-Total no of Blocks,[19]-Total no of Instructions,[20]-Total no of Float Operation,[21]-Total no of Integer Operation,[22]-Total no of Loop Operation,[23]-Total no of Loop,[24]-Ram,[25]-CPU Rank,[26]-GPU Rank,[27]-Matrix Size,[28]-Speed up\n")
    
for i in range(0,len(_Final)):
    v1 = _Final[i][0].split('-')
    for j in range(0,len(v1)):
        v1[j]=int(v1[j])
    v1.append(_Final[i][1])
    v2 = _Final[i][0].split('-')
    for j in range(0,len(v2)):
        v2[j]=int(v2[j])
    v2.append(_Final[i][2])
    with open("../Data/2/Classification_data.csv", "a") as f:
        f.write(str(v2).split('[')[1].split(']')[0]+"\n")
    with open("../Data/2/Regression_Data.csv", "a") as f:
        f.write(str(v1).split('[')[1].split(']')[0]+"\n")


# # 2. Training Classification Model

# In[45]:


import pandas as pd


# In[46]:


df_class = pd.read_csv("../Data/2/Classification_data.csv")
data = df_class[  df_class.columns[0:-1] ]
label = df_class[ df_class.columns[-1] ]


# In[47]:


import numpy as np
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split( data, label, test_size=0.33, random_state=42)


# In[48]:


from sklearn import datasets
from sklearn.svm import SVC

clf = SVC()
clf.fit(x_train, y_train)


# In[49]:


y_pred = clf.predict( x_test  )


# In[50]:


print ( "Accuracy is : " , len(y_test [ y_pred == y_test ] )/ len(y_test)*100, "%" )


# In[51]:


import pickle

# save the classifier
with open('trained_classifier.pkl', 'wb') as fid:
    pickle.dump( clf, fid)    

# load it again
#with open('trained_classifier.pkl', 'rb') as fid:
    #clf = cPickle.load(fid)


# # 3. Training Regression Model

# In[52]:


df_regr = pd.read_csv("../Data/2/Regression_Data.csv")
data = df_regr[  df_regr.columns[0:-1] ]
label = df_regr[ df_regr.columns[-1] ]


# In[53]:


import numpy as np
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split( data, label, test_size=0.33, random_state=42)


# In[54]:


from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression

regr = RandomForestRegressor(n_estimators=200, max_depth=5, random_state=0)

regr.fit(x_train, y_train)


# In[55]:


y_pred = regr.predict( x_test )


# In[56]:


from sklearn.metrics import mean_absolute_error
mean_absolute_error( list( y_test ) , list( y_pred ) )


# In[57]:


import pickle

# save the classifier
with open('trained_regressor.pkl', 'wb') as fid:
    pickle.dump( regr, fid)

# load it again
#with open('trained_regressor.pkl', 'rb') as fid:
    #regr = cPickle.load(fid)


# In[ ]:




