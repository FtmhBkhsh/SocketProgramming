from os import close
import socket
import threading
import os


def receive_message(connection, client_address):
    global history_dic
    while True:
     try:
        message = connection.recv(1024)
        if message:
            print("client: ", client_address, "message: ", message)      
            if message == b't':
                history_dic[client_address]=False    
                connection.close()
                print(client_address,":download is canceled")
                break
            if message == b'p':
                history_dic[client_address]=False   
                print(client_address,":download is paused")
            if message == b'r':
                history_dic[client_address]=True  
                print(client_address,":download is resumed")
     except:
            connection.close()
            #print("close",e)                
                

                


def send_message(connection,client_address):
    global history_dic
    try:
        filesize = os.path.getsize("music.mp3")
        connection.send(str(filesize).encode(encoding='UTF-8'))
        with open("music.mp3",'rb') as output:
            while True:
                if history_dic[client_address]  :
                    data = output.read(buffer_size)
                    bytes=data         
                    if not data:
                        connection.close()
                        print("the download is completed")
                        break
                    else:
                        connection.sendall(bytes)

    except:
            connection.close()
            #print("close",e)


def main():
    #initialize welcoming socket
    s = socket.socket()
    s.bind(server_address)
    s.listen(5)
    print("Server is ready ...")
    try:
        while True:
            #receive a connection request
            connection, client_addr = s.accept()
            print("\nconnection received from: ", client_addr)
            history_dic[client_addr]=True
            #run functions as threads
            receive_thread =  threading.Thread(target=receive_message, args=[connection,client_addr])
            receive_thread.daemon=True
            receive_thread.start()
            send_thread = threading.Thread(target=send_message, args=[connection,client_addr])
            send_thread.daemon=True
            send_thread.start()
    except:
        s.close()
        #print("close",e)


buffer_size=1024
server_address = ("0.0.0.0", 9000)
#a dictionary for recording the state of each download
history_dic={}
if __name__ == "__main__":
    main()

