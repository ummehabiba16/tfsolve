---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "(i) The kernel is launched as <<<1, ARRAY_SIZE>>>: one block with ARRAY_SIZE threads, and a block can have at most 1024 threads, so larger sizes fail to launch and out[] is never computed. (ii) Launch several blocks: threads = 256, blocks = (n + 255)/256, global index i = blockIdx.x * blockDim.x + threadIdx.x with the existing i < n guard (or a grid-stride loop)."
sources: ["NVIDIA CUDA C Programming Guide (thread hierarchy: blocks, grids, 1024 threads per block, blockIdx/blockDim/threadIdx)"]
---
**(i) Why it works only up to 1024**

The launch `vecSquare<<<1, ARRAY_SIZE>>>` creates **one thread block** containing ARRAY_SIZE threads, and each thread squares the element `threadIdx.x`. A thread block can contain **at most 1024 threads**. For ARRAY_SIZE > 1024 the launch configuration is invalid: the kernel does not run at all (the launch returns an "invalid configuration" error, which the program does not check), so `h_out` gets garbage. Also, using only `threadIdx.x` as the index cannot address more than one block's elements.

**(ii) Modified program for any ARRAY_SIZE**

Use a **grid of many blocks** and compute a global index from the block number:

```c
#include <stdio.h>
#include <stdlib.h>
#include "cuda_runtime.h"
#include "device_launch_parameters.h"

#define ARRAY_SIZE 100000           // any size
#define THREADS_PER_BLOCK 256       // <= 1024

// the kernel
__global__ void vecSquare(float *in, float *out, int n)
{
    int i = blockIdx.x * blockDim.x + threadIdx.x;   // global index
    if (i < n)                                       // last block may be partly unused
        out[i] = in[i] * in[i];
}

int main()
{
    const int ARRAY_BYTES = ARRAY_SIZE * sizeof(float);

    // host arrays (heap, so large sizes are fine)
    float *h_in  = (float *)malloc(ARRAY_BYTES);
    float *h_out = (float *)malloc(ARRAY_BYTES);
    for (int i = 0; i < ARRAY_SIZE; i++)
        h_in[i] = float(i);

    // GPU memory
    float *d_in, *d_out;
    cudaMalloc(&d_in, ARRAY_BYTES);
    cudaMalloc(&d_out, ARRAY_BYTES);

    // host -> device
    cudaMemcpy(d_in, h_in, ARRAY_BYTES, cudaMemcpyHostToDevice);

    // enough blocks to cover all elements
    int blocks = (ARRAY_SIZE + THREADS_PER_BLOCK - 1) / THREADS_PER_BLOCK;
    vecSquare<<<blocks, THREADS_PER_BLOCK>>>(d_in, d_out, ARRAY_SIZE);

    // device -> host
    cudaMemcpy(h_out, d_out, ARRAY_BYTES, cudaMemcpyDeviceToHost);

    // free memory
    cudaFree(d_in);
    cudaFree(d_out);
    free(h_in);
    free(h_out);
    return 0;
}
```

`blocks` is the ceiling of ARRAY_SIZE / 256, so there are at least ARRAY_SIZE threads; the `if (i < n)` test stops the extra threads in the last block from writing past the array. (For extremely large arrays, beyond the grid-size limit, a grid-stride loop `for (i = ...; i < n; i += blockDim.x * gridDim.x)` can be used in the kernel.)
