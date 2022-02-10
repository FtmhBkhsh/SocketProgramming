from os import close
import socket
import threading
#pickle is used for serializing and deserializing a python object structure
import pickle

def select_a_leader(s):
    global leader
    global node_ip
    global node_number
    sending=True
    ip_list=list(nodes.values())
    #iterate_trough_all_nodes
    for i in range(len(nodes)):
        if node_ip==ip_list[i]: 
        #I_am_a_server_now_and_I_recieve_other_node_numbers
                print("ready for communication ...\n")
                for j in range(len(nodes)-1):
                    recieve_connection, client_addr = s.accept()               
                    numbers = (recieve_connection.recv(1024))
                    print("connection received from: ", client_addr, "its number is: ",numbers) 
                    num_of_nodes.append(int(str(numbers).split("'")[1]))
                num_of_nodes.append(int(node_number))  
        else: 
            #I_am_a_client_now_and_I_send_my_number_to_a_node
            send_connection = socket.socket()    
            while sending: 
                try:
                    destination_address = (ip_list[i], 9000)
                    send_data(send_connection,destination_address,str(node_number))                  
                    print("send my number to node: ", ip_list[i])
                    #connection.connect(destination_address)
                    #connection.send((str(node_number)).encode(encoding='UTF-8'))
                    sending=False
                except:   
                    print("server is not ready yet!")
        sending=True                     
    send_connection.close()
    recieve_connection.close()

    #leader_is_who_has_the_minimum_number
    leader=min(num_of_nodes) 
    print("I think the leader is: ",leader)
    number_of_awk=0                                            

    if node_number!=str(leader): 
        #ready_to_get_anouncement
        recieve_connection, client_addrr = s.accept()           
        announced_leader = (recieve_connection.recv(1024))
        if leader==int(announced_leader):
            send_connection = socket.socket()    
            while True: 
                    try:
                        destination_address = (nodes[str(leader)], 9000)
                        send_data(send_connection,destination_address,str(1))
                        print("I confirm the Leader") 
                        break
                    except:   
                        print("server should listen")

        else:
            print("I do not confirm the Leader") 
            send_data(send_connection,destination_address,str(0))

    else: 
        sending=True                     
        for i in range(len(nodes)):
            send_connection = socket.socket()    
            if node_ip!=ip_list[i]:   
                while sending: 
                    try:
                        print("I am the leader and i am introducing myself to: ",ip_list[i])
                        destination_address = (ip_list[i], 9000)
                        send_data(send_connection,destination_address,str(leader))
                        sending=False
                    except:   
                        print("followers are not ready yet!")
            sending=True 
        for j in range(len(nodes)-1):
            conne, server_addr = s.accept() 
            print("I got an answer from: ", server_addr) 
            leader_awk = (conne.recv(len(nodes)-1))
            if (int(leader_awk)):
                number_of_awk=int(leader_awk)+1
    if number_of_awk==len(nodes)-1:
        print("Everyone think leader is: ",leader)
    send_connection.close()
    recieve_connection.close()


def send_data(connection,adress,data):
    connection.connect(adress)
    connection.send(data.encode(encoding='UTF-8'))


def propagate_data():
    print("reaching consensus")
    for key in nodes:
        if node_ip!=nodes[key]:
            connection = socket.socket()    
            destination_address = (nodes[key], 9000)
            print("recent data sent to node: ", nodes[key])
            connection.connect(destination_address)                       
            pickle_of_data=pickle.dumps(data[-3:])
            connection.sendall(pickle_of_data)
            connection.close()
    
def receive_message(connection, client_address):
    global leader
    global node_ip
    global node_number
    global counter
    #reciever_is_leader_or_clients?
    if str(leader)==node_number:#reciever_is_the_leader
        #handle_request
        new_data = connection.recv(1024)
        connection.send(b"L")
        int_new_data=str(new_data).split("'")[1]
        print("from: ", client_address, "message: ",int_new_data )
        data.append(int_new_data)
        print(data)
        counter=1+counter
        #check_status
        if counter==3:
            #syncronize_data
            propagate_data()
            counter=0
    else:#reciever_is_a_client
        #sender_is_leader_or_client?
        if client_address[0]==nodes[str(leader)]: #sender_is_the_leader_and_it_update_data
            new_pickle_data = connection.recv(1024) 
            new_data=pickle.loads(new_pickle_data)
            for item in new_data:
                data.append(item)
            print("my data is: ", data) 
        else: #sender_is_client_and_It_data_request_to_leader
            new_data = connection.recv(1024)
            connection.send(b"C")
            if len(new_data):
                new_connection = socket.socket()
                leader_address = (nodes[str(leader)], 9000)
                print("send data to leader: ", nodes[str(leader)])
                new_connection.connect(leader_address)
                new_connection.send(new_data)
                new_connection.close()
    connection.close()


def main():
    s = socket.socket()
    s.bind(welcome_address)
    s.listen(5)
    #leader_selection
    if leader==0:
        select_a_leader(s)
    print("ready for serving requests ...\n")
    while True:
        connection, client_addr = s.accept()
        print("connection received from: ", client_addr) 
        #receive_message(connection, client_addr)
        th = thread = threading.Thread(target=receive_message, args=[connection, client_addr])
        th.start()

leader=0
node_ip=socket.gethostbyname(socket.gethostname())
node_number=node_ip.split(".")[3]
nodes = {
  "2": "192.168.10.2",
  "11": "192.168.10.11",
  "12": "192.168.10.12"
}
counter=0
num_of_nodes=[]
data=[]
welcome_address = ("0.0.0.0", 9000)

if __name__ == "__main__":
    main()

