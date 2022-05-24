
import socket
import sys

HOST, PORT = "localhost", 9999
data = "Test"


with socket.socket(socket.AF_INET, socket.SOCK_RAW,socket.IPPROTO_TCP) as sock:
    sock.recvfrom(1024)
    #sock.connect((HOST, PORT))
    #sock.sendall(bytes(data + "\n", "utf-8"),1)

    #
    # Receive data from the server and shut down
    #received = str(sock.recv(1024), "utf-8")

print("Sent:     {}".format(data))
