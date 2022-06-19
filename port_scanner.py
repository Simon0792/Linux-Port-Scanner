'''This programs takes an ip address or website and scans for open ports. It than returns all the open ports and the time taken to complete the scan.
Written by Simone Onorato.
Kingston, Ontario.
For questions or support email simon.onorato@queensu.ca'''

import socket
import subprocess
import sys
from datetime import datetime

#Clear screen
subprocess.call('clear', shell=True)

#Ask user input for server address (IP or website)
remoteServer = input("Enter a server or website address: ")
remoteServerIP = socket.gethostbyname(remoteServer)

#Starting scan
print ("_" * 60)
print ("Please wait, scanning remote host", remoteServerIP)
print ("_" *60)
timeStart = datetime.now() #Save scan starting time

#Specifing port and handling errors
try:
    for port in range (5000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result ==0:
            print ("Port {}:        Open".format(port))
            sock.close()

except KeyboardInterrupt: #if Ctrl+C pressed, quit the program.
    print ("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print ("Hostname could not be resolved. Exiting")
    sys.exit()

except socket.error:
    print ("Couldn't connect to server")
    sys.exit()


#Completing the scan
timeEnd = datetime.now()
totalTime = timeEnd - timeStart

#Printing the information on screen
print ('Scanning Completed in ', totalTime)