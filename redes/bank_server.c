#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>

int saldo = 0;
pthread_t tid[100];

void *deposito (void *valor){
  int x = int(valor)
  saldo += x;
  return;
}
void *saque (void *valor){
  int x = int(valor)
  if(saldo - x >= 0)
    saldo -= x;
  else
    write(client_sockfd, "Saldo Insuficiente\n", 50);

  return;
}

int main(int argc, char *argv[]){
	int server_sockfd, client_sockfd;
	int server_len, client_len;
	int result, flag;
	struct sockaddr_in server_address;
	struct sockaddr_in client_address;
	char message[50];
  char operator;
	server_sockfd = socket(AF_INET, SOCK_STREAM, 0);
	server_address.sin_family = AF_INET;
	server_address.sin_addr.s_addr = htonl(INADDR_ANY);
	server_address.sin_port = atoi(argv[1]);
	server_len = sizeof(server_address);
	bind(server_sockfd, (struct sockaddr *)&server_address, server_len);
	listen(server_sockfd, 1);
	while (1){
		printf("waiting 4 u\n");
		client_len = sizeof(client_address);
		client_sockfd = accept(server_sockfd, (struct sockaddr *)&client_address, &client_len);
		read(client_sockfd, message, 50);
		token = strtok(message, ":");
		op = token[0];
    if(operator == 's'){
      pthread_create(&(tid[i]), saque(atoi(message));
    }
    else if(operator == 'd'){
      deposito(atoi(message));
    }
    else{
      write(client_sockfd, "Operador invalido\n", 50);
    }
    sprintf(message, "%d", saldo);
		write(client_sockfd, message, 50);
		close(client_sockfd);
	}
	return 0;
}
