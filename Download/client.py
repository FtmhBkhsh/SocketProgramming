import socket
import time
import tqdm
import threading


def listen(sckt):
    while True:
        try:
            order=input()
            if order == "p":
                sckt.sendall(b'p')
                print("pause order")
            if order == "r":
                sckt.sendall(b'r')
                print("resume order")
            if order == "t":
                sckt.sendall(b't')
                print("termination order")
                sckt.close()
                break
        except:
            print("socket is closed!")
            break




def receive(sckt,progress,int_filesize):
    with open("my_file.mp3", 'wb+') as output:
        while True:
            try:
                rec = sckt.recv(buffer_size)
                time.sleep(0.001)            
                if not rec:
                    continue
                output.write(rec)
                progress.update(buffer_size)
            except:    
                print("download completed or terminated")
                output.close()
                sckt.close()
                break



def main():
    try:
            sckt = socket.socket()
            print("\nconnect to server: ", server_address)
            print("enter <p> for pause, <r> for resume and <t> for temination\n")
            sckt.connect(server_address)
            filesize = (sckt.recv(7))
            int_filesize=int(filesize)
            progress = tqdm.tqdm(range(int_filesize), f"receiving", unit="B", unit_scale=True, unit_divisor=1024,disable=False)
            #run functions as threads
            listen_thread = thread = threading.Thread(target=listen,args=[sckt])
            listen_thread.start()
            receive_thread = thread = threading.Thread(target=receive,args=[sckt,progress,int_filesize])
            receive_thread.start()

    except Exception as e:
            sckt.close()
            print("close",e)

    
buffer_size=1024
server_address = ("192.168.10.2", 9000)

if __name__ == "__main__":
    main()

