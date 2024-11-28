import time
import random
def receive_ack(expected_frame):
    time.sleep(1) 
    return random.choices([expected_frame, None],weights=[0.4,0.6])[0]  

frames = [x for x in range(10)]
window_size = 4
sent = 0
ack =0

def handle_lost_frames(lost_frames):
    lost_again =[]
    if lost_frames == []: 
        return
    for frame in lost_frames:
        ackno = receive_ack(frame)
        if ackno == None:
            print(f"acknowledgement for {frame} was lost....")
            lost_again.append(frame)
        else:
            print(f"acknowledgment of {frame} was recieved.....")
    handle_lost_frames(lost_again)


while ack < len(frames):
    lost_frames = []
    for i in range(ack,min(ack+window_size,len(frames))):
        print("sending frame ",i)
    
    for i in range(ack,min(ack+window_size,len(frames))):
        ackno = receive_ack(i)
        if ackno==None:
            print(f"acknowledgement for {i} was lost....")
            ack += 1
            lost_frames.append(i)
        else:
            print(f"acknowledgment of {i} was recieved.....")
            ack += 1

    handle_lost_frames(lost_frames)
    

    