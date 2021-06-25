#!/usr/bin/env python
# coding: utf-8

# In[26]:


with open("../Data/1/Resume_Data.txt", "r") as f:
     file = f.readlines()
_Features = []
pause_feature = file[1]
for val in pause_feature.strip().split(","):
    _Features.append(val)
_Programs = []
pause_programs = file[0]
for val in pause_programs.strip().split(","):
    _Programs.append(val.split('-'))
#Training Data Setup
Min_Size = int(file[2])
Max_Size = int(file[3])
Examples_per_program = int(file[4])
Repeation_Time = int(file[5])
_Jump = int((Max_Size-Min_Size)/(Examples_per_program-1))
with open("../Data/1/Resume_Index.txt", "r") as f:
     file = f.read().split(',')
c_i = int(file[0])
c_j = int(file[1])
c_k = int(file[2])


# In[27]:


print(_Features,_Programs,Min_Size,Max_Size,Examples_per_program,Repeation_Time,_Jump,c_i,c_j,c_k)


# In[28]:


for i in range(0,len(_Programs)):
    if(i<=c_i):
        continue
    for j in range(0,Examples_per_program):
        if(j<=c_j):
            continue
        size = int(Min_Size+_Jump*j)
        pth = _Features[i]+str(size)
        for k in range(0,Repeation_Time):
            if(k<=c_k):
                continue
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

