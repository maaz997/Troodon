import sys
import os
import time

base = str(sys.argv[1])
id= str(sys.argv[2])

'''
Call script 
'''
os.system("python3 "+base+"/3_Scheduler/Scheduling.py "+base+" "+id)

while(True):
    with open(base+"/Data/3/Wait/"+id+".txt", "r") as f:
        time.sleep(5)
        '''
        Call script
        '''
        os.system("python3 "+base+"/3_Scheduler/Scheduling.py "+base+" "+id)

        device=int(f.read())
        if(device!=-1):
            break

sys.exit(device)