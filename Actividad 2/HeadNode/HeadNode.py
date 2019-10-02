import socket
import random
import struct
import sys, os
from threading import Thread
import time

def mc():
	multicast_group = ('224.3.29.71', 10000)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.settimeout(0.2)
	ttl = struct.pack('b', 1)
	sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

	print("holacocos")

	with open("heartbeat_server.txt", "w") as log:
		log.write("<-Registro multicasting->\n\n")


	mensaje = "tasbien?"
	

	while True:
		print("mandando mensajuwu")
		sent = sock.sendto(mensaje.encode('ascii'), multicast_group)
		
		while True:

			try:
				data, server = sock.recvfrom(16)
				with open("heartbeat_server.txt", "a") as log:
					escribir = "{}. {}\n".format(data , server)
					log.write(escribir)



			except socket.timeout:
				with open("heartbeat_server.txt", "a") as log:
					log.write("timeout \n")
				break
        
		time.sleep(5)






def Main():
	HOST = 'headnode'
	PORT = 5000
	count=0
	flag=True

	with open("registro_server.txt", "w") as log:
		log.write("<-Archivo de registro, formato 'Mensaje::IP'->\n\n")

	

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
	data = c.recv(1024)
	MSG = data.decode()
	print("Mensaje recibido: ",MSG)
	with open("registro_server.txt","a") as log:
		escribir = "{}. {}::{}\n".format(count, MSG, HOST)
		log.write(escribir)
	data = "Mensaje recibido, amiwo"
	c.send(data.encode('ascii'))
	count+=1
	
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

th1 = Thread(target=Main,args=[])
th2 = Thread(target=mc,args=[])

th2.start()
th1.start()

th2.join()
th1.join()


