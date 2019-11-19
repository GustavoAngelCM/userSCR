import os

def mainMenu():
	os.system("clear")
	print("+--------------------------------------------------------+")
	print("|                ADMINISTRACION DE SERVIDORES            |")
	print("+--------------------------------------------------------+")
	print("| [1]. USERS  =>  USER|SSH|JAIL|WEB                      |")
	print("| [0]. SALIR                                             |")
	print("+--------------------------------------------------------+")
	print("|Selecciona una opcion  [ 0 - 1 ]                        |")
	print("+--------------------------------------------------------+")

def usersMenu():
	os.system("clear")
	print("+--------------------------------------------------------+")
	print("|         ADMINISTRACION DE SERVIDORES [USERS]           |")
	print("+--------------------------------------------------------+")
	print("| [1]. CREAR USUARIO                                     |")
	print("| [2]. BORRAR USUARIO                                    |")
	print("| [3]. CREAR GRUPO                                       |")
	print("| [4]. BORRAR GRUPO                                      |")
	print("| [5]. CREAR CERTIFICADO SSH                             |")
	print("| [0]. VOLVER                                            |")
	print("+--------------------------------------------------------+")
	print("|Selecciona una opcion  [ 0 - 3 ]                        |")
	print("+--------------------------------------------------------+")	