#!/usr/bin/python
import socket #Importing the socket library

buffer =  'A' * 5000

#connecting
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("IP", PORT))

#sending
s.send(buffer)
s.close()
