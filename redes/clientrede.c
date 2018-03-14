#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]){
	int sockfd, port, len, result;
	struct sockaddr_in address;
	char word[50], output[50];

	port = atoi(argv[2]);

	sockfd = socket(AF_INET, SOCK_STREAM, 0);
	address.sin_family = AF_INET;
	address.sin_addr.s_addr = inet_addr(argv[1]);
	address.sin_port = 1100;
	len = sizeof(address);
	result = connect(sockfd, (struct sockaddr *)&address, len);
	if(result == -1){
		perror("vixe\n");
		exit(1);
	}

	printf("Digite a mensagem:\n");
	scanf("%s", word);
	write(sockfd, word, 50);
	read(sockfd, output, 50);
	printf("Voce recebeu:\n%s\n", output);
	close(sockfd);
	exit(0);
	return 0;
}
