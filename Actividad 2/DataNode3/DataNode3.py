import socket

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
			#c.send(data.encode('ascii'))
			break

		data = "Mensaje recibido, amiwo"
		c.send(data.encode('ascii'))
		count+=1

	
	s.close()

Main()
