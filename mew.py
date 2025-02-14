import socket
import sys
from datetime import datetime

target = input(str('Target IP: '))

try:

    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
    
        #Return open port
        result = s.connect_ex((target,port))
        if result == 0:
            print('[*] Port {} is open'.format(port))
        s.close
except KeyboardInterrupt:
    print('\n Exiting :(')
    sys.exit
    
except socket.error:
    print('Host not responding')
    sys.exit