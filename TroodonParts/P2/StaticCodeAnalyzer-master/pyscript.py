import re
import os

import sys
filename= str(sys.argv[1])
print filename

#print "\n \t Enter a File Path for Static Analysis:",
#filename = raw_input()
x = "clang -Xclang -load -Xclang ../StaticCodeAnalyzer-master/llvm-pass-skeleton/build/skeleton/libSkeletonPass.so -S -emit-llvm -o test.ll -x cl "+filename
os.system("clear")
checking=os.system(x)



s =open(filename).read()
r = re.compile(r'\bint\b\s\w+', flags=re.I | re.M)
r2 = re.compile(r'\s\w+',flags=re.I | re.M)
z=r.findall(s)
f1=str(z)
z2=r2.findall(f1)
str1 = ''.join(z2)
#print str1
z3=re.split(r'\s*',str1)

c=0;
#print z3
for x in range(1, len(z3)):
    f2=str(z3[x])
    r34 = re.compile(r'\W'+f2+'\W', flags=re.I | re.M)
    zw=r34.findall(s)
    #print zw
    #print len(zw)
    c +=len(zw)
d2=str(c)

from time import  strftime
datetime=strftime("%a, %d %b %Y %X ")

datetime2=str(datetime)

r1 = re.compile(r'\bfloat\b\s\w+', flags=re.I | re.M)
r21 = re.compile(r'\s\w+',flags=re.I | re.M)
z1=r1.findall(s)
f11=str(z1)
z21=r21.findall(f11)
str11 = ''.join(z21)
z31=re.split(r'\s*',str11)

c1=0;

for x1 in range(1, len(z31)):
    f21=str(z31[x1])
    r341 = re.compile(r'\W'+f21+'\W', flags=re.I | re.M)
    zw1=r341.findall(s)
    #print zw1
    c1 +=len(zw1)
d21=str(c1)
line1="[20]-Total no of Float Operation: "
line1+= d21
line2 ="[21]-Total no of Integer Operation:  "
line2 += d2
r = re.compile(r'\b(\w+\s*)(<=|<|>=)(\s\w+)', flags=re.I | re.M)
r2 = re.compile(r'\b\s\s\w+\s', flags=re.I | re.M)
z=r.findall(s)
f1=str(z)
str1 = ''.join(f1)
r20=""
zo="'"
d=0
for x in range(1, len(str1)):
    if str1[x] == '[' or str1[x] == '(' or str1[x] == ')' or str1[x] == ']' or str1[x] == ',' or str1[x] == zo:
        
        d+=1
        #print str1[x]
        #print "if loop"
    else:
        r20 += str1[x]
z3=re.split(r'\s*',r20)
s231=""
for i, var in enumerate(z3):
        
        s231+=" "
        s231+= z3[i]
        

r8 = re.compile(r'\b(\s)(<=|<|>=)(\s\w+)', flags=re.I | re.M)
z9=r8.findall(s231)


f1e=str(z9)
str1e = ''.join(f1e)
r81 = re.compile(r'\b\s\w\s', flags=re.I | re.M)
z91=r81.findall(str1e)

f1ef=str(z91)
str1ef = ''.join(f1e)


r201=""
zo="'"
d=0
for x3 in range(1, len(str1ef)):
    if str1ef[x3] == '[' or str1ef[x3] == '(' or str1ef[x3] == ')' or str1ef[x3] == ']' or str1ef[x3] == ',' or str1ef[x3] == zo:
        
        d+=1
        #print str1[x]
        #print "if loop"
    else:
        r201 += str1ef[x3]

z91e=re.findall(r'\w+',r201)







string3=""

for x in range(0, len(z91e)):
   f2=str(z91e[x])
   
   r34 = re.compile(r'\bint\b\s'+f2+'\s', flags=re.I | re.M)
   zw=r34.findall(s)
   
   sa=str(zw)
   string3+=sa


string4=re.findall(r'\w+',string3)


r203=""
integer="int"
for x34 in range(1, len(string4)):
    if string4[x34] == '['  or string4[x34] == ']' or string4[x34] == ',' or string4[x34] == integer or string4[x34] == zo:
        
        d+=1
        #print str1[x]
        #print "if loop"
    else:
        r203+=" "
        r203 += string4[x34]


zw = re.sub("[^\w]", " ",  r203).split()



list3=list(zw)


s23=""
state=()
for x5 in range(0, len(zw)):
    f5=str(zw[x5])
    print f5
    r5 = re.compile(r'\s'+f5+'(\s\W)(\d+)', flags=re.I | re.M)
    state=r5.findall(s)
    s23+=str(state)


r10 = re.compile(r'\b\d+', flags=re.I | re.M)
z10=r10.findall(s23)



count=0
d2=list(z10)
for xr in range(0, len(d2)):
    df=d2[xr]
    dfg=int(df)
    count+=dfg

r = re.compile(r'\b(\w+\s*)(<=|<|>=)(\s\d+)|\b(\w+\s*)(<=|<|>=)(\d+)', flags=re.I | re.M)
z21=r.findall(s)




f21=str(z21)
str21 = ''.join(f21)



r21 = re.compile(r'\d+', flags=re.I | re.M)
z22=r21.findall(str21)



d22=list(z22)
for x22 in range(0, len(d22)):
    df2=d22[x22]
    dfg2=int(df2)
    count+=dfg2



lout=len(d22)+len(list3)
line3 = "[22]-Total no of Loop Operation:  "
line3 += str(count)


line4 = "[23]-Total no of Loop:    "
line4 += str(lout)


#os.remove('b1.txt')
fout=open('b1.txt', 'a')
fout.write("\n")
fout.write(line1)
fout.write("\n")
fout.write(line2)
fout.write("\n")
fout.write(line3)
fout.write("\n")
fout.write(line4)
fout.write("\n")


fout.write("\t \t Log date/time:  ")
fout.write(datetime2)

fout.write("\n")
fout.write("\n")
fout.close()


#fopen=open('/home/usman/Test/text/b1.txt').read()
#print fopen



if (checking != 0):
    print "\n \n"
    print "Error Script Failed "
    #print checking
    #print os.WEXITSTATUS(checking)
    print "\n \n"
    
else:
    print "\n \n"
    print "     |Executed: Check Log File|"
    print "\n \n"




'''

____________________________________________________________________________
Installation
sudo apt-get install clang


how to install passer
https://www.cs.cornell.edu/~asampson/blog/llvm.html
$ cd llvm-pass-skeleton
$ mkdir build
$ cd build
$ cmake ..  # Generate the Makefile.
$ make  # Actually build the pass.

____________________________________________________________________________


____________________________________________________________________________
Error


#if defined(cl_amd_fp64) || defined(cl_khr_fp64)
 
#if defined(cl_amd_fp64)
#pragma OPENCL EXTENSION cl_amd_fp64 : enable
#elif defined(cl_khr_fp64)
#pragma OPENCL EXTENSION cl_khr_fp64 : enable
#endif

typedef unsigned int uint;
typedef unsigned char uchar;
typedef unsigned char uchar4 __attribute__((ext_vector_type(4)));
typedef unsigned int uint4 __attribute__((ext_vector_type(4)));
typedef float float4 __attribute__((ext_vector_type(4)));
typedef float float2 __attribute__((ext_vector_type(2)));
typedef int int4 __attribute__((ext_vector_type(4)));
typedef int int2 __attribute__((ext_vector_type(2)));
#define CLK_LOCAL_MEM_FENCE 
#define CLK_GLOBAL_MEM_FENCE 
#define get_local_id
#define get_local_size
#define get_global_id
#define get_global_size
typedef int size_t;
#include <stddef.h>

typedef unsigned short ushort2 __attribute__((ext_vector_type(2)));
typedef int int2 __attribute__((ext_vector_type(2)));
#define CLK_LOCAL_MEM_FENCE 
#define CLK_GLOBAL_MEM_FENCE 
#define get_local_id
#define get_local_size
#define get_global_id
#define get_global_size
#define BLOCK_SIZE 16

/home/usman/Test/usman/AtomicCounters/AtomicCounters_Kernels.cl
___________________________________________________________________________

python /home/usman/Test/text/pyscript.py
Python  /home/usman/Test/usman/benchmark/intel_ocl_samples/BitonicSort/BitonicSort.cl
Path /home/usman/AMDAPPSDK-3.0/samples/opencl/cl/1.x
cmake -G "Unix Makefiles" 
cd bin/x86_64/Release/
/home/usman/Test/testcode/kernel.cl
commandqueue = clCreateCommandQueue(context, device, CL_QUEUE_PROFILING_ENABLE, &err_num);
 clFinish(commandQueue);
 clWaitForEvents(1 , &ndrEvt);
 cl_ulong time_start, time_end;
 double total_time;
 clGetEventProfilingInfo(ndrEvt, CL_PROFILING_COMMAND_START, sizeof(time_start), &time_start, NULL);
 clGetEventProfilingInfo(ndrEvt, CL_PROFILING_COMMAND_END, sizeof(time_end), &time_end, NULL);
 total_time = time_end - time_start;
 printf("\nKernel Execution time in milliseconds = %0.3f ms\n", (total_time / 1000000.0) );

/* Header to make Clang compatible with OpenCL */
#define __global __attribute__((address_space(1)))
int get_global_id(int index);
/* Test kernel */
__kernel void test(__global float *in, __global float *out)
{
    int index = get_global_id(0);
    out[index] = 3.14159f * in[index] + in[index];
}

clang -S -emit-llvm -o test.ll -x cl test.cl


   barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE); 




gcc -I -o vectmul.c -lOpenCL












'''
