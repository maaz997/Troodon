import sys

'''
Args
'''
base=str(sys.argv[1])
id=int(sys.argv[2])

'''
Reading program files
'''
with open(base+"Output/"+str(id)+"_class.txt", "r") as f:
    _class = int(f.read().strip())
with open(base+"Output/"+str(id)+"_speed_up.txt", "r") as f:
    _speed_up = float(f.read().strip())
    
'''
Creating program dictionary
'''
Program_Dict={"Id":id,"Class":_class,"Speed_up":_speed_up}

'''
Reading and saving waiting list
'''
Program_Found=False
Waiting_List_CPU=[]
Waiting_List_GPU=[]

with open(base+"Output/"+'Waiting.csv', 'r') as f_object:
    while(True):
        temp_val=f_object.readline().strip()
        
        '''
        Checks csv file end
        '''
        if(temp_val==""):
            break
        
        '''
        Setting values after splitting
        '''
        temp_split=temp_val.split(',')
        temp_id=int(temp_split[0])
        temp_class=int(temp_split[1])
        temp_speed_up=float(temp_split[2])
        
        '''
        Creating dictionary
        '''
        Temp_Program_Dict={"Id":temp_id,"Class":temp_class,"Speed_up":temp_speed_up}
        
        '''
        Checks if program matches
        '''
        if(temp_id==Program_Dict["Id"]):
            Program_Found=True
            
        '''
        Adding dictionary in respective list
        '''
        if(temp_class==0):
            Waiting_List_CPU.append(Temp_Program_Dict)
        elif(temp_class==1):
            Waiting_List_GPU.append(Temp_Program_Dict)
            
    '''
    Adding new program in waiting list and saving wait status -1
    '''
    if(Program_Found==False):
        if(Program_Dict["Class"]==0):
            Waiting_List_CPU.append(Program_Dict)
        elif(Program_Dict["Class"]==1):
            Waiting_List_GPU.append(Program_Dict)
        with open(base+"Output/"+str(id)+'.txt', 'w') as f_object:
            f_object.write('-1')
            f_object.close()

'''
Sorting and saving waiting queue in list
'''
Waiting_List=sorted(Waiting_List_CPU, key=lambda k: k['Speed_up'], reverse=True)+sorted(Waiting_List_GPU, key=lambda k: k['Speed_up'], reverse=False)

'''
Getting cpu and gpu perecentage
'''
import psutil
cpu_perecentage=psutil.cpu_percent(interval=1,percpu=False)
import GPUtil
GPUs = GPUtil.getGPUs()
load = GPUs[0].load
gpu_perecentage=load*100

'''
Assigning waiting program devices
'''
#to be updated later ----------------------------
if(gpu_perecentage<70 and len(Waiting_List)>0): #
    gpu_run=Waiting_List.pop(-1)                #
else:                                           #
    gpu_run=0                                   #
if(cpu_perecentage<70 and len(Waiting_List)>0): #
    cpu_run=Waiting_List.pop(0)                 #
else:                                           #                   
    cpu_run=0                                   #
#to be updated later ----------------------------
if(gpu_run!=0):
    with open(base+"Output/"+str(gpu_run["Id"])+'.txt', 'w') as f_object:
        f_object.write('1')
        f_object.close()
if(cpu_run!=0):
    with open(base+"Output/"+str(cpu_run["Id"])+'.txt', 'w') as f_object:
        f_object.write('0')
        f_object.close()

'''
Saving waiting list
'''

with open(base+"Output/"+'Waiting.csv', 'w') as f_object:
    for val in Waiting_List:
        t=str(val['Id'])+","+str(val['Class'])+","+str(val['Speed_up'])+"\n"
        f_object.write(t)
    f_object.close()
