import socket
import time

def communicate_with_server(client_socket):
    while True:
        try:
            x = int(input("Enter number of requests"))
            for i in range(0,x):
                # time.sleep(0.5)
                client_socket.send("1".encode())
                y= client_socket.recv(1024).decode()
                print(f"Server: {y}")
            
            
        except Exception as e:
            print("Connection terminated!")
            client_socket.close()
            break

def create_client():
    client_socket = socket.socket()
    host = '127.0.0.2'
    port = 6000
    client_socket.connect((host,port))
    print("Connection established !!")
    return client_socket

client_socket = create_client()
communicate_with_server(client_socket)