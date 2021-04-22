cd CPU

a=0

g++ matrixT_host.cpp -lOpenCL -L$AMDAPPSDKROOT/lib/x86_64
./a.out

a=`expr $a + 1`

cd ..

cd GPU

a=0

g++ matrixT_host.cpp -lOpenCL -L$AMDAPPSDKROOT/lib/x86_64
./a.out

a=`expr $a + 1`

cd ..

