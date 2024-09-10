#!/bin/python3

import socket

HOST = "127.0.0.1"
PORT = 5412

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET is IPv4
#SOCK_STREAM is port

s.connect((HOST,PORT))
