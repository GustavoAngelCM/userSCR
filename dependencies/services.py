import os

from getpass import getpass

def createUsers():
	os.system("clear")
	arrayToFile, usuario, password, confirmPassword, grupo, nombre, numero, telefono,   c,   error, exit = [], '', '', '', '', '', '', '', 0, False, False
	print("************CREAR USUARIO************\n\nCampos requeridos *\n")
	while exit is False:
		usuario = inputObligatorio("el nombre de Usuario")
		if usuario == '' : 
			exit = True
			break
		while True:
			password = secretObligatorio("su clave")
			if password == '' : break
			confirmPassword = secretObligatorio("su clave nuevamente")
			break
		if password == '' or confirmPassword == '' or password!=confirmPassword: 
			exit = True
			break
		grupo = input("Introduzca el nombre de grupo al que desea asignar: ")
		nombre = input("Introduzca el nombre completo: ")
		numero = input("Introduzca el numero de habitacion: ")
		telefono = input("Introduzca el numero de telefono: ")
		arrayToFile = [
			password+'\n',
			confirmPassword+'\n',
			nombre+'\n',
			numero+'\n',
			telefono+'\n',
			'\n',
			'\n',
			'S',
		]
		archivo = open('data.g', 'w')
		archivo.writelines(arrayToFile)
		archivo.close()
		os.system('sudo adduser ' + usuario + ' < data.g')
		if grupo != '' and usuario!=grupo : 
			os.system('sudo  addgroup ' + grupo)
			os.system('sudo  usermod -g ' + grupo + ' ' + usuario)
			os.system('sudo  delgroup ' + usuario)
			print("\n[ Aviso ]Reasignación de grupo\n\n")
		break
	if exit is True:
		print("\n\n[ ERROR ] Valor inesperado. \n\nIngrese un usuario o verifique que las claves ingresadas sean iguales.\n\nPresiona [ ENTER ]")
		errorF = input()
	else:
		print("\n\nComando ejecutado... \n\nVerificando creacion de usuario.\n\n")
		os.system('cat /etc/passwd | grep ' + usuario)
		print('\n\nPresiona [ ENTER ]\n')
		verificando = input()

def deleteUser(): 
	os.system("clear")
	print("************ELIMINAR USUARIO************\n\nCampos requeridos *\n")
	usuario = inputObligatorio("el usuario a eliminar")
	if usuario != '' :
		os.system('sudo deluser --remove-home ' + usuario)
		print("\n\nComando ejecutado... \n\nVerificando eliminacion de usuario.\n\n")
		os.system('cat /etc/passwd | grep ' + usuario)
		print('\n\nPresiona [ ENTER ]\n')
		errorF = input()
	else : 
		print("\n\n[ ERROR ] Valor inesperado. \n\nIngrese un usuario.\n\nPresiona [ ENTER ]")
		errorF = input()

def createGroup():
	os.system("clear")
	print("************CREAR GRUPO************\n\nCampos requeridos *\n")
	grupo = inputObligatorio("el nombre del grupo")
	if grupo != '' :
		os.system('sudo addgroup ' + grupo)
		print("\n\nComando ejecutado... \n\nVerificando creacion de grupo.\n\n")
		os.system('cat /etc/group | grep ' + grupo)
		print('\n\nPresiona [ ENTER ]\n')
		errorF = input()
	else : 
		print("\n\n[ ERROR ] Valor inesperado. \n\nIngrese un nombre de grupo.\n\nPresiona [ ENTER ]")
		errorF = input()

def deleteGroup():
	os.system("clear")
	print("************ELIMINAR GRUPO************\n\nCampos requeridos *\n")
	grupo = inputObligatorio("el nombre del grupo a eliminar")
	if grupo != '' :
		os.system('sudo delgroup ' + grupo)
		print("\n\nComando ejecutado... \n\nVerificando eliminacion de grupo.\n\n")
		os.system('cat /etc/group | grep ' + grupo)
		print('\n\nPresiona [ ENTER ]\n')
		errorF = input()
	else : 
		print("\n\n[ ERROR ] Valor inesperado. \n\nIngrese un nombre de grupo.\n\nPresiona [ ENTER ]")
		errorF = input()

