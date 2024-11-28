data_list = input("enter data:")
data = [int(i) for i in data_list.split()]
p1 = data[0] ^ data[1] ^ data[3]
p2 = data[0] ^ data[2] ^ data[3]
p4 = data[1] ^ data[2] ^ data[3]

data.insert(0,p1)
data.insert(1,p2)
data.insert(3,p4)

print(data)

idx = int(input("enter the index to add the error in:"))

print(idx)

data[idx]=0 if data[idx]==1 else 1

print(data)

p1 = data[0] ^ data[2] ^ data[4] ^ data[6]
p2 = data[1] ^ data[2] ^ data[5] ^ data[6]
p4 = data[3] ^ data[4] ^ data[5] ^ data[6]

error = (p1*1 + p2*2 + p4*4 )-1 

if error == 0:
    print("no error found")
else:
    print("error found at index ",error)