g++ Matrix_Sizes_Setter.cpp

./a.out

file="Data.csv"

if [ -f $file ] ; then
    rm $file
fi

cd Matrix_Mul

./Run.sh

cd ..

cd Matrix_Add

./Run.sh

cd ..

cd Matrix_Sub

./Run.sh

cd ..

cd Matrix_Transpose

./Run.sh

cd ..