def deleteCertifiedSSH():
	# os.system('ssh -i .sshANGELCEREZO/keyangelcerezo angelcerezo@192.168.1.21')
	usuario, ip, clave, purchase = '', '', '', ''
	os.system('clear')
	print("************CREAR CERTIFICADO SSH************\n\nCampos requeridos *\n")
	usuario = inputObligatorio('el nombre de usuario con el que desea conectarse')
	if usuario != '':
		clave = secretObligatorio('su clave')
		if clave != '':
			ip = inputObligatorio('la direccion ip del servidor')
			if ip != '':
				arrayIP =  ip.split('.')
				try:
					if  ( len(arrayIP) == 4 and
						 ( int(arrayIP[0]) >= 0 and int(arrayIP[0]) < 256 ) and
						 ( int(arrayIP[1]) >= 0 and int(arrayIP[1]) < 256 ) and
						 ( int(arrayIP[2]) >= 0 and int(arrayIP[2]) < 256 ) and
						 ( int(arrayIP[3]) >= 0 and int(arrayIP[3]) < 256 ) ) :
						purchase = secretObligatorio('la clave de la llave SSH de autenticacion')
						if purchase != '' and len(purchase) > 5 :
							encript = input("Ingresa la encriptacion del KEYGEN [ rsa / dsa ] default [rsa]: ")
							arrayToFile = [
								'.ssh'+usuario.upper()+'/key_'+usuario.lower()+'\n',
								purchase+'\n',
								purchase
							]
							archivo = open('data.g', 'w')
							archivo.writelines(arrayToFile)
							archivo.close()
							os.system('mkdir .ssh' + usuario.upper())
							if encript != '' :							
								os.system('ssh-keygen -t ' + encript + ' < data.g')								
								ejecutarConexion(usuario, ip, True)
								valor = input()
							else :
								os.system('ssh-keygen < data.g')
								ejecutarConexion(usuario, ip, True)
								valor = input()
						else :
							print("\n\n[ ERROR ] Valor inesperado. \n\nIngrese su clave SSH correctamente.\n\nPresiona [ ENTER ]")
							errorF = input()
					else :
						print("\n\n[ ERROR ] Valor inesperado. \n\nIngrese formato de IP valido.\n\nPresiona [ ENTER ]")
						errorF = input()
				except Exception as e:
					print(e)
					print("\n\n[ ERROR ] Valor inesperado. \n\nIngrese formato de IP valido.\n\nPresiona [ ENTER ]")
					errorF = input()
			else :
				print("\n\n[ ERROR ] Valor inesperado. \n\nIngrese la direccion IP.\n\nPresiona [ ENTER ]")
				errorF = input()
		else :
			print("\n\n[ ERROR ] Valor inesperado. \n\nIngrese su clave.\n\nPresiona [ ENTER ]")
			errorF = input()
	else :
		print("\n\n[ ERROR ] Valor inesperado. \n\nIngrese un nombre usuario.\n\nPresiona [ ENTER ]")
		errorF = input()

def ejecutarConexion(usuario, ip, init):
	os.system('rm data.g')
	print('\n\nSe abrira una conexion con el servidor')
	if init :
		print('\npor favor vuelva a introducir la contraseña')
		print('\nseguidamente ejecute los siguientes comandos\n\npara poder hacer efectiva la conexion ssh')
		print('\n\n\t[1]	cd ~')
		print('\n\n\t[2]	mkdir .ssh/')
		print('\n\n\t[2]	exit')
	print('\n\nPresiona [ ENTER ]\n\n')
	enter = input()
	os.system('ssh ' + usuario + '@' + ip)
	os.system('clear')
	print('Coneccion cerrada')
	print('\nSe abrira una conexion con el servidor')
	print('\npuede que se le pida la contraseña nuevamente')
	print('\nCopiando la llave de autenticacion al servidor\n')
	os.system('scp .ssh'+usuario.upper()+'/key_'+usuario.lower()+'.pub '+usuario+'@'+ip+':.ssh/authorized_keys')


def inputObligatorio(textoInput):
	valorInput, c, error = '', 0, False
	while valorInput == '' and c < 3:
		c = c + 1
		if error : print("[Error] este campo no debe ser vacio. (%d)" % (c))
		valorInput = input("Introduzca " + textoInput + " *: ")
		if valorInput == '' : error = True
	return valorInput


def secretObligatorio(textoSecret):
	valorSecret, c, error = '', 0, False
	while valorSecret == '' and c < 3:
		c = c + 1
		if error : print("[Error] este campo no debe ser vacio. (%d)" % (c))
		valorSecret = getpass("Introduzca " + textoSecret + " *: ")
		if valorSecret == '' : error = True
	return valorSecret