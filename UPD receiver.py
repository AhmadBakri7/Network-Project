from socket import * #importing everything from the soocket library
import time #importing the time library

serverPort = 5566 #setting the port number
serverSocket = socket(AF_INET, SOCK_DGRAM) #this is for creating a udp connection
serverSocket.bind(('0.0.0.0', serverPort)) #this adds the server port and ip(0.0.0.0) to the server socket so it can be seen publicly
print("server is ready to recieve")
count = 0 #to ensure that there is no data loss
start = time.time() #this equals 0, as the time has just started
while True: #the loop keeps going until client finishes sending data
    message, clientAddress = serverSocket.recvfrom(2048) #This is the message that was sent by the client, being recieved here by the server(the number from 0-1000000), and the address of the client
    print(str(message.decode())) #this prints the message (the number from 0-1000000)
    count = count+1 #incrementing count by 1, as the message also gets incremented
    end = time.time() #this equals the time that the whole process took
    print("time it took is "+str(end - start)) #printing the time
    print("count is "+str(count)) #this prints the counter, as it should be equal to the value of message
