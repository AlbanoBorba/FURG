#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/un.h>
#include <unistd.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  int server_socket, client_socket;
  int server_length, client_length;
  struct socketaddr server_address;
  struct socketaddr client_address;
  char ch;

  server_socket = socket(AF_INET, SOCK_STREAM, 0);
  server_address.sin_family = AF_INET;
  server_address.sin_addr.s_addr = htonl(INADDR_ANY);
  server_address.sin_port = 1100;
  server_len = sizeof(server_address);
  bind(server_socket, (struct socketaddr *) &server_address, server_len);
  listen(server_socket, 5);
  while(1){
    printf("waiting 4 u\n");
    client_length = sizeof(client_address);
    client_socket = accept(server_socket, (struct socketaddr *)
                           &client_address, &client_length);
    read(client_socket, &ch, 1);
    ch++;
    write(client_socket, &ch, 1);
    close(client_socket);
  }
  return 0;
}
