import sys
import os
import time

base = str(sys.argv[1])
id= str(sys.argv[2])

'''
Call script 
'''
os.system("python3 "+base+"Scheduling.py "+base+" "+id)

while(True):
    with open(base+"Output/"+id+".txt", "r") as f:
        time.sleep(5)
        '''
        Call script
        '''
        os.system("python3 "+base+"Scheduling.py "+base+" "+id)

        device=int(f.read())
        if(device!=-1):
            break

sys.exit(device)