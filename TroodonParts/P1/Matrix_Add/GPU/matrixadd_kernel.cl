
/* kernel.cl 
 * Matrix multiplication: C = A * B.
 * Device code.
 */
 
// OpenCL Kernel
__kernel void
matrixMul(__global float* C, 
          __global float* A, 
          __global float* B, 
          int wA, int wB)
{
  
   int tx = get_global_id(0); 
   int ty = get_global_id(1);
 
   // value stores the element that is 
   // computed by the thread
   float value = 0;
   float elementA = A[ty * wA + tx];
   float elementB = B[ty * wA + tx];
   value = elementA + elementB;
 
   // Write the matrix to device memory each 
   // thread writes one element
   C[ty * wA + tx] = value;
}
