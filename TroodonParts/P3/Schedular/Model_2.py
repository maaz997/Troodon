import sys
import os
base = str(sys.argv[3])
with open(base+"b1.txt", "r") as f:
    file = f.readlines()
    
features = []
for f in file:
    if "Log" in f or f.strip() is '':
        continue
    features.append(  int( f.split(":")[-1].strip()) ) 
    #print (f)

features.append(int(sys.argv[2]))
#features
# load it again
import pickle
with open(base+'my_dumped_classifier.pkl', 'rb') as fid:
    clf = pickle.load(fid)
class_ =  clf.predict(  [features] )[0]
# load it again
import pickle
with open(base+'my_dumped_regressor.pkl', 'rb') as fid:
    regr = pickle.load(fid)
    
speed_up = regr.predict( [features] )[0]

#print (class_)
with open(base+"Output/"+str(sys.argv[1])+"_class.txt", "w") as f:
    f.write( str(class_) )
    
with open(base+"Output/"+str(sys.argv[1])+"_speed_up.txt", "w") as f:
    f.write( str(speed_up) )
with open(base+"Output/"+str(sys.argv[1])+"_features.txt", "w") as f:
    f.write( str(features) )

os.remove(base+"b1.txt")
