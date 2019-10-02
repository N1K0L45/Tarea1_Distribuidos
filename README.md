# Tarea1 Distribuidos
Tarea 1 Sistemas Distribuidos 2019-2    

Nicolás Acevedo Y.	201573512-3  
Vicente Yagui R.	201560560-2

## Instrucciones de uso
El proyecto tiene la siguiente estrucutra:
```
├─Tarea1_Distribuidos
  ├──Actividad 1
  │  ├──Cliente
  │  ├──Server
  │  └──docker-compose.yml
  ├──Actividad 2
  │  ├──Cliente
  │  ├──DataNode1
  │  ├──DataNode2
  │  ├──DataNode3
  │  ├──HeadNode
  │  └──docker-compose.yml
  └──README.md
 ```
 Cada Actividad tiene su propio archivo ``docker-compose``, por ende, debe situarse en el directorio de la actividad que desee correr. Por ejemplo, para correr la Actividad 1, debe estar en ``/Tarea1_Distribuidos/Actividad1/``.

### Ejecución de una Actividad
Para ejecutar una actividad, solamente debe usar los comandos
```
$ docker-compose build
$ docker-compose up
```
situado obviamente en el directorio de la actividad a ejecutar, como se indicó anteriormente.

## Ubicación de archivos de Registro
Los archivos de registro (o _data logs_) de cada actividad se encuentran en el directorio de cada servicio, tal y como se indicó en el enunciado. A continuación se presenta una estructura de los directorios, mostrando solamente los nombres de los archivos:
```
├─Tarea1_Distribuidos
  ├──Actividad 1
  │  ├──Cliente
  │  │  └─respuestas.txt
  │  └──Server
  │     └─log.txt
  ├──Actividad 2
  │  ├──Cliente
  │  │  └─registro_cliente.txt  
  │  ├──DataNode1
  │  │  └─data.txt
  │  ├──DataNode2
  │  │  └─data.txt
  │  ├──DataNode3
  │  │  └─data.txt
  │  └──HeadNode
  │     ├─heartbeat_server.txt
  │     └─resgistro_server.txt
  └──README.md
 ```

 # Consideraciones Importantes
 - Los mensajes que el cliente envía están indicados en el código, y se le especifican mediante la lista ``peticiones``.
 - La actividad 2 no finaliza automáticamente, ya que se encuentra realizando multicasting cada 5 segundos de manera infinita. Por ende, debe cancelarse manualmente (``Ctrl + C``, dos veces para terminar también el proceso de Docker).
 - Recordar que la primera vez que se construye el proyecto se demora un poco más, debido a que debe descargar la imagen de Ubuntu para funcionar.
