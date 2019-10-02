import socket
import random
import sys, os

def Main():
	HOST = 'headnode'
	PORT = 5000
	count=1
	flag=True

	with open("registro_server.txt", "w") as log:
		log.write("<-Archivo de registro, formato 'Mensaje::IP'->\n\n")

	with open("heartbeat_server.txt", "w") as log:
		log.write("<-Registro multicasting->\n\n")

	s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	HOST1 = 'datanode1'
	HOST2 = 'datanode2'
	HOST3 = 'datanode3'

	PORT1 = 1001
	PORT2 = 1002
	PORT3 = 1003

	s1.connect((HOST1,PORT1))
	s2.connect((HOST2,PORT2))
	s3.connect((HOST3,PORT3))

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	print("Socket conectado al puerto", PORT)
	host_name = socket.gethostname()
	host_ip=socket.gethostbyname(host_name)

	print("LA IP ES: ", host_ip)

	s.listen(5)
	print("Socket escuchando...")

	c, addr = s.accept()
	print("Conectado a: ", addr[0], ':', addr[1])


	while(flag):
		data = c.recv(1024)
		MSG = data.decode()
		print("Mensaje recibido: ",MSG)

	
		if(MSG=="exit"):
			data = "Chao amiwo"
			c.send(data.encode('ascii'))
			break


		r = random.randint(0,3)
		if(r==0):
			s1.send(MSG.encode('ascii'))
			with open("registro_server.txt","a") as log:
				escribir = "{}. {}::{}\n".format(count, MSG, HOST1)
				log.write(escribir)
		elif(r==1):
			s2.send(MSG.encode('ascii'))
			with open("registro_server.txt","a") as log:
				escribir = "{}. {}::{}\n".format(count, MSG, HOST2)
				log.write(escribir)
		else:
			s3.send(MSG.encode('ascii'))
			with open("registro_server.txt","a") as log:
				escribir = "{}. {}::{}\n".format(count, MSG, HOST3)
				log.write(escribir)

		data = "Mensaje recibido, amiwo"
		c.send(data.encode('ascii'))
		count+=1

	data = "exit"
	s1.send(data.encode('ascii'))
	s2.send(data.encode('ascii'))
	s3.send(data.encode('ascii'))
	
	s.close()
	s1.close()
	s2.close()
	s3.close()

Main()
