import socket
import struct
import sys
from threading import Thread

def mc():

	multicast_group = '224.3.29.71'
	server_address = ('', 10000)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind(server_address)
	group = socket.inet_aton(multicast_group)
	mreq = struct.pack('4sL', group, socket.INADDR_ANY)
	sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

	while True:
		data, address = sock.recvfrom(1024)
		ack = 'ack1'
		sock.sendto(ack.encode('ascii'), address)


def Main():
	HOST = 'datanode3'
	PORT = 1003
	count=1
	flag=True

	with open("data.txt", "w") as log:
		log.write("<-Registro de mensajes->\n\n")

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	print("Socket conectado al puerto", PORT)
	host_name = socket.gethostname()
	host_ip=socket.gethostbyname(host_name)

	print("LA IP ES: ", host_ip)

	s.listen(5)
	print("Socket escuchando...")

	c,addr = s.accept()


	while(flag):
		data = c.recv(1024)
		MSG = data.decode()
		print("Mensaje recibido: ",MSG)

		with open("data.txt","a") as log:
			escribir = "{}. {}\n".format(count, MSG)
			log.write(escribir)
	
		if(MSG=="exit"):
			data = "Chawo amiwo"
			break

		data = "Mensaje recibido, amiwo"
		c.send(data.encode('ascii'))
		count+=1

	
	s.close()

th1 = Thread(target=Main,args=[])
th2 = Thread(target=mc,args=[])

th2.start()
th1.start()

th2.join()
th1.join()
