import socket

host = ''
port = 12345

c = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
c.bind((host,port))

while True:
	print("please waiting!")
	data,adder = c.recvfrom(1024)
	if(data):
		print(adder , data.decode())
	c.sendto("收到".encode(),adder)
	
c.close()