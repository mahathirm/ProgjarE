import socket
import time
import sys

UDP_IP = "127.0.0.1"
UDP_PORT = 5005 
filenya=["koin1.jpg", "koin2.jpg", "koin3.jpg", "koin4.jpg"]; 

for data in filenya: 
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
	sock.sendto(data, (UDP_IP, UDP_PORT)) 

	fp = open(data, "rb")
	data = fp.read()
	while(data):
	    if(sock.sendto(data, (UDP_IP, UDP_PORT))):
	        data = fp.read() 

	sock.close()
	fp.close() 
	time.sleep(7)