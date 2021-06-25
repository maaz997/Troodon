#!/usr/bin/env python
# coding: utf-8

# In[18]:


import os


# In[19]:


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

# Reading Program Details
with open("../Data/Setup/Training_Programs.csv", "r") as f:
    file = f.readlines()
_Programs = []
for i in range(1,len(file)):
    _Programs.append(file[i].strip().split(','))


# In[20]:


# Extracting Features of Read Programs
_Features = []
for i in range(0,len(_Programs)):
    # Feature extraction cmd
    cmd = "python "+_Path+"/0_Feature_Extractor/Extract_Features.py "+_Path+"/1_Data_Generator/"+_Programs[i][2]+" "+_Programs[i][0]
    os.system(cmd)
    # Program compilation cmd
    cmd = "g++ "+_Path+"/1_Data_Generator/"+_Programs[i][1]+" -lOpenCL -L$AMDAPPSDKROOT/lib/x86_64 -o "+_Path+"/1_Data_Generator/"+_Programs[i][0]+".out"
    os.system(cmd)
    
    with open("../Data/Features/"+_Programs[i][0]+".txt", "r") as f:
        file = f.readlines()
    features = []
    for f in file:
        if "Log" in f or f.strip() is '':
            continue
        features.append(int( f.split(":")[-1].strip())) 
    features.append(int(_Ram)) 
    features.append(int(_CPU_Rank)) 
    features.append(int(_GPU_Rank)) 
    temp_F=""
    for val in features:
        temp_F+=str(val)
        temp_F+="-"
    _Features.append(temp_F)


# In[21]:


#Training Data Setup
Min_Size = 10000
Max_Size = 17000
Examples_per_program = 2
Repeation_Time = 1
_Jump = int((Max_Size-Min_Size)/(Examples_per_program-1))


# In[22]:


#Converting features list to string
pause_feature = ""
for val in _Features:
    pause_feature+=val+","
pause_feature = pause_feature[:len(pause_feature)-1]
#Converting programs list to string
pause_programs = ""
for _program in _Programs:
    for val in _program:
        pause_programs += val+"-"
    pause_programs = pause_programs[:len(pause_programs)-1]+","
pause_programs = pause_programs[:len(pause_programs)-1]
#Saving data for resuming
with open("../Data/1/Resume_Data.txt", "w") as f:
    f.write(str(pause_programs)+"\n")
    f.write(str(pause_feature)+"\n")
    f.write(str(Min_Size)+"\n")
    f.write(str(Max_Size)+"\n")
    f.write(str(Examples_per_program)+"\n")
    f.write(str(Repeation_Time)+"\n")


# In[23]:


with open("../Data/1/Execution_Fail.txt", "w") as f:
    f.write("")
for i in range(0,len(_Programs)):
    for j in range(0,Examples_per_program):
        size = int(Min_Size+_Jump*j)
        pth = _Features[i]+str(size)
        for k in range(0,Repeation_Time):
            #Reading Csv before cpu execution
            with open("../Data/1/Execution_Data.csv", "r") as f:
                file_O = f.readlines()
            #Cmd to run program for cpu execution
            cmd = "./"+_Programs[i][0]+".out "+str(size)+" "+str(_CPU)+" "+_CPU_Platform+" "+pth
            os.system(cmd)
            #Reading Csv after cpu execution
            with open("../Data/1/Execution_Data.csv", "r") as f:
                file_C = f.readlines()
            # Checking failure and saving data if failed 
            if(len(file_C)==len(file_O)):
                with open("../Data/1/Execution_Fail.txt", "a") as f:
                    f.write( str(cmd)+"\n" )
            #Cmd to run program for gpu execution       
            cmd = "./"+_Programs[i][0]+".out "+str(size)+" "+str(_GPU)+" "+_GPU_Platform+" "+pth
            os.system(cmd)
            #Reading Csv before gpu execution
            with open("../Data/1/Execution_Data.csv", "r") as f:
                file_G = f.readlines()
            # Checking failure and saving data if failed 
            if(len(file_C)==len(file_G)):
                with open("../Data/1/Execution_Fail.txt", "a") as f:

                    f.write( str(cmd)+"\n" )
            with open("../Data/1/Resume_Index.txt", "w") as f:
                f.write(str(i)+","+str(j)+","+str(k))


# In[ ]:




