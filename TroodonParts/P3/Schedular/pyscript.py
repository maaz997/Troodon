import re
import os

import sys
filename= str(sys.argv[1])
print filename

_base=str(sys.argv[4])

x = "clang -Xclang -load -Xclang "+_base+"llvm-pass-skeleton/build/skeleton/libSkeletonPass.so -S -emit-llvm -o test.ll -x cl "+filename
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
fout=open(_base+"b1.txt", 'a')
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
    
    #----our code for model
    import os
    os.system("python3 "+_base+"Model_2.py "+sys.argv[2]+" "+sys.argv[3]+" "+sys.argv[4])
    
