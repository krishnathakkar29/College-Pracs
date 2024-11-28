import socket

s = socket.socket()

print("socket created...")

s.bind(('localhost',5000))

print("waiting for connection...")
s.listen(3)
c, addr = s.accept()
print("connected with ",addr)
recieved_message = ""
recieved_frames = []
while recieved_message!= "$":
    message = c.recv(1024)
    if message.decode()=="$":
        print("recieved all frames...")
        c.close()
        break
    else:
        print(f"Recieved: {message.decode()}")
    x = "ACK"+str(int(message.decode()[1:])+1)
    c.send(x.encode())
    if message.decode()!="$":
        recieved_frames.append(message.decode())
    print(recieved_frames)
s.close()
print("....program ended....")