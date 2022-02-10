import socket
import time
import random




def main():

    rand = random.randrange(0, 3)
    data = random.randrange(1, 5)
    destination = list(nodes.values())[rand]
    print("data is : ", data)
    server_address = (destination, 9000)
    s = socket.socket()
    print("send my request to : ", server_address)
    s.connect(server_address)
    s.send((str(data)).encode(encoding='UTF-8'))
    response = s.recv(1024)
    if response==b"L":
        print("the leader handle my request")
    else:
        print("a client handle my request")    

    



    s.close()


nodes = {
  "2": "192.168.10.2",
  "11": "192.168.10.11",
  "12": "192.168.10.12"
}

if __name__ == "__main__":
    main()

