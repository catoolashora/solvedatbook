from socket import *
from _codecs import ascii_encode


def http_get(server, filename):
    s = socket()
    s.connect((server, 80))
    aniohevetpaz = "GET "  + filename + " HTTP/1.0 \r\n\r\n"
    enc = bytes(aniohevetpaz, "utf-8")
    s.sendall(enc)
    data = s.recv(1000000000)
    s.close()
    return data

goo = http_get("www.google.com", "/")
print(goo)