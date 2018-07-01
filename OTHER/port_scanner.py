import socket
from termcolor import colored

color_green = colored("[+]",'green')
color_red = colored("[!]", 'red')
color_yellow = colored("[!]", 'yellow')

def scan_separate():
	print("~"*50)

	host = input(color_yellow + "HOST --> ")
	port = int(input(color_yellow + "PORT --> "))

	print("~"*50)

	scan = socket.socket()

	try:
		scan.connect((host,port)) # передаём один аргумент через кортеж
	except socket.error:
		print(color_red + "Port --", port, "[CLOSED]")
	else:
		print(color_green + "Port --", port, "[OPEN]")

def scan_list():
	print("~"*50)

	host = input(color_yellow + "HOST --> ")
	ports = [20, 21, 22, 23, 42, 43, 53, 67, 69, 80, 443, 8080, 8000]
	
	print("~"*50)

	for port in ports:
		try:
			scan = socket.socket()
			scan.settimeout(0.5)
			scan.connect((host,port))
		except socket.error:
			print(color_red + "Port --", port, "[CLOSED]")
		else:
			print(color_green + "Port --", port, "[OPEN]")

print("~~"*25)
print("\t[1] --- scan separate port")
print("\t[2] --- scan list")
print("~~"*25,"\n")

text_a = input("[scan] ---> ")

if text_a == "1":
	scan_separate()
elif text_a == "2":
	scan_list()
else:
	print(colored("Введи хоть это правильно!",'red'))
