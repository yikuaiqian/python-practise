import socket
import sys

host = sys.argv[1]
service = {'21':'ftp','23':'Telnet','25':'smtp','53':'DNS','69':'tftp','80':'http','135':'rpc','137':'NetBIOS','139':'Samba','1521':'Oracle','1433':'SQL_Server','3306':'Mysql','3389':'Remote_Destop'}

port = [21,23,25,53,69,80,135,137,139,1521,1433,3306,3389]

print("please waiting!")

for p in port:
	try:
		c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		c.connect((host,p))
		print(str(p) + ' '+service[str(p)] + " is open!")
	except :
		print(str(p) + ' '+service[str(p)] + " is not open!")
	finally:
		c.close()
		del c