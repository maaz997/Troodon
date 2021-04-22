import sys
import os

base = str(sys.argv[1])
with open(base+"Output/"+str(sys.argv[2])+"_class.txt", "r") as f:
    ml_class = f.read()
with open(base+"Output/"+str(sys.argv[2])+"_speed_up.txt", "r") as f:
    ml_speed_up = f.read()
# Features read
with open(base+"Output/"+str(sys.argv[2])+"_features.txt", "r") as f:
    features = f.read()
f1=features.split("[")
f2=f1[1].split("]")
temp=[]
temp.append(sys.argv[3])
temp.append(sys.argv[4])
temp.append(f2[0])
temp.append(ml_class)
temp.append(ml_speed_up)
temp.append(sys.argv[5])
temp.append(sys.argv[6])
temp.append(sys.argv[7])

from csv import writer
#  Open our existing CSV file in append mode
# Create a file object for this file
with open(base+"Output/"+'Output.csv', 'a') as f_object:
  
    # Pass this file object to csv.writer()
    # and get a writer object
    writer_object = writer(f_object)
  
    # Pass the list as an argument into
    # the writerow()
    writer_object.writerow(temp)
  
    #Close the file object
    f_object.close()
os.remove(base+"Output/"+str(sys.argv[2])+".txt")
os.remove(base+"Output/"+str(sys.argv[2])+"_class.txt")
os.remove(base+"Output/"+str(sys.argv[2])+"_speed_up.txt")
os.remove(base+"Output/"+str(sys.argv[2])+"_features.txt")