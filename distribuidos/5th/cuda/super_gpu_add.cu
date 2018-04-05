#include <iostream>
#include <math.h>

// Kernel Function to tell GPU that it can run there
__global__
void add(int n, float *x, float *y){
    int index = blockIdx.x * blockDim.x + threadIdx.x;
    int stride = blockDim.x * gridDim.x;
    for (int i=index; i<n; i+=stride)
        y[i] = x[i] + y[i];
}

int main(void){
    int N = 1<<20; // 1M elements
    int blockSize = 256;
    int numBlocks = (N + blockSize - 1) / blockSize;
    
    // allocate unified memory: accessible from CPU or GPU
    float *x, *y;
    cudaMallocManaged(&x, N*sizeof(float));
    cudaMallocManaged(&y, N*sizeof(float));

    for (int i=0; i<N; i++){
        x[i] = 1.0f;
        y[i] = 2.0f;
    }

    // run kernel function on 1M elements on the GPU
    add<<<numBlocks, blockSize>>>(N, x, y);

    // wait for GPU to finish
    cudaDeviceSynchronize();

    float maxError = 0.0f;
    for (int i=0; i<N; i++)
        maxError = fmax(maxError, fabs(y[i]-3.0f));
    std::cout << "Max error: " << maxError << std::endl;

    // free memory
    cudaFree(x);
    cudaFree(y);
    
    return 0;
}