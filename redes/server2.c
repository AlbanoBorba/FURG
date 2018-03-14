#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

int main(){
	int server_sockfd, client_sockfd;
	int server_len, client_len;
	struct sockaddr_in server_address;
	struct sockaddr_in client_address;
	char message[50] = "";
	char output[50] = "";
	char op;
	int divisor, i=0, temp, out;
	char num1[10] = "", num2[10] = "";
	
	server_sockfd = socket(AF_INET, SOCK_STREAM, 0);
	server_address.sin_family = AF_INET;
	server_address.sin_addr.s_addr = htonl(INADDR_ANY);
	server_address.sin_port = 1100;
	server_len = sizeof(server_address);
	bind(server_sockfd, (struct sockaddr *)&server_address, server_len);
	listen(server_sockfd, 5);
	while (1){
		printf("waiting 4 u\n");
		client_len = sizeof(client_address);
		client_sockfd = accept(server_sockfd, (struct sockaddr *)&client_address, &client_len);
		read(client_sockfd, message, 50);
		op = message[0];
		i = 2;
		while(1){
			if(message[i]!=' ')
				num1[i-2] = message[i];
			else{
				num1[i-2] = '\0';
				break;
			}
			i++;
		}
		temp = i;
		while(1){
			if(message[i] != ' ')
				num2[i-temp] = message[i];
			else{
				num2[i-temp] = '\0';
				break;
			}
			i++;
		}
		switch(op){
			case '+':
				out = atoi(num1) + atoi(num2);
				break;
			case '-':
				out = atoi(num1) - atoi(num2);
				break;
			case '*':
				out = atoi(num1) * atoi(num2);
				break;
			case '/':
				out = atoi(num1) / atoi(num2);
				break;
		}
		printf("out: %d\n", out);
		sprintf(output, "%d", out);
		write(client_sockfd, output, 50);
		close(client_sockfd);
	}
	return 0;
}
