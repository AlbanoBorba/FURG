// C program for implementation of Bubble sort
#include <stdio.h>
#include <ctime>
#include <thread>
#include <iostream>
#include <vector>
#include <atomic>
#include <chrono>

using namespace std;
using namespace std::chrono;

const int num_threads = 1;
const int size = 1000;
const int groups = 400;

void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}
 
// A function to implement bubble sort
void bubbleSort(int arr[], int n)
{
   int i, j;
   for (i = 0; i < n-1; i++)      
 
       // Last i elements are already in place   
       for (j = 0; j < n-i-1; j++) 
           if (arr[j] > arr[j+1])
              swap(&arr[j], &arr[j+1]);
}

int partition (int arr[], int low, int high)
{
    int pivot = arr[high];    // pivot
    int i = (low - 1);  // Index of smaller element
 
    for (int j = low; j <= high- 1; j++)
    {
        // If current element is smaller than or
        // equal to pivot
        if (arr[j] <= pivot)
        {
            i++;    // increment index of smaller element
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}
 
/* The main function that implements QuickSort
 arr[] --> Array to be sorted,
  low  --> Starting index,
  high  --> Ending index */
void quickSort(int arr[], int low, int high)
{
    if (low < high)
    {
        /* pi is partitioning index, arr[p] is now
           at right place */
        int pi = partition(arr, low, high);
 
        // Separately sort elements before
        // partition and after partition
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

void sequentialQuick(int group[groups][size]){
    for(int i=0; i<groups; i++)
        quickSort(group[i], 0, size-1);
}

void sequentialBubble(int group[groups][size]){
    for(int i=0; i<groups; i++)
        bubbleSort(group[i], size);
}

void oneQuick(int group[groups][size], int start, int num_threads){
    for(int i=start; i<groups; i+=num_threads)
        quickSort(group[i], 0, size-1);
}

void oneBubble(int group[groups][size], int start, int num_threads){
    for(int i=start; i<groups; i+=num_threads)
        bubbleSort(group[i], size);
}

int sum_arr(atomic<int> arr[], int num_threads){
    int total = 0;
    for(int i=0; i<num_threads; i++)
        total += arr[i];
    return total;
}

void parallelQuick(int group[groups][size], int num_threads){
    int sum_value;
    thread my_threads[128];
    for(int i=0;i<num_threads;i++)
        my_threads[i] = thread(oneQuick, group, i, num_threads);
    for(int i=0;i<num_threads;i++)
        my_threads[i].join();
}

void parallelBubble(int group[groups][size], int num_threads){
    thread my_threads[128];
    for(int i=0;i<num_threads;i++)
        my_threads[i] = thread(oneBubble, group, i, num_threads);
    for(int i=0;i<num_threads;i++)
        my_threads[i].join();
}

void copy_array(int origin[groups][size], int destiny[groups][size]){
    for(int i=0;i<groups;i++){
        for(int j=0;j<size;j++)
        destiny[i][j] = origin[i][j];
    }
}

void print_array(int arr[size]){
    for(int i=0; i<size;i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main(){
    int group[groups][size];
    int group2[groups][size];
    int group3[groups][size];
    int group4[groups][size];
    

    high_resolution_clock::time_point begin;   // create timers.
    high_resolution_clock::time_point end;
    for(int num_threads=1; num_threads<=16; num_threads*=2){
        srand((unsigned)time(0)); 

        for(int j=0; j<groups; j++) 
            for(int i=0; i<size; i++)
                group[j][i] = (rand()%10000);
        copy_array(group, group2);
        copy_array(group, group3);
        copy_array(group, group4);
        
        printf("%d threads, %d arrays with %d elements each\n", num_threads, groups, size);

        begin = high_resolution_clock::now();
        parallelQuick(group, num_threads);
        end = high_resolution_clock::now();
        auto duration3 = duration_cast<microseconds>( end - begin ).count();
        //cout << "parallel quick: " << duration3 << " microseconds" << endl;
        cout << duration3 << " ";

        begin = high_resolution_clock::now();
        sequentialQuick(group2);
        end = high_resolution_clock::now();
        auto duration1 = duration_cast<microseconds>( end - begin ).count();
        //cout << "sequential quick: " << duration1 << " microseconds" << endl;
        cout << duration1 << " ";

        begin = high_resolution_clock::now();
        parallelBubble(group3, num_threads);
        end = high_resolution_clock::now();
        auto duration4 = duration_cast<microseconds>( end - begin ).count();
        //cout << "parallel bubble: " << duration4 << " microseconds" << endl;
        cout << duration4 << " ";
        
        begin = high_resolution_clock::now();
        sequentialBubble(group4);
        end = high_resolution_clock::now();
        auto duration2 = duration_cast<microseconds>( end - begin ).count();
        //cout << "sequential bubble: " << duration2 << " microseconds" << endl;
        cout << duration2 << endl;
        
        cout << "quick difference: " << duration1 - duration3 << endl;
        cout << "bubble difference: " << duration2 - duration4 << endl;
    }
}