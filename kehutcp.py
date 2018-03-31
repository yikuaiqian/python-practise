import socket

target_host = '172.16.111.9'
target_port = 78965
c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect((target_host,target_port))

while True:
	a = input("请输入：")
	if not a :
		break;
	c.send(a.encode())
	data=c.recv(1024)
	print("接收到的：" + data.decode())
c.close()

	