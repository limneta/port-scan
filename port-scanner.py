import socket
from datetime import datetime

def is_open(host, port):
    s = socket.socket()
    try:
        s.connect((host, port))
    except:
        return False
    else:
        return True

ip = input("Enter the host: ")

try:
    lp = int(input("Scan from port:"))
    up = int(input("Up to port:"))
except:
    print("Try again. Be sure to enter an integer")
    quit()

st = datetime.now()

for port in range(lp, up):
    if is_open(ip, port):
        print("Port", port, "is open")
    else:
        print("Port", port, "is not open")

et = datetime.now()

tt = et - st

print("Scan took", tt)
