# Troodon
# Data Generator
How to Run
To generate data just run Run.sh in Data_Generation folder.
Configuration
Configuration is needed for setting platform id for cpu and gpu separately as it varies for
different heterogeneous systems.
1.Matrix_Mul :
Open Matrix_Mul folder.
 Setting platforms : In CPU/GPU folder set platform id according to the system.
 Setting no of samples : In Run.sh set loop size according to sample size for cpu
and gpu.
In Matrix_Sizes.cpp set loop condition with sample size ( 100 in fig below )

# StaticCodeAnalyzer
Settting Feature Extractor

1- Change path according to your Output file (llvm-pass-skeleton\skeleton\Skeleton.cpp) line 100.
2- Install clang. Command : "sudo apt install clang"
3- cd llvm-pass-skeleton
4- mkdir build
5- cd build
6- cmake ..
7- make
8- cd ..
9- Change path of your pass (File pyscript.py , line 9,  /home/pcna-1/Usman/)
10- run python script. Command: "python pyscript.py   path_of_kernal"



