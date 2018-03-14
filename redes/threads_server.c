#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <string.h>

int valor;

void* soma(int x){
  valor += x;
}
void* subtrai(int x){
  valor -= x;
}


int main(){
  valor = 0;
	pthread_t thread1, thread2, thread3, thread4, thread5;
  pthread_create(&thread1, NULL, soma, 5);
  pthread_join(thread1, NULL);
  pthread_create(&thread2, NULL, soma, 3);
  pthread_join(thread2, NULL);
  pthread_create(&thread3, NULL, soma, 1);
  pthread_join(thread3, NULL);
  pthread_create(&thread4, NULL, subtrai, 3);
  pthread_join(thread4, NULL);
  pthread_create(&thread5, NULL, subtrai, 7);
  pthread_join(thread5, NULL);
}
