from socket import * #importing everything from the soocket library
serverName = 'localhost' #Thsi is the ip address of the server that the client is going to connect with (local host = 127.0.0.1)
serverPort = 5566 #Thsi is the port number of the server
clientSocket = socket(AF_INET, SOCK_STREAM) #this is for creating a tcp connection
clientSocket.connect(('localhost', 5566)) #this establishes a connection with the server, with its ip addreess and port number

for x in range(0, 1000001): #this loop increments x after each run, sending x to the server
    clientSocket.send(str(x).encode()) #this sends x (packet) to the server
    clientSocket.close() #this closes the connection between the client and server
    clientSocket = socket(AF_INET, SOCK_STREAM) #this is again for creating a tcp connection
    clientSocket.connect(('localhost', 5566)) #this again establishes a connection with the server, with its ip addreess and port number