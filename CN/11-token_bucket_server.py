import socket
import time
import threading


MAX_TOKEN_COUNT = 5
MAX_BUCKET_SIZE = 5
bucket = MAX_BUCKET_SIZE
TOKEN_RATE = 0.5

def handle_clients(client_socket):
    global bucket
    while True:
        try:
            data = client_socket.recv(1024).decode().strip()
            
            if not data :
                continue
            else:
                
                if bucket > 0:
                    bucket = bucket - 1
                    client_socket.send("Request processed. Token consumed".encode())
                else:
                    client_socket.send("Bucket is empty Please wait...".encode())
                print(f"Tokens  remaining = {bucket}")
                
                    
        except Exception as e:
            client_socket.close()
            print("Connection Terminated!!")
            break

def token_bucket():
    
    global bucket
    while True:
        time.sleep(1/TOKEN_RATE)
        if bucket < MAX_BUCKET_SIZE:
            bucket+=1
            print(f"Token added to bucket {bucket}")
            
def start_server():
    host = '127.0.0.2'
    port = 6000
    server_socket = socket.socket()
    server_socket.bind((host,port))
    print(f"Server online on host{host} port{port}")
    server_socket.listen(5)
    threading.Thread(target = token_bucket, daemon = True).start()
    
    while True:
        client_socket,addr = server_socket.accept()
        print(f"{addr} Connected to the server!")
        threading.Thread(target=handle_clients,daemon=True,args=(client_socket,)).start()

start_server()
    