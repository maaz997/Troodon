#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string>
#include <iostream>
using namespace std;
#ifdef __APPLE__
#include <OpenCL/opencl.h>
#else
#include <CL/cl.h>
#endif

#define MAX_SOURCE_SIZE (0x100000)

int main(void) {

//<======================================= 1=> Program Id =======================================>
time_t t = time(NULL);
struct tm tm = *localtime(&t);
int program_temp_id=tm.tm_mday*1000000+tm.tm_hour*10000+tm.tm_min*100+tm.tm_sec;
//<======================================= 1=> End ****** =======================================>

//<======================================= 2=> Program ML =======================================>
string kernel_path="/home/user-admin/Desktop/Fyp_Part_3/Opencl_Test_Program/vector_add_kernel.cl"; //set
string _base="/home/user-admin/Desktop/Fyp_Part_3/Schedular/"; //set
int program_size=2048; //set

string _cmd_call="python "+_base+"pyscript.py "+kernel_path+" "+to_string(program_temp_id)+" "+to_string(program_size)+" "+_base;
system(_cmd_call.c_str());
//<======================================= 2=> End ****** =======================================>

//<======================================= 3=> Device SEL =======================================>
clock_t wait_start,wait_end,execution_end;
wait_start = clock();
/*------------------------------ Waiting for device assigning ------------------------------*/
string _Args=_base+" "+to_string(program_temp_id);
string _wait_cmd_call="python3 "+_base+"Waiting.py "+_Args;
int SEL_Device=system(_wait_cmd_call.c_str())/256;
/*------------------------------ Device assigned by schedular ------------------------------*/
wait_end = clock();

//<======================================= 3=> End ****** =======================================>

//<======================================= 4=> Device SET =======================================>
if (SEL_Device==0)
{
        /* code for running on cpu (setting cpu and its platform) */
}
else
{
        /* code for running on cpu (setting gpu and its platform) */
}
//<======================================= 4=> End ****** =======================================>

    int i;
    const int LIST_SIZE = 2048;
    int *A = (int*)malloc(sizeof(int)*LIST_SIZE);
    int *B = (int*)malloc(sizeof(int)*LIST_SIZE);
    for(i = 0; i < LIST_SIZE; i++) {
        A[i] = i;
        B[i] = LIST_SIZE - i;
    }

    // Load the kernel source code into the array source_str
    FILE *fp;
    char *source_str;
    size_t source_size;

    fp = fopen("vector_add_kernel.cl", "r");
    if (!fp) {
        fprintf(stderr, "Failed to load kernel.\n");
        exit(1);
    }
    source_str = (char*)malloc(MAX_SOURCE_SIZE);
    source_size = fread( source_str, 1, MAX_SOURCE_SIZE, fp);
    fclose( fp );

    // Get platform and device information
    cl_platform_id platform_id = NULL;
    cl_device_id device_id = NULL;   
    cl_uint ret_num_devices;
    cl_uint ret_num_platforms;
    cl_int ret = clGetPlatformIDs(1, &platform_id, &ret_num_platforms);
    ret = clGetDeviceIDs( platform_id, CL_DEVICE_TYPE_ALL, 1, 
            &device_id, &ret_num_devices);

    // Create an OpenCL context
    cl_context context = clCreateContext( NULL, 1, &device_id, NULL, NULL, &ret);

    // Create a command queue
    cl_command_queue command_queue = clCreateCommandQueueWithProperties(context, device_id, 0, &ret);

    // Create memory buffers on the device for each vector 
    cl_mem a_mem_obj = clCreateBuffer(context, CL_MEM_READ_ONLY, 
            LIST_SIZE * sizeof(int), NULL, &ret);
    cl_mem b_mem_obj = clCreateBuffer(context, CL_MEM_READ_ONLY,
            LIST_SIZE * sizeof(int), NULL, &ret);
    cl_mem c_mem_obj = clCreateBuffer(context, CL_MEM_WRITE_ONLY, 
            LIST_SIZE * sizeof(int), NULL, &ret);

    // Copy the lists A and B to their respective memory buffers
    ret = clEnqueueWriteBuffer(command_queue, a_mem_obj, CL_TRUE, 0,
            LIST_SIZE * sizeof(int), A, 0, NULL, NULL);
    ret = clEnqueueWriteBuffer(command_queue, b_mem_obj, CL_TRUE, 0, 
            LIST_SIZE * sizeof(int), B, 0, NULL, NULL);

    // Create a program from the kernel source
    cl_program program = clCreateProgramWithSource(context, 1, 
            (const char **)&source_str, (const size_t *)&source_size, &ret);

    // Build the program
    ret = clBuildProgram(program, 1, &device_id, NULL, NULL, NULL);

    // Create the OpenCL kernel
    cl_kernel kernel = clCreateKernel(program, "vector_add", &ret);

    // Set the arguments of the kernel
    ret = clSetKernelArg(kernel, 0, sizeof(cl_mem), (void *)&a_mem_obj);
    ret = clSetKernelArg(kernel, 1, sizeof(cl_mem), (void *)&b_mem_obj);
    ret = clSetKernelArg(kernel, 2, sizeof(cl_mem), (void *)&c_mem_obj);
    
    // Execute the OpenCL kernel on the list
    size_t global_item_size = LIST_SIZE; // Process the entire lists
    size_t local_item_size = 64; // Process in groups of 64
    ret = clEnqueueNDRangeKernel(command_queue, kernel, 1, NULL, 
            &global_item_size, &local_item_size, 0, NULL, NULL);

    // Read the memory buffer C on the device to the local variable C
    int *C = (int*)malloc(sizeof(int)*LIST_SIZE);
    ret = clEnqueueReadBuffer(command_queue, c_mem_obj, CL_TRUE, 0, 
            LIST_SIZE * sizeof(int), C, 0, NULL, NULL);

    // Display the result to the screen
//     for(i = 0; i < LIST_SIZE; i++)
//         printf("%d + %d = %d\n", A[i], B[i], C[i]);

    // Clean up
    ret = clFlush(command_queue);
    ret = clFinish(command_queue);
    ret = clReleaseKernel(kernel);
    ret = clReleaseProgram(program);
    ret = clReleaseMemObject(a_mem_obj);
    ret = clReleaseMemObject(b_mem_obj);
    ret = clReleaseMemObject(c_mem_obj);
    ret = clReleaseCommandQueue(command_queue);
    ret = clReleaseContext(context);
    free(A);
    free(B);
    free(C);

//<======================================= 5=> Post Exec. =======================================>
execution_end = clock();
float wait_time,exec_time;
wait_time= (wait_end-wait_start);
exec_time= (execution_end-wait_end);
wait_time= wait_time/CLOCKS_PER_SEC;
exec_time= exec_time/CLOCKS_PER_SEC;
string Start_Date=to_string(tm.tm_mday)+"-"+to_string(tm.tm_mon)+"-"+to_string(tm.tm_year+1900);
string Start_Time=to_string(tm.tm_hour)+"-"+to_string(tm.tm_min)+"-"+to_string(tm.tm_sec);

string Pass_Args=_base+" "+to_string(program_temp_id)+" "+Start_Date+" "+Start_Time+" "+to_string(SEL_Device)+" "+to_string(wait_time)+" "+to_string(exec_time);
string _end_cmd_call="python3 "+_base+"Cleaning.py "+Pass_Args;
system(_end_cmd_call.c_str());
//<======================================= 5=> End ****** =======================================>   

    return 0;
}

