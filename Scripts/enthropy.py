import math

zeros=0
ones=0
lenf=0

with open("original.jpg", "rb") as f:
    byte = f.read(1)
    while byte != b"":
        byte=bin(int(byte.hex(),base=16))[2:].zfill(8)
        zeros+=byte.count('0')
        ones+=byte.count('1')
        lenf+=8
        byte = f.read(1)

print(-math.log2(zeros/lenf), -math.log2(ones/lenf))
