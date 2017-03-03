#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Inicio del programa

import socket
import json
#Crear una variable de conexión tipo socket
server = socket.socket()

#Dirección IP del servidor y puerto de conexión
server.bind(("", 35000))

#Cuantas conexiones se van a escuchar
server.listen(1)
ruta_c, addr = server.accept()
#nombre_equipo = socket.gethostname()
#ruta_c.chdir('escritorio')
#Si se recibe algo de la ruta acepta la conexión y almacena la dirección aceptada
#ruta_c, direccion = server.accept()
usuario = 'admin'
clave = '1234'
#numero1='true'
#numero2='true'

while True:
    recibido = ruta_c.recv(1024)
    recibido1 = ruta_c.recv(1024)
    if usuario == recibido and clave == recibido1:
        print "bienvedidos"
        mensaje = 'bienvenidos'
        ruta_c.send(mensaje)
    else:
         print "Usuario y contrasena incorrectos."

    #opcion = raw_input(">")
    #ruta_c.send(opcion)
    #a = ruta_c.recv(1024)
    #a = input("digite el primer numero:")
    #b = ruta_c.recv(1024)
    #b = input("digite el primer numero:")

    opcion1 = ruta_c.recv(1024)
    #opcion2 = ruta_c.recv(1024)
    #opcion3 = ruta_c.recv(1024)
   # dato = json.loads(opcion1,opcion2,opcion3)
   # if opcion1 == opcion1:
        #suma = opcion2 + opcion3
        #print suma
        #ruta_c.send(suma)



    #Tamaño de los mensajes enviados por el cliente
    ruta_c.send(recibido)
    ruta_c.send(recibido1)
    if recibido1 == 'si':
        break

    #imprimir la dirección IP del Cliente
    print str(addr[0]) + "Envio: ", recibido
    #print str(time[0]) + "Envio: ", recibido
    print "Envío desde el cliente : ", recibido
    #Devolver petición al cliente

#print "Hasta la Vista!!! Baby"

#Cerrar ruta del cliente y servidor
ruta_c.close()
server.close()
