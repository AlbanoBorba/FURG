#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>
#define NUM_THREADS 600

int reg;
int counter;

void *soma (void *threadid){
  int i;
  long tid;
  tid = (long)threadid;
  for(i=0; i<10; i++){
    reg = counter;
    reg = reg + 1;
    counter = reg;
    printf("%d\n", counter);
    sleep(1);
  }
}
int main(){
  pthread_t threads[NUM_THREADS];
  int i;
  for(i=0;i<NUM_THREADS;i++){
    pthread_create(&threads[i], NULL, soma, (void*) i);
  }
  pthread_exit(NULL);
}
