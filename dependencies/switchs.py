from .menus import *
from .services import *

def indexSwitch():
	while True:
		mainMenu()
		opcion = input()
		if opcion == '0':
			break	
		mainSwitch(opcion)

def mainSwitch(opcion):
	if opcion == '1':
		while True:
			usersMenu()
			opcion = input()
			if opcion == '0':
				break	
			usersSwitch(opcion)
	else :
		print("\n\n[ ERROR ] Opcion no valida. \n\nIngrese valores entre [ 0 - 1 ]\n\nPresiona [ ENTER ]")
		error = input()

def usersSwitch(opcion):
	if opcion == '1':
		createUsers()
	elif opcion == '2' :
		deleteUser()
	elif opcion == '3' :
		createGroup()
	elif opcion == '4' :
		deleteGroup()
	elif opcion == '5' :
		deleteCertifiedSSH()
	else :
		print("\n\n[ ERROR ] Opcion no valida. \n\nIngrese valores entre [ 0 - 3 ]\n\nPresiona [ ENTER ]")
		error = input()