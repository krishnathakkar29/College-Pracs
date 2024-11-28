import socket
import random
import time
c = socket.socket()
c.connect(('localhost',5000))
print("Connected successfully....")
frames = int(input("enter number of frames:"))
time_out = int(input("enter time_out time:"))
ack=0
frame =[]
for i in range(0,frames):
    frame.append(f"F{i}")
print(frame)
while ack<frames:
    while True:    
        actual_time = abs(random.normalvariate(0,time_out))
        time.sleep(actual_time)
        if actual_time>time_out:
            print("time out of acknowledgement occurred....RESENDING")
        else:
            break
    message = frame[ack].encode()
    c.send(message)
    message = c.recv(1024)
    print(f"recieved {message.decode()} after {actual_time} seconds")
    ack += 1

c.send("$".encode())
c.close()
print("...Program ended...")