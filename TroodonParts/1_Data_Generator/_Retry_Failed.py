#!/usr/bin/env python
# coding: utf-8

# In[10]:


import os
with open("../Data/1/Execution_Fail.txt", "r") as f:
    file = f.readlines()
with open("../Data/1/Execution_Fail.txt", "w") as f:
    f.write("")
for val in file:
    #Reading Csv before execution
    with open("../Data/1/Execution_Data.csv", "r") as f:
                file_S = f.readlines()
    cmd = val.strip()
    os.system(cmd)
    #Reading Csv before after execution
    with open("../Data/1/Execution_Data.csv", "r") as f:
                file_E = f.readlines()
    # Checking failure and saving data if failed 
    if(len(file_S)==len(file_E)):
        with open("../Data/1/Execution_Fail.txt", "a") as f:
            f.write( str(cmd)+"\n" )


# In[ ]:




