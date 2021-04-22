//Usman - MS-Semester Project

#include "llvm/Pass.h"
#include "llvm/IR/Module.h"
#include "llvm/Support/raw_ostream.h"
#include "llvm/IR/LegacyPassManager.h"
#include "llvm/Transforms/IPO/PassManagerBuilder.h"
#include <fstream>
#include <iostream>
#include <CL/cl.h>
using namespace llvm;

namespace {
  struct SkeletonPass : public ModulePass {
    static char ID;
	int inst=0;
	int block=0;
	int func=0;
	int instload=0;
	int inststore=0;
	int instbr=0;
	int instreturn=0;
	int installoc=0;
	int instfmul=0;
	int instmul=0;
	int instfdiv=0;
	int instsdiv=0;
	int insticmp=0;
	int instfadd=0;
	int instadd=0;
	int instfsub=0;
	int instsub=0;
	int instcall=0;

	FILE * myfile;
	
	
    SkeletonPass() : ModulePass(ID) {}

    virtual bool runOnModule(Module &M) {
        for (auto& F : M) {
	
             	errs() << "\tFunction: " << F.getName() << "\n";
		func++;

            for (auto& BB : F) {
                errs() << "\t\tBasic Block: " << BB.getName() << "\n";
		block++;

                for (auto& I : BB) {
                   errs() << "\t\t\tInstruction: " << I.getOpcodeName() << "\n";
		 //   errs() << "\t\t\tOpcode " << I.getOpcode() << "\n";
		    
		  	if(I.getOpcode()==30)
				{instload++;}
			else if(I.getOpcode()==31)
				{inststore++;}
			else if(I.getOpcode()==2)
				{instbr++;}
			else if(I.getOpcode()==1)
				{instreturn++;}
			else if(I.getOpcode()==29)
				{installoc++;} 
			else if(I.getOpcode()==16)
				{instfmul++;}
			else if(I.getOpcode()==11)
				{instadd++;}
			else if(I.getOpcode()==15)
				{instmul++;}
			else if(I.getOpcode()==19)
				{instfdiv++;}
			else if(I.getOpcode()==18)
				{instsdiv++;} 
			else if(I.getOpcode()==51)
				{insticmp++;} 
			else if(I.getOpcode()==12)
				{instfadd++;} 
			else if(I.getOpcode()==11)
				{instadd++;} 
			else if(I.getOpcode()==14)
				{instfsub++;} 
			else if(I.getOpcode()==13)
				{instsub++;} 
			else if(I.getOpcode()==54)
				{instcall++;} 
			inst++;
                }
            }
        }
	
	//errs() << "\n \t\t\tTotal no of Functions: " << func << "\n";
	//errs() << "\t\t\tTotal no of Blocks: " << block << "\n";
	//errs() << "\t\t\tTotal no of Instructions: " << inst << "\n";
	//errs() << "\t\t\t\tTotal no of load Instructions: " << instload << "\n";
	//errs() << "\t\t\t\tTotal no of store Instructions: " << inststore << "\n";
	//errs() << "\t\t\t\tTotal no of Control Statement Instructions: " << instbr << "\n  ";
	//errs() << "\t\t\t\tTotal no of Math Operation " << instfadd << "\n \n ";


	myfile = fopen ("../../b1.txt","a");
	
	fprintf(myfile,"\n"); 
	fprintf(myfile, "[1]- Total no of Return statement: " ); 
	fprintf(myfile, "%d",instreturn);
	fprintf(myfile,"\n"); 
	fprintf(myfile, "[2]- Total no of Control Statement:" ); 
	fprintf(myfile, "%d",instbr );
	fprintf(myfile,"\n"); 
	fprintf(myfile, "[3]- Total no of Allocation instruction: " ); 
	fprintf(myfile, "%d",installoc);
	fprintf(myfile,"\n");
	fprintf(myfile, "[4]- Total no of Load Instructions:" ); 
	fprintf(myfile, "%d",instload );
	fprintf(myfile,"\n"); 
	fprintf(myfile, "[5]- Total no of Store Instructions:" ); 
	fprintf(myfile, "%d",inststore );
	fprintf(myfile,"\n"); 
	fprintf(myfile, "[6]- Total no of Multiplication (Float Datatype) Operation: " ); 
	fprintf(myfile, "%d",instfmul);
	fprintf(myfile,"\n"); 
	fprintf(myfile, "[7]- Total no of Addition(Integer Datatype) Instruction: " ); 
	fprintf(myfile, "%d",instadd); 
	fprintf(myfile,"\n"); 
	fprintf(myfile, "[8]- Total no of Multiplication(Integer Datatype) Instruction: " ); 
	fprintf(myfile, "%d",instmul); 
	fprintf(myfile,"\n"); 
 	fprintf(myfile, "[9]- Total no of Division(Float Datatype) instruction: " ); 
	fprintf(myfile, "%d",instfdiv); 
	fprintf(myfile,"\n"); 
	fprintf(myfile, "[10]-Total no of Division(Integer Datatype) instruction: " ); 
	fprintf(myfile, "%d",instsdiv); 
	fprintf(myfile,"\n"); 
	fprintf(myfile, "[11]-Total no of Condition Check instruction: " ); 
	fprintf(myfile, "%d",insticmp); 
	fprintf(myfile,"\n"); 
	fprintf(myfile, "[12]-Total no of Addition(Float Datatype) instruction: " ); 
	fprintf(myfile, "%d", instfadd);
	fprintf(myfile,"\n"); 
	fprintf(myfile, "[13]-Total no of Addition(Integer Datatype) instruction: " ); 
	fprintf(myfile, "%d", instadd);
	fprintf(myfile,"\n"); 
	fprintf(myfile, "[14]-Total no of Subtraction(Float Datatype) instruction: " ); 
	fprintf(myfile, "%d", instfsub);
	fprintf(myfile,"\n"); 
	fprintf(myfile, "[15]-Total no of Subtraction(Integer Datatype) instruction: " ); 
	fprintf(myfile, "%d", instsub);
	fprintf(myfile,"\n"); 
	fprintf(myfile, "[16]-Total no of Function Call instruction: " ); 
	fprintf(myfile, "%d", instcall);
	fprintf(myfile,"\n"); 
	fprintf(myfile, "[17]-Total no of Functions:" ); 
	fprintf(myfile, "%d",func); 
	fprintf(myfile,"\n"); 
	fprintf(myfile, "[18]-Total no of Blocks:" ); 
	fprintf(myfile, "%d",block);
	fprintf(myfile,"\n"); 
	fprintf(myfile, "[19]-Total no of Instructions:" ); 
	fprintf(myfile, "%d",inst);
	
	

	fclose (myfile); 
        
        return false;
    }
  };
}

char SkeletonPass::ID = 0;


static void registerSkeletonPass(const PassManagerBuilder &,
                         legacy::PassManagerBase &PM) {
  PM.add(new SkeletonPass());
}

static RegisterStandardPasses RegisterMyPass(PassManagerBuilder::EP_ModuleOptimizerEarly,
                                                registerSkeletonPass);

static RegisterStandardPasses RegisterMyPass1(PassManagerBuilder::EP_EnabledOnOptLevel0,
                                                registerSkeletonPass);
