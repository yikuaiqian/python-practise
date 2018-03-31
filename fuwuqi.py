import socket

host = "0.0.0.0"
port = 44444
c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

c.bind((host,port))
c.listen(5)
while True:
	print("waiting for connection..")
	a,adder = c.accept()
	print("来自地址:",adder)
	while True:
		data = a.recv(1024)
		if not data:
			break
		print(data.decode())
		a.send(data)
	a.close()
c.close()