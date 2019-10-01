import socket

def Main():
	HOST = 'server'
	PORT = 5000
	count=1
	flag=True

	with open("log.txt", "w") as log:
		log.write("<-Archivo de registro, formato 'Mensaje::IP'->\n\n")

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

		with open("log.txt","a") as log:
			escribir = "{}. {}::{}\n".format(count, MSG, addr[0])
			log.write(escribir)
	
		if(MSG=="exit"):
			data = "Chao amiwo"
			c.send(data.encode('ascii'))
			break

		data = "Mensaje recibido, amiwo"
		c.send(data.encode('ascii'))
		count+=1

	
	s.close()

Main()
