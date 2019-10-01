import socket

def Main():
	HOST = 'server'
	PORT = 5000
	count=1
	peticiones=[
		"primero",
		"segundo",
		"tercero",
		"exit"
		]

	with open("respuestas.txt","w") as resp:
		resp.write("<-Archivo de respuestas recibidas por el servidor->\n\n")

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	message = "Hola Serviduwu!"

	s.send(message.encode('ascii'))
	data = s.recv(1024)
	MSG = str(data.decode('ascii'))

	with open("respuestas.txt","a") as resp:
		escribir = "{}. {}\n".format(count,MSG)
		resp.write(escribir)

	print(HOST, "dice:", MSG)

	count+=1
	for req in peticiones:
		s.send(req.encode('ascii'))
		data = s.recv(1024)
		MSG = str(data.decode('ascii'))

		with open("respuestas.txt","a") as resp:
			escribir = "{}. {}\n".format(count,MSG)
			resp.write(escribir)

		print(HOST, "dice:", MSG)
		count+=1


	s.close()

Main()
