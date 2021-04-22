#include<iostream>
#include<fstream>
#include <set>
#include <string.h>
#include <cassert>
#include<stdio.h>
#include <stdlib.h>
#include <math.h>
#include <bits/stdc++.h>

using namespace std;

int main()
{

   set<string> CPU;
   set<string> GPU;

   set<int> Speed_Up;
   vector<int> List_Speed_Up;

   int Cpu_Count =0;
   int Gpu_Count =0; 

   remove("Classification_Data.csv");
   remove("Speedup_Data.csv");


   fstream fout_Classification,fout_Speedup,fin;// file pointer 

   fout_Classification.open("Classification_Data.csv", ios::out | ios::app); 
   fout_Speedup.open("Speedup_Data.csv", ios::out | ios::app);

   fout_Classification << "[1]-Total no of Return statement,[2]-Total no of Control Statement,[3]-Total no of Allocation instruction,[4]-Total no of Load Instructions,[5]-Total no of Store Instructions,[6]-Total no of Multiplication (Float Datatype) Operation,[7]-Total no of Addition(Integer Datatype) Instruction,[8]-Total no of Multiplication(Integer Datatype) Instruction,[9]-Total no of Division(Float Datatype) instruction,[10]-Total no of Division(Integer Datatype) instruction,[11]-Total no of Condition Check instruction,[12]-Total no of Addition(Float Datatype) instruction,[13]-Total no of Addition(Integer Datatype) instruction,[14]-Total no of Subtraction(Float Datatype) instruction,[15]-Total no of Subtraction(Integer Datatype) instruction,[16]-Total no of Function Call instruction,[17]-Total no of Functions,[18]-Total no of Blocks,[19]-Total no of Instructions,[20]-Total no of Float Operation,[21]-Total no of Integer Operation,[22]-Total no of Loop Operation,[23]-Total no of Loop,[24]-Matrix Size,[25]-Classification\n";
   fout_Speedup << "[1]-Total no of Return statement,[2]-Total no of Control Statement,[3]-Total no of Allocation instruction,[4]-Total no of Load Instructions,[5]-Total no of Store Instructions,[6]-Total no of Multiplication (Float Datatype) Operation,[7]-Total no of Addition(Integer Datatype) Instruction,[8]-Total no of Multiplication(Integer Datatype) Instruction,[9]-Total no of Division(Float Datatype) instruction,[10]-Total no of Division(Integer Datatype) instruction,[11]-Total no of Condition Check instruction,[12]-Total no of Addition(Float Datatype) instruction,[13]-Total no of Addition(Integer Datatype) instruction,[14]-Total no of Subtraction(Float Datatype) instruction,[15]-Total no of Subtraction(Integer Datatype) instruction,[16]-Total no of Function Call instruction,[17]-Total no of Functions,[18]-Total no of Blocks,[19]-Total no of Instructions,[20]-Total no of Float Operation,[21]-Total no of Integer Operation,[22]-Total no of Loop Operation,[23]-Total no of Loop,[24]-Matrix Size,[25]-Speed up\n";
    
   fout_Classification.close();
   fout_Speedup.close();
   
   /********************** READS EXECUTION DATA FROM TEMP FILE ************************/
      
 
   fin.open("../P1/Data.csv", ios::in | ios::app);

   string line;

   while (getline(fin,line))
   {
       size_t found = line.find("CPU"); 
       if (found != string::npos)
       {
           CPU.insert(line);
       }
       else
       {
           GPU.insert(line);
       }     
   }
   
   fin.close();

   string List_Arr[CPU.size()];

   int i = 0;

   for (auto elem : CPU)
    {
        List_Arr[i]=elem;
        i++;
    }
    i = 0;
    for (auto elem : GPU)
    {
        List_Arr[i]=List_Arr[i]+" : "+elem;
        i++;
    }
    
    for (int i = 0; i < CPU.size(); i++)
    {
        string value = List_Arr[i];
        vector <string> tokens; 
      
    // stringstream class check1 
    stringstream check1(value); 
      
    string intermediate; 
      
    while(getline(check1, intermediate, ',')) 
    { 
        tokens.push_back(intermediate); 
    } 
      
    for(int i = 0; i < tokens.size(); i++)
    {
        if(i==1 || i==6)
        {
            tokens[i] = tokens[i].substr(1);
        }
        
        if(i==5)
        {
            stringstream check2(tokens[i]);
            getline(check2, intermediate, ':');
            tokens[i] = intermediate;
        }
    }
    
    vector<string>::iterator it1, it2 , it3;
    it1 = tokens.begin(); it1+=7;
    it2 = tokens.begin(); it2+=6;
    it3 = tokens.begin(); it3+=1;

    tokens.erase(it1);
    tokens.erase(it2);
    tokens.erase(it3);
    
    float fc = (stof(tokens[2]) + stof(tokens[3]) + stof(tokens[4]))/3;

    float fg = (stof(tokens[5]) + stof(tokens[6]) + stof(tokens[7]))/3;
    
    // cout << "Program : "+tokens[0];
    // cout << " Size : "+tokens[1];
    // cout << " CPU Avg : " << fc;
    // cout << " GPU Avg : " << fg;
    // if (fc < fg){ cout << " Suitable : CPU\n"; } else { cout << " Suitable : GPU\n"; }

    fout_Classification.open("Classification_Data.csv", ios::out | ios::app); 
    fout_Speedup.open("Speedup_Data.csv", ios::out | ios::app); 


    if(tokens[0].find("Transpose")!=-1)
    {
        fout_Classification << "1 , 0 , 0 , 1 , 1 , 0 , 2 , 2 , 0 , 0 , 0 , 0 , 2 , 0 , 0 , 2 , 4 , 1 , 15 , 6 , 16 , 0 , 0 , ";
        fout_Speedup << "1 , 0 , 0 , 1 , 1 , 0 , 2 , 2 , 0 , 0 , 0 , 0 , 2 , 0 , 0 , 2 , 4 , 1 , 15 , 6 , 16 , 0 , 0 , "; 
    }
    else if(tokens[0].find("addition")!=-1)
    {
        fout_Classification << "1 , 0 , 0 , 2 , 1 , 0 , 1 , 1 , 0 , 0 , 0 , 1 , 1 , 0 , 0 , 2 , 4 , 1 , 13 , 8 , 13 , 0 , 0 , "; 
        fout_Speedup << "1 , 0 , 0 , 2 , 1 , 0 , 1 , 1 , 0 , 0 , 0 , 1 , 1 , 0 , 0 , 2 , 4 , 1 , 13 , 8 , 13 , 0 , 0 , "; 
    }
    else if(tokens[0].find("multiplication")!=-1)
    {
        fout_Classification << "1 , 3 , 0 , 2 , 1 , 0 , 4 , 3 , 0 , 0 , 1 , 0 , 4 , 0 , 0 , 3 , 5 , 4 , 26 , 8 , 17 , 0 , 0 , "; 
        fout_Speedup << "1 , 3 , 0 , 2 , 1 , 0 , 4 , 3 , 0 , 0 , 1 , 0 , 4 , 0 , 0 , 3 , 5 , 4 , 26 , 8 , 17 , 0 , 0 , "; 
    }
    else if(tokens[0].find("subtraction")!=-1)
    {
        fout_Classification << "1 , 0 , 0 , 2 , 1 , 0 , 1 , 1 , 0 , 0 , 0 , 0 , 1 , 1 , 0 , 2 , 4 , 1 , 13 , 8 , 13 , 0 , 0 , "; 
        fout_Speedup << "1 , 0 , 0 , 2 , 1 , 0 , 1 , 1 , 0 , 0 , 0 , 0 , 1 , 1 , 0 , 2 , 4 , 1 , 13 , 8 , 13 , 0 , 0 , "; 
    }

    // Matrix Size 

    fout_Classification << tokens[1] << " , ";
    fout_Speedup << tokens[1] << " , ";

    // CPU & Speedup

    if (fc < fg)
    {
        //fout_Classification << "CPU\n";
        Cpu_Count+=1;
        Speed_Up.insert((int)((fg-fc)*10));
        List_Speed_Up.push_back((int)((fg-fc)*10));
        
        fout_Classification << "0\n";
        fout_Speedup << fg-fc << "\n"; 
    }
    else 
    {
        //fout_Classification << "GPU\n"; 
        Gpu_Count+=1;
        Speed_Up.insert((int)((fc-fg)*10));
        List_Speed_Up.push_back((int)((fc-fg)*10));

        fout_Classification << "1\n";
        fout_Speedup << fc-fg << "\n";
    }
    
    fout_Classification.close();
    fout_Speedup.close();

    }

    remove("Data_Analysis.csv");


   fstream fout_Analysis;// file pointer 

   fout_Analysis.open("Data_Analysis.csv", ios::out | ios::app); 

   fout_Analysis << "CPU Count : " << Cpu_Count << endl;

   fout_Analysis << "GPU Count : " << Gpu_Count << endl;

   for (auto elem : Speed_Up)
    {
        fout_Analysis << "Speedup Difference " << elem/10.0 << " : " << count(List_Speed_Up.begin(),List_Speed_Up.end(),elem) << endl;
    }

   fout_Analysis.close();

}
