from socket import socket
from time import asctime

server_socket = socket()
server_socket.bind(("0.0.0.0", 3777))
server_socket.listen(5)
while(1):
    (client_socket, client_address) = server_socket.accept()
    time_string = asctime() + "\r\n"
    client_socket.sendall(bytes(time_string, "utf-8"))
    client_socket.close()
