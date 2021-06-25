#!/usr/bin/env python
# coding: utf-8

# In[20]:


import os
import sys


# In[21]:


_Date = str(sys.argv[1])
_Time = str(sys.argv[2])
_Wait = str(sys.argv[3])
_Exec = str(sys.argv[4])
_Selc = str(sys.argv[5])
_PrId = str(sys.argv[6])
# _Date = "17-3-2021"
# _Time = "21-10-21"
# _Wait = "0.000212"
# _Exec = "0.225832"
# _Selc = "1"
# _PrId = "24144601"


# In[22]:


with open("../Data/3/"+_PrId+".txt", "r") as f:
    fr = f.read().split(',')
_Features = str(fr[0])
_Device = str(fr[1])
_Speed_up = str(fr[2])


# In[23]:


os.remove("../Data/3/"+_PrId+".txt")


# In[24]:


with open("../Data/3/Exec_History.csv", "a") as f:
    f.write(_Date+",")
    f.write(_Time+",")
    f.write(_Features+",")
    f.write(_Device+",")
    f.write(_Speed_up+",")
    f.write(_Selc+",")
    f.write(_Wait+",")
    f.write(_Exec+"\n")


# In[ ]:




