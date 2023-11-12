import os
from socket import *
serverPort = 7788
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)
print ("Server is ready to recieve")
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    print (addr)
    print (sentence)
    ip=addr[0]
    port=addr[1]
    print ("ip is "+str(ip))
    print ("port is "+str(port))

    FirstLine = sentence.splitlines()[0]
    FirstLineWithoutSpaces = FirstLine.split(" ")
    token = FirstLineWithoutSpaces[1]
    tokenwithoutslash = token.split("/")[1]

    if token=="/" or token=="/index.html" or token=="/main_en.html" or token=="/en":
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        f1 = open("main_en.html", "rb")
        connectionSocket.send(f1.read())
        connectionSocket.close()

    elif token=="/ar":
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        f1 = open("main_ar.html", "rb")
        connectionSocket.send(f1.read())
        connectionSocket.close()

    elif token=="/go":
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
        connectionSocket.send("Location: https://www.google.com \r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    elif token=="/so":
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
        connectionSocket.send("Location: https://www.stackoverflow.com \r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    elif token=="/bzu":
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
        connectionSocket.send("Location: https://www.birzeit.edu/en/b-hub \r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    # connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
    # connectionSocket.send("Location: https://www.google.com \r\n".encode())

    else:
        if os.path.isfile(tokenwithoutslash):
            tokenwithoutdotbefore = tokenwithoutslash.split(".")[0]
            tokenwithoutdotafter = tokenwithoutslash.split(".")[1]

            if tokenwithoutdotafter=="html":
                connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
                connectionSocket.send("Content-Type: text/html \r\n".encode())
                connectionSocket.send("\r\n".encode())
                f1 = open(tokenwithoutslash, "rb")
                connectionSocket.send(f1.read())
                connectionSocket.close()

            elif tokenwithoutdotafter=="css":
                connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
                connectionSocket.send("Content-Type: text/css \r\n".encode())
                connectionSocket.send("\r\n".encode())
                f1 = open(tokenwithoutslash, "rb")
                connectionSocket.send(f1.read())
                connectionSocket.close()

            elif tokenwithoutdotafter=="png":
                connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
                connectionSocket.send("Content-Type: image/png \r\n".encode())
                connectionSocket.send("\r\n".encode())
                f1 = open(tokenwithoutslash, "rb")
                connectionSocket.send(f1.read())
                connectionSocket.close()

            elif tokenwithoutdotafter == "jpg":
                connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
                connectionSocket.send("Content-Type: image/jpeg \r\n".encode())
                connectionSocket.send("\r\n".encode())
                f1 = open(tokenwithoutslash, "rb")
                connectionSocket.send(f1.read())
                connectionSocket.close()

            else:
                connectionSocket.send("“HTTP/1.1 200 OK \r\n".encode())
                connectionSocket.send("Content-Type: text/html \r\n".encode())
                connectionSocket.send("\r\n".encode())
                f1 = open("404.html", "rb")
                connectionSocket.send(f1.read())
                connectionSocket.close()

        else:
            connectionSocket.send("HTTP/1.1 404 Not Found \r\n".encode())
            connectionSocket.send("Content-Type: text/html \r\n".encode())
            connectionSocket.send("\r\n".encode())
            f1 = open("404.html", "rb")
            # Creating an HTML file
            errorFile = open("404.html", "w")
            # Adding input data to the HTML file
            errorFile.write("<!DOCTYPE html> \
                            <html> \
                            <head> \
                            <title>Error</title> \
                            <style> \
                                .ForPort{ \
                                    font - weight: bold; \
                                } \
                            </style> \
                            </head> \
                            <body> \
                            <h1 align=""center"" style=""color:red;""> \
                            <br><br><br><br><br><br> ""The file is not found"" <br> \
                            </h1> \
                            <h2 align=""center"" class=""h2""> \
                             ""Ayman Salama 1200488"" <br> \
                             ""Ahmad Bakri 1201509"" <br> \
                             ""Samuel Tannous 1201123"" <br> \
                            </h2> \
                            </body> \
                            </html>")
            errorFile.write("<br><br><h1 class=""ForPort"">IP is </h1>" + str(ip))
            errorFile.write("<h1 class=""ForPort"">port is </h1>" + str(port))
            # Saving the data into the HTML file
            errorFile.close()
            connectionSocket.send(f1.read())
            connectionSocket.close()