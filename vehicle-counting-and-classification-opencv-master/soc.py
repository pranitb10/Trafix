import socket

s=socket.socket()
print("success")
port=8080
s.bind(('',port))
print("socket binded to %s" %(port))
s.listen(1)
print("listening")

c, addr = s.accept()
print("got connection")
c.close()