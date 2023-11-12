from socket import * #importing everything from the soocket library
import time #importing the time library

serverPort = 5566 #setting the port number
serverSocket = socket(AF_INET, SOCK_STREAM) #this is for creating a tcp connection
serverSocket.bind(('0.0.0.0', serverPort)) #this adds the server port and ip(127.0.0.1) to the server socket

print("The server is ready to receive")
serverSocket.listen(1) #This makes the server ready to recieve from client

count = 0 #to ensure that there is no data loss
start = time.time() #this equals 0, as the time has just started
while True:
    connectionSocket, addr = serverSocket.accept() #This means that the server starts recieving packets from the client, and stores the address of client
    message = connectionSocket.recv(2048) #This is the message that was sent by the client, being recieved here by the server(the number from 0-1000000)
    connectionSocket.send(str(message).encode()) #this send back the message that the server recieved to the client
    print(str(message.decode())) #this prints the message (the number from 0-1000000)
    count = count + 1 #incrementing count by 1, as the message also gets incremented
    connectionSocket.close() #closing the connection with the client
    serverSocket.listen(1) #making the server listen again to what the cient has to send
    print("count is " + str(count)) #this prints the counter, as it should be equal to the value of messageipc
    end = time.time() #this equals the time that the process took until now
    print("time it took is "+str(end - start)) #printing the time