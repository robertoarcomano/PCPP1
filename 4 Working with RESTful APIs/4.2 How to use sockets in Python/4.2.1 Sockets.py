"""
1 Create a new socket:
    1.1 Protocol: socket.AF_INET / socket.AF_UNIX
    1.2 socket.SOCK_STREAM / socket.SOCK_DGRAM
2 Client -> Connect -> Use of a tuple, 2 double brackets
3 socket.send(bytes) to send data. For sending bytes, the following is needed:
    3.1 bytes(TEXT, FORMAT) -> bytes("GET / HTTP/1.0\n\n", encoding="utf8")
    3.2 bTEXT
4 socket.recv(MAX_BYTES)
5 closing sockets:
    5.1 socket.close just decrements the open FD
    5.2 socket.shutdown(socket.SHUT_RDWR) definitely closes the connection, even for other threads
6 repr(text)
7 Exceptions:
    7.1 socket.gaierror, coming from getaddrinfo()
    7.2 socket.timeout
"""
import socket
SERVER_IP = "www.google.com"
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_connection = my_socket.connect((SERVER_IP, 80))
my_socket.send(bytes("GET / HTTP/1.0\n\n", encoding='utf8'))
print(my_socket.recv(10000))
my_socket.shutdown(socket.SHUT_RDWR)
my_socket.close()
