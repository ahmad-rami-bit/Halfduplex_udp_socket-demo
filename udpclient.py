from socket import *
serverName='localhost'
serverPort=1234
clientSocket = socket(AF_INET, SOCK_DGRAM)
while True:
    message = input('type:')
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    modifiedmsg, serverAddress = clientSocket.recvfrom(2048)
    if modifiedmsg.decode()!=str(0):
            print(modifiedmsg)
    else:   
        message=0
        clientSocket.sendto(str(message).encode(),(serverName,serverPort))
        clientSocket.close()
