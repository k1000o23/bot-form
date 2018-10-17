#Autor: Camilo Andrés Bruna 
import re,urllib,sys
import urllib.request
import requests
import os
from urllib import request, parse
from robobrowser import RoboBrowser
import pandas as pd
from random import randint
import random
import string

#comprueba la conexion a una web
def conectar(url):
	try:
		var_c = requests.get(url)
		if var_c.status_code != 200:
			sys.stderr.write("! Error {} retrieving url {}".format(var_c.status_code, url))
			return None
		return print("ok: ", var_c.status_code)	

	except Exception as e: 
		print ("No es posible conectar...")
		print (e)
		#sys.exit(1)

#lista los parametros de un form y los devuelve en forma de array
def parametros(enlace):
	try:
	  var = urllib.request.urlopen(enlace).read()
	except Exception as e: 
	  print (e)
	  print ("No es posible conectar...")
	  #sys.exit(1)
	url_enviar=""
	for url in re.findall("<form (.*)>",var.decode('utf-8')):
	  if "action" in url.lower():
	    for web in url.split():
	      if re.findall("action=(.*)",web):
	        url_enviar=web.replace("action=","")
	url_enviar = url_enviar.replace("\"","")
	datos_r = []
	for campos in re.findall("<input (.*)>",var.decode('utf-8')):
	  if "name" in campos.lower():
	    for cam in campos.split():
	      if re.findall("name=(.*)",cam):
	        datos_r.append(cam.replace('"',""))
	for s in datos_r:
		datos_r[datos_r.index(s)] =  s.replace("name=","")
	return datos_r

#crea usuarios en el pueblo pasado como parametro
def crear(url, numero):
	conectar(url)
	#para generar diferentes correos y numeros de telefono para el formulario
	def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	    """
	    Función para generar valores aleatorios
	    Puede recibir:
	        size = longitud de la cadena
	            Defecto 6
	        chars = caracteres a utilizar para buscar la cadena
	            Defecto letras mayusculas y numeros
	    """
	    return ''.join(random.choice(chars) for _ in range(size)) 
	# devuelve una cadena de 8 caracteres en minucula
	#print (id_generator(8,string.ascii_lowercase))
	 
	i = 0
	while i < numero:
		s = RoboBrowser(user_agent='MOBILE_USER_AGENT', parser="lxml", history=True)
		s.open(url)
		f= s.get_form()
		f['username'].value = 'bot'
		f['apellidos'].value = 'python'
		f['password'].value = 'bot'
		f['email'].value = id_generator(8,string.ascii_lowercase)+"@bot.es"
		f['phone'].value = randint(600000000, 999999999)
		f['sexo'].value = 'Hombre'
		f['nacimiento'].value = '1997-01-01'
		f['universidad'].value = 'ee'
		f['camiseta'].value = 'L'
		f['coche'].value = 'No'
		f['guitarra'].value = 'No'
		f['alergias'].value = 'No'
		f['comentarios'].value = 'Test'
		f['aceptar_privacidad'].value = '1'
		f.serialize() 
		s.submit_form(f)
		i+=1
	print("Se han añadido ", numero, " usuarios nuevos","\t")

#menu de inicio del programa 
def menu():

	os.system('cls')
	print ("Opciones para la URL--> ", var_check)
	print ("\t1 - Cambiar URL")
	print ("\t2 - Check status")
	print ("\t3 - Listar parámetros")
	print ("\t4 - Crear usuarios")
	print ("\t9 - salir")

#Principio de programa	
os.system('cls')
print("  ")
print("URL por defecto: https://www.ejemplo.es/registration.php") 
var_check = "https://www.ejemplo.es/registration.php"
while True:
	# Mostramos el menu
	menu()
 
	# Opciones
	opcionMenu = input("Elige una opción >> ")
 
	if opcionMenu=="1":
		print ("")
		print("No olvides poner 'https://'") 
		var_check = input("Introduce una URL --> ")
	elif opcionMenu=="2":
		print ("")
		conectar(var_check)
		input("\npulsa una tecla para continuar")
	elif opcionMenu=="3":
		print ("")
		datos_r = parametros(var_check)
		print ("Campos Detectados:")
		for s in datos_r:
			print (s, "\t")
		input("\npulsa una tecla para continuar")
	elif opcionMenu=="4":
		print ("")
		numero = int(input("\n¿Cuantos quieres crear? -->"))
		crear(var_check, numero)
		input("\npulsa una tecla para continuar")
	elif opcionMenu=="9":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")


