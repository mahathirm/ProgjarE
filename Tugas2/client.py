
import socket
import select

UDP_IP = "127.0.0.1"
IN_PORT = 5005 


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, IN_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    data1 = data[:5] + "out.jpg"  
    file_name = data1 
    f = open(file_name, 'wb')

    while True:
        data1, addr = sock.recvfrom(15360)
        f.write(data1)   
	f.close()
	break
f.close()
        