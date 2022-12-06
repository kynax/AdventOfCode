import sys

data = [l.strip() for l in sys.stdin][0]

packet = True
message = True
i = 0
while packet or message:
    if packet and len(set(data[i:i+4])) == 4:
        print('start of packet', i+4)
        packet = False
        
    if message and len(set(data[i:i+14])) == 14:
        print('start of message', i+14)
        message = False
        
    i += 1