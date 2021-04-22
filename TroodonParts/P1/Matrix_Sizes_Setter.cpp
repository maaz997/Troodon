#include<iostream>
#include<fstream>
#include <set>
#include <cassert>
#include<stdio.h>
#include <stdlib.h>
#include <math.h>

using namespace std;

int main()
{
    int initial_size = 10000;
    int iterations_each = 30;
    srand(time(0));

    fstream fout; /* fstream object for reading or writing */

    /************************** Random Matrix Sizes Generation **************************/
    
    set<int> Matrix_Sizes;

    /*Matrix_Sizes.insert(1024);*/

    /*while (Matrix_Sizes.size()<100)  Random No within 1024-19999 
    {
        int temp = (rand()%10000) + 7000;
        Matrix_Sizes.insert(temp);
    }*/

    //cout << "Size : " << Matrix_Sizes.size() << endl; /* Total Matrix Size values in set */

    /************************** Saving Generated Matrix Sizes  **************************/
    

    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    for (int i = initial_size; i <= initial_size + (500 * (iterations_each - 1)); i+=500) /* Multiples of 500 within 1500-20000 */
    {
        Matrix_Sizes.insert(i);
    }

    remove("./Matrix_Sub/Matrix_Sizes.txt"); 
    
    fout.open("./Matrix_Sub/Matrix_Sizes.txt", ios::out | ios::app);
    
    for (auto elem : Matrix_Sizes)
    {
        fout << elem << "\n";
    }
    fout.close();
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    for (int i = initial_size; i <= initial_size + (500 * (iterations_each - 1)); i+=500) /* Multiples of 500 within 1500-20000 */
    {
        Matrix_Sizes.insert(i);
    }

    remove("./Matrix_Mul/Matrix_Sizes.txt"); 
    
    fout.open("./Matrix_Mul/Matrix_Sizes.txt", ios::out | ios::app);

    for (auto elem : Matrix_Sizes)
    {
        fout << elem << "\n";
    }
    fout.close();
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    for (int i = initial_size; i <= initial_size + (500 * (iterations_each - 1)); i+=500) /* Multiples of 500 within 1500-20000 */
    {
        Matrix_Sizes.insert(i);
    }
    remove("./Matrix_Add/Matrix_Sizes.txt"); 
    
    fout.open("./Matrix_Add/Matrix_Sizes.txt", ios::out | ios::app);

    for (auto elem : Matrix_Sizes)
    {
        fout << elem << "\n";
    }
    fout.close();
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    for (int i = initial_size; i <= initial_size + (500 * (iterations_each - 1)); i+=500) /* Multiples of 500 within 1500-20000 */
    {
        Matrix_Sizes.insert(i);
    }
    
    remove("./Matrix_Transpose/Matrix_Sizes.txt"); 
    
    fout.open("./Matrix_Transpose/Matrix_Sizes.txt", ios::out | ios::app);

    for (auto elem : Matrix_Sizes)
    {
        fout << elem << "\n";
    }
    
    fout.close();
    /************************************************************************************/
    
    return 0;
}
