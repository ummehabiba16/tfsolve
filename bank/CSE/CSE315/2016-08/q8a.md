---
marks: 17
topics: [gpu-cuda]
kind: code
source: {page: 79-80}
---
Consider the following CUDA program:

```c
#include <stdio.h>
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#define ARRAY_SIZE 10
float h_in[ARRAY_SIZE];
float h_out[ARRAY_SIZE];
// the kernel
__global__ void vecSquare(float * in , float * out, int n)
{
    int i = threadIdx.x;
    if(i < n)
    {
        out[i] = in[i] * in[i];
    }
}
int main()
{
    const int ARRAY_BYTES = ARRAY_SIZE * sizeof(float);
    // generate the input array on the host
    for(int i=0; i<ARRAY_SIZE; i++)
    {
        h_in[i] = float(i);
    }
    // declare GPU memory pointers
    float * d_in;
    float * d_out;
    // allocate GPU memory
    cudaMalloc( &d_in, ARRAY_BYTES);
    cudaMalloc( &d_out, ARRAY_BYTES);
    // transfer the array to the GPU
    cudaMemcpy(d_in, h_in, ARRAY_BYTES, cudaMemcpyHostToDevice);
    // launch the kernel
    vecSquare<<< 1,ARRAY_SIZE >>>(d_in,d_out, ARRAY_SIZE);
    // copy back the result array to the CPU
    cudaMemcpy(h_out, d_out, ARRAY_BYTES, cudaMemcpyDeviceToHost);
    // free GPU memory allocation
    cudaFree(d_in);
    cudaFree(d_out);
    return 0;
}
```

This program performs square of each array element using NVIDIA GPU. Answer the following questions considering this program:

(i) If you run this program varying the value of ARRAY_SIZE (defined in line 4), you would notice that this program successfully works for ARRAY_SIZE upto 1024. What is the reason for this? **Hints:** A thread block can contain maximum 1024 threads.

(ii) Modify this program so that it can work for arbitrary value of ARRAY_SIZE. Rewrite the complete program.
