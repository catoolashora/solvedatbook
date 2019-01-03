from socket import *

server_socket = socket()
server_socket.bind(("0.0.0.0",8888))
server_socket.listen(5)
header = ""
while (1):
    (client_socket, client_adress) = server_socket.accept()
    try:
        request = str(client_socket.recv(1000).decode())
        splt = request.split(" ")
        message = "you bad boy \r\n"
        if(splt[0] != "GET"):
            message = "youre messing \r\n"
        elif(splt.__len__() != 2):
            message = "youre the dancing queen \r\n"
        elif(splt[1] in ["\r", "\n", "\r\n", "", " ", None]):
            message = "youre joking \r\n"
        else:
            try:
                    splt[1] = splt[1].split("\r")[0]
                    splt[1] = splt[1].split("\n")[0]
                    splt[1] = splt[1].split("\r\n")[0]
                    file = open(splt[1], "r").read()
                    header = "HTTP/1.0 200 Document Follows\r\nContent-length: "  + str(len(file)) + "\r\n\r\n"
                    message = header + file + " \r\n"
            except FileNotFoundError:
                message = "HTTP/1.0 404 Not Found \r\n"
        message_bytes = bytes(message, "utf-8")
        client_socket.sendall(message_bytes)
        client_socket.close()
    except UnicodeDecodeError:
        client_socket.close()
    