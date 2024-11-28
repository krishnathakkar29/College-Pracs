import time
import random
def receive_ack(expected_frame):
    time.sleep(1) 
    return random.choices([expected_frame, None],weights=[0.6,0.4])[0]  

frames = [x for x in range(10)]
window_size = 4
sent = 0
ack =0

while ack < len(frames):
    for i in range(ack,min(ack+window_size,len(frames))):
        print("sending frame ",i)
    
    for i in range(ack,min(ack+window_size,len(frames))):   
        ackno = receive_ack(i)
        if ackno==None:
            print(f"acknowledgement for {i} was lost....")
            print(f"resending the frames from {i}")
            break
        else:
            print(f"acknowledgment of {i} was recieved.....")
            ack += 1
