import socket 
# import sys
# import time

host = '172.16.111.9'
port = 12345
c = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
	# data = sys.argv[1]
	data = input("please input:")
	if not data:
		break
	c.sendto(data.encode(),(host,port))
	data2,adder = c.recvfrom(1024)
	print(data2.decode())

c.close()
