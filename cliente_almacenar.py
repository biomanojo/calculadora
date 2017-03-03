#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Inicio del programa
#import json
import socket
#import menu_operaciones
ruta_s = socket.socket()

#dirección ip del servidor
ruta_s.connect(("localhost", 35000))

while True:
    #usuario = 'admin'
    #clave = '1234'


        usuario = raw_input('username: ')
        ruta_s.send(usuario)
        clave = raw_input('password: ')
        ruta_s.send(clave)
        datos =ruta_s.recv(1024)
        if datos =="bienvenidos":
            print datos


        print """
        seleccionar alguna de las opciones:
        a para sumar"
        b para restar
        c para multiplicqar
        d para dividir
        e para salir
        """
        opcion= raw_input("digite alguna opcion ")
        ruta_s.send(opcion)
        numero1 = int(raw_input("digite el primer numero:"))
        ruta_s.send(str(numero1))
        numero2 = int(raw_input("digite el segundo numero:"))
        ruta_s.send(str(numero2))


        if opcion == 'a':
            suma = numero1 + numero2
            print "resultado",suma
            #ruta_s.send(str(suma))
            opcion = raw_input("digite alguna opcion ")

        elif opcion == 'b':
            resta = numero1 - numero2
            print "resultado",resta

        elif opcion == 'c':
            mult = numero1 * numero2
            print "resultado",mult

        elif opcion == 'd':
            divicion = numero1 / numero2
            print "resultado",divicion

        elif opcion == 'e':
            break

           # mensaje = raw_input(' ')
            #if mensaje == "salir":
                #break


print "Regrese Cuando Quiera"



#cerrar conexión con el servidor
ruta_s.close()