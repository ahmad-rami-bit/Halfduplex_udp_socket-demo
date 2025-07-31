from socket import *

serverPort =1234
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print("server is ready")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    if message.decode()!=str(0):
        print(message.decode())
        modifiedmsg=input("type:")
        serverSocket.sendto(modifiedmsg.encode(), clientAddress)
    else:serverSocket.close()