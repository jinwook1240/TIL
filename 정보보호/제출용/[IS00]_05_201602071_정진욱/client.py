#!/usr/bin/python3
import socket
import MCipher as MCipher

def client_program():
 host = '127.0.0.1'
 port = 5461
 
 keyReceive = False
 client_socket = socket.socket()
 client_socket.connect((host, port))
 
 if(keyReceive == False):
  key = client_socket.recv(1024).decode()
  print('key : ' + key)
  client_socket.send('key exchange Success'.encode())
  iv = client_socket.recv(1024).decode()
  print('iv : ' + iv)
  client_socket.send('iv exchange Success'.encode())
  keyReceive = True
  cipher = MCipher.setAES(key, iv);
  
  if(keyReceive):
   message = input(' -> ')
   while message.lower().strip() != 'bye':
    client_socket.send(MCipher.AES_Encrypt(cipher, message))
    data = client_socket.recv(1024)
    data = MCipher.AES_Decrypt(cipher, data).decode()
    print('Received from user1 : ' + data)
    
    message = input(" -> ")
  client_socket.close()
  
if __name__ == '__main__':
 client_program()