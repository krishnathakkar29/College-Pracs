
data = input("Enter the data bits (e.g., 1010): ")
generator = input("Enter the generator polynomial bits (e.g., 1101): ")

data_waith_zeros = data + '0' * (len(generator) - 1)

remainder = data_with_zeros[:len(generator)]
count = len(generator)

def xor(remainder,generator):
    answer = ''
    for i in range(1,len(generator)):
            answer = answer+'0' if remainder[i] == generator[i]  else answer+'1'
    return answer


while count < len(data_with_zeros):
    if remainder[0] == '1':
        remainder = xor(remainder,generator)
        remainder += data_with_zeros[count]
        count += 1

    else:
        remainder = remainder[1:] + data_with_zeros[count]
        count += 1
remainder = remainder[1:]

print(f'The remainder is {remainder}')
print(f'the answer is {data+remainder}')